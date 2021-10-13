from __future__ import annotations
from typing import List, Tuple, Optional
import pygame
from pygame import Surface
from sse.engine.stage import Stage
from sse.engine.imoveable import IMoveable

#TODO: Camera controller 
#A role can descende form a position Controller ??

class Camera(IMoveable):
    """
    Camera to take shoots from some position and zomm of a scene
    """
    def __init__(self, title:str, width:int, height:int, fps:int) -> None:
        """
        Init a camera window with a title

        :param title:      Camera window title
        :param width:      Camera window width in pixels
        :param height:     Camera window height in pixels
        :param fps:        Maximum number of frames per second                    
        """ 
        pygame.init() 
        pygame.display.set_caption(title)
        
        flags = pygame.DOUBLEBUF | pygame.HWSURFACE 
        self._screen : Surface = pygame.display.set_mode((width, height), flags)
        
        self._dt  : float = 0    #diff time between frames in seconds
        self._fps : int   = fps 
        

    def dt(self) -> float:
        return self._dt

    def move(self, p:Vector):
        pass

    def setScenario(self, stage:Stage) -> None:
        '''
        Set scenario
        '''
        self._screen.blit(stage.scenario(), (0, 0))
        pygame.display.update()
        
    def restore(self, stage:Stage) -> None:
        '''
        restore scenario removing all objects in groups[]
        '''
        for g in stage.groups():
            g.clear(self._screen, stage.scenario())    


    def shoot(self, stage:Stage) -> None:
        '''
        Take picture, actually draw frame
        '''
        #set maximum FPS
        #dt is time since last call in secs (convert ms to secs)
        self._dt = pygame.time.Clock().tick(self._fps) / 1000 
        #print("{:.2f} {}".format(1/(self._dt), self._dt))
        
        actors : pygame.sprite.Group = []
        for g in stage.groups():
            actors += g.draw(self._screen)

        if stage.scenario() is None:
            pygame.display.flip()           #flip double buffer
        else:
            pygame.display.update(actors)   #update actors over scenario
            

        """
        Using display.update() to repaint background over sprites and 
        display.update(List[Sprites]) again to redraw them on a new position
        This can be faster, but only can be used with fixed backgrounds
        
        Using display.flip() to update background means that
        surfaces and sprites are drawn, ie. copied or blited, to another area
        of video memory that is not currently being displayed. At the vertical
        retrace, ie. when the previous frame was fully drawn, and the next one
        did not started to be drawn yet, the pointer to the address of the area
        of video memory to display next is changed to the area where sprites 
        were drawn, the double buffer. This has a swap screen effect and is much
        faster than copying the whole image. This also avoids screen tearing, ie.
        part of the previous frame to be drawn with part of the next frame, since
        the swapping to the double buffer is made when the hardware is not updating
        the display.  
        """
       
        