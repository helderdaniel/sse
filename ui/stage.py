from __future__ import annotations
from typing import List, Tuple, Optional
import pygame
from pygame import Surface
from sse.engine.actor import Actor

#Todo implement a stage wider than the window

class Stage:
    """
    Stage to play: the User Interface
    """
    def __init__(self, title:str, width:int, height:int, fps:int, 
                       background:Actor=None, redraw:bool=False) -> None:
        """
        Init game a window with a title

        :param title:      Window title
        :param width:      Window width in pixels
        :param height:     Window height in pixels
        :param fps:        Maximum number of frames per second
        :param background: Stage background over where Actors move
        :param redraw:     If True redraws only portions of background where sprites
                           are using display.update() to repaint background over sprites and 
                           display.update(List[Sprites]) again to redraw them on a new position
                           This can be faster, but only can be used with fixed backgrounds
                           
                           If False use display.flip() to update background. This means that
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
        pygame.init() 
        pygame.display.set_caption(title)
        
        if redraw: flags = 0
        else:      flags = pygame.DOUBLEBUF | pygame.HWSURFACE 
        self._screen : Surface = pygame.display.set_mode((width, height), flags)
        
        self._fps         = fps 
        self._background = background
        self._redraw     = redraw


    def restore(self, groups : List[pygame.sprite.Group]):
        '''
        restore backgroung removing all Actors in groups[], if
        redraw is True (only can be used with fixed background)
        '''
        if self._redraw:
            for g in groups:
                #clear all objects from screen
                g.clear(self._screen, self._bgImage)


    def move(self, groups : pygame.sprite.Group, dt:float) -> List[pygame.Rect]:
        '''
        plot all Actors in groups[] over background
        '''
        #move and plot updated objects
        objectsToDraw : pygame.sprite.Group = []
        for g in groups:
            g.update(dt)
            objectsToDraw += g.draw(self._screen)
        return objectsToDraw


    def draw(self, objectsToDraw) -> None:
        '''
        actually draw frame
        '''
        if self._redraw:
            pygame.display.update(objectsToDraw)   #draw only changed Actors
        else:
            pygame.display.flip()                  #flip double buffer
        
       
        