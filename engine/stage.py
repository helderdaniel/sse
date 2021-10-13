from __future__ import annotations
from typing import List, Tuple, Optional
from abc import ABC, abstractmethod
import pygame
from pygame.sprite import *
from pygame.surface import Surface
from sse.engine.collider import Collider
from sse.engine.actor import Actor


class Stage(ABC):
    """
    Defines a scenario and actors that can interact with each other
    playing a scene.
    The scenario is a fixed image.
    If willing an animated background, do not define a scenario,
    but rather define an actor with size enough to fill the 
    camera display and that can be animated and play a Role, as
    the most distant actor.
    Can be used to define a game Level or part of a level
    """
    def __init__(self, scenarioFile : str=None, 
                       resize       : Optional[Tuple(int, int)]=None,
                       collider     : Collider=Collider()) -> None:
        """
        :param scenarioFile: File to loada an image to create a Stage
                             background surface over where Actors move
                             if None, does NOT define any scenario
        :param resize:       an optional desired redimension for the scenario 
                             (width, height)                             
        :param collider:     Colision detection configuration
        """
        self._scenario : Optional[Surface] = None
        if scenarioFile is not None:
            i = pygame.image.load(scenarioFile)
            if resize is not None:                 #resize image
                i = pygame.transform.scale(i, (resize[0], resize[1]))
            self._scenario = Surface.convert_alpha(i)    #convert for fast blitting keeping alpha channel
            
        self._collider : Collider    = collider
        self._pause    : bool        = False
        self._groups   : List[Group] = []
        

    def scenario(self) -> Optional[Surface]:
        return self._scenario

    def groups(self) -> List[Group]:
        return self._groups

    @abstractmethod
    def sceneEnded(self) -> bool:
        """
        Predicate used to find if the scene to be played in 
        the stage is completed
        Can be used to determine if level ended
        should be called when drawing each frame
        """
        raise NotImplementedError

    @abstractmethod
    def collisions(self) -> pygame.Sprite_dict:
        """
        Handle collisions
        """
        raise NotImplementedError



class SimpleStage(Stage):
    """
    Stage that have 3 groups of actors:
        Friends
        Foes

    that can be seen as different factions, and a neutral faction,
    or a fixed scenario:

        Neutral

    Neutral is drwan first, so it is always in background
    """
    def __init__(self, scenarioFile : str=None, 
                       resize       : Optional[Tuple(int, int)]=None,
                       collider     : Collider=Collider()) -> None:
        super().__init__(scenarioFile,resize,collider)
        #neutral is first, so it is plotted in background
        self._neutral = pygame.sprite.RenderUpdates()
        self._groups.append(self._neutral)
        self._foes = pygame.sprite.RenderUpdates()
        self._groups.append(self._foes)
        self._friends = pygame.sprite.RenderUpdates()
        self._groups.append(self._friends)

    def addFriend(self, a : Actor) -> None:
        self._friends.add(a)

    def addFoe(self, a : Actor) -> None:
        self._foes.add(a)

    def addNeutral(self, a : Actor) -> None:
        self._neutral.add(a)

    def collisions(self) -> None:
        for actor in self._foes:
            colList = spritecollide(actor, self._friends, 
                                    False, self._collider.detect)
            actor.collisions(colList) #Send list of collisions to actor

        for actor in self._friends:
            colList = spritecollide(actor, self._foes, 
                                    False, self._collider.detect)
            actor.collisions(colList) #Send list of collisions to actor


    """
    def _addMissiles(self, group):
        for a in group:
            shoot : Actor = a.shoot()
            if shoot is not None:
                group.add(shoot)

    def _addExplosions(self, collisions):
        for s in collisions:
            blow : Actor  = s.hit()
            if blow is not None:
                self._explosions.add(blow)

    def update(self, collisions):
        self._addMissiles(self._friends)
        self._addMissiles(self._foes)
        self._addExplosions(collisions)
    """

    def sceneEnded(self) -> bool:
        """
        :return: True if all foes group is empty
                 False otherwise.
        """
        return len(self._foes) == 0


    

