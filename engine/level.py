from __future__ import annotations
from typing import List, Tuple, Optional
from abc import ABC, abstractmethod
import pygame
from pygame import Surface, Rect, Mask


class Level:
    '''
    Defines entities and background in a Level
    and completed criteria
    '''
    def __init__(self):
        pass

    def isCompleted(self) -> bool:
        '''
        Predicate used to find if levelis completed
        should be called when drawing each frame
        '''
        pass

