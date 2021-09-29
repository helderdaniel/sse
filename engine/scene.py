from __future__ import annotations
from typing import List, Tuple, Optional
from abc import ABC, abstractmethod
import pygame
from pygame import Surface, Rect, Mask


class Act:
    """
    Defines actors and background that can interact
    Can be used to define a game Level or part of a level
    """
    def __init__(self):
        pass

    def isCompleted(self) -> bool:
        """
        Predicate used to find if action is completed
        should be called when drawing each frame
        """
        pass

