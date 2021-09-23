from __future__ import annotations
import pygame
from pygame import Surface


class GUI:
    """
    User interface
    """
    def __init__(self, title:str, width:int, height:int) -> None:
        """
        Init game window with title
        """
        pygame.init()
        pygame.display.set_caption(title)
        self._screen : Surface = pygame.display.set_mode((width, height))
