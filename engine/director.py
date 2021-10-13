from __future__ import annotations
from typing import List, Tuple, Optional
import pygame
from sse.engine.stage import Stage
from sse.ui.camera import Camera
from sse.ui.guiconfig import GUIconfig

class Director:
    """
    The Director have a set of Stages where scenes are played by stage order
    Stages can be seen as a set of game levels
    :param camera:   View point and zoom to take pictures
    :param stages:   List of stages to play scenes
    :param guicfg:   Configuration for GUI 
    """
    def __init__(self, camera : Camera, stages:List[Stage], guicfg:GUIconfig=GUIconfig()):
        self._camera = camera
        self._stages = stages
        self._guicfg = guicfg
        self._pause : bool = False


    def action(self) -> None:
        """
        Starts scenes one Stages one by one
        :return: True if all scenes in all Stages are completed (a game finished)
                 False if at some Stage(level) a scene was interrupted
        """
        for stage in self._stages:
            if self._play(stage) == False:  #interrupt
                return False    
        return True


    def _update(self, groups, dt):
        '''
        update all Actors in groups[]
        '''
        #move and plot updated objects
        objectsToDraw : pygame.sprite.Group = []
        for g in groups:
            g.update(dt)
        return objectsToDraw

    
    def _play(self, stage:Stage):
        """
        Plays the scene on the stage 
        This is the scene (or game) loop 
        """ 
        if stage.scenario() is not None:
            self._camera.setScenario(stage)

        while True:           
            #get event (to test quit (remove from contoler))
            events = pygame.event.get()

            #Check pause and quit:
            #todo: Pause is hardwired
            for event in events:
                if self._guicfg.pause(event): self._pause = not self._pause
                if self._guicfg.quit(event):  return False

            if not self._pause:
                actors = self._update(stage.groups(), self._camera.dt())  #update actors attitude with controllers
                stage.collisions()                  #detect collisions and send info to actors
                if stage.scenario() is not None:
                    self._camera.restore(stage)     #restore scenario
                self._camera.shoot(stage)           #draw frame

                if stage.sceneEnded():
                    return True
     