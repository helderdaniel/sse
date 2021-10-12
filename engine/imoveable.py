from abc import ABC, abstractmethod
from sse.engine.vector import Vector

class IMoveable(ABC):
    """
    IMoveable interface for moveable objects
    """
    @abstractmethod
    def move(self, p:Vector):
        """
        move to a p position
        """
        pass