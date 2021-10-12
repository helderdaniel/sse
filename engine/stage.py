from __future__ import annotations
from typing import List, Tuple, Optional
from abc import ABC, abstractmethod
import pygame
from pygame.sprite import *
from sse.engine.collider import Collider
from sse.engine.actor import Actor


class Stage(ABC):
    """
    Defines a scenario and actors that can interact
    with each other playing a scene
    The scenario itself is an actor that can be animated and play a Role
    Can be used to define a game Level or part of a level
    """

    def __init__(self, scenario:Actor=None, collider:Collider=Collider()) -> None:
        """
        :param scenario: Stage background over where Actors move
                         if False, actors collided must be romoved by user
        :param collider: Colision detection configuration
        """
        self._scenario : Actor    = scenario
        self._collider : Collider = collider
        self._pause    : bool     = False
        self._groups   : List[pygame.sprite.Group] = []
        
        #Add scenario Actor as the first group to be blitted first
        #scenarioGroup = pygame.sprite.RenderUpdates()
        #scenarioGroup.add(scenario)
        #self._groups.append(scenarioGroup)

    def groups(self):
        return self._groups


    @abstractmethod
    def isCompleted(self) -> bool:
        """
        Predicate used to find if a stage is completed
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

    def __init__(self, scenario:Actor, collider:Collider=Collider()) -> None:
        super().__init__(scenario,collider)
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

    def isCompleted(self) -> bool:
        """
        :return: True if all foes group is empty
                 False otherwise.
        """
        return len(self._foes) == 0


    

