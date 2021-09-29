from __future__ import annotations
from typing import List, Tuple, Optional
from abc import ABC, abstractmethod
import pygame, time
from sse.ui.stage import Stage
from sse.engine.actor import Actor


class Scene(ABC):
    """
    Defines actors and background that can interact
    Can be used to define a game Level or part of a level
    """

    def __init__(self, stage : Stage, kill:bool=True) -> None:
        """
        :param stage: GUI
        :param kill:  if True remove actors that have collided.
                      if False, actors collided must be romoved by user
        """
        self._stage = stage
        self._kill  = kill
        self._groups : List[pygame.sprite.Group] = []


    #to implement
    def pause(self) -> None:
        """
        Pause action
        """
        pass

    #to implement
    def resume(self) -> None:
        """
        Resume action
        """
        pass

    @abstractmethod
    def isCompleted(self) -> bool:
        """
        Predicate used to find if a scene is completed
        Can be used to determine if level ended
        should be called when drawing each frame
        """
        pass

    #todo: move to Act
    def play(self):
        """
        Plays the scene.
        This is the act (or game) loop 
        """

        avg  = []
        avgm = 100
        while True:
            start = time.perf_counter()
            
            #time elapsed since last frame
            dt = pygame.time.Clock().get_fps() 

            #get event (to test quit (remove from contoler))
            events = pygame.event.get()

            #Check quit:
            for event in events:
                if event.type == pygame.QUIT:
                    return False

            self._stage.restore(self._groups)        #remove actors
            actors = self._stage.move(self._groups, dt)  #update actor positions with controllers
            collisions = self.collisions()        #detect collisions
            #self.update(collisions)               #user defined game logic

            self._stage.draw(actors)                 #draw frame

            stop = time.perf_counter()

            avg.append(1/(stop-start))
            if len(avg)>avgm:
                del avg[0]
            sum = 0
            for i in avg:
                sum += i

            print(pygame.time.Clock().get_fps(), sum/len(avg), stop-start, dt)

            if self.isCompleted():
                return True


class SimpleScene(Scene):
    """
    Scene that have 3 groups of actors:
        Friends
        Foes

    that can be seen as different factions, and a neutral faction:
        Neutral
    """

    def __init__(self, stage : Stage) -> None:
        super().__init__(stage)
        self._foes = pygame.sprite.RenderUpdates()
        self._groups.append(self._foes)
        self._friends = pygame.sprite.RenderUpdates()
        self._groups.append(self._friends)
        self._neutral = pygame.sprite.RenderUpdates()
        self._groups.append(self._neutral)


    def addFriend(self, p : Actor) -> None:
        self._friends.add(p)

    def addFoe(self, f : Actor) -> None:
        self._foes.add(f)

    def addNeutral(self, f : Actor) -> None:
        self._foes.add(f)

    def collisions(self):
        foes = pygame.sprite.groupcollide(self._foes, self._friends,
                                          False, False,
                                          pygame.sprite.collide_mask)
        friends = pygame.sprite.groupcollide(self._friends, self._foes,
                                             self._kill, self._kill,
                                             pygame.sprite.collide_mask)
        all = foes | friends
        return all

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


    

