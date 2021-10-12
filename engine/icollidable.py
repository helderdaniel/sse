from typing import List
from abc import ABC, abstractmethod
from pygame.sprite import Sprite

class ICollidable(ABC):
    """
    ICollidable interface for moving objects
    """
    @abstractmethod
    def collisions(self, colList:List[Sprite]):
        self._collisions = colList
        """
        Set list of overlaped Actors in current frame
        """
        pass