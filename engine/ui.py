from __future__ import annotations
from typing import List, Tuple, Optional
from abc import ABC, abstractmethod
import pygame
#from pygame import Surface, Rect, Mask, Font, Color


class UI:
    '''
    User interface
    '''
    def __init__(self,title:str, width:int, height:int) -> none:
        '''
        Init game window with title and size
        '''
        pygame.init()
        pygame.display.set_caption(title)
        self._screen  = pygame.display.set_mode((width, height))

    def screen(self) -> Surface:
        return self._screen
       
       