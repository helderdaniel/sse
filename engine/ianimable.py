from abc import ABC, abstractmethod

class IAnimable(ABC):
    """
    IAnimable interface for animable objects
    """
    @abstractmethod
    def selectAnimation(self, idx:int) -> None:
        """
        Select animation in use
        """
        pass

    @abstractmethod    
    def setImage(self, idx:int) -> None:
        """
        Set image in the animation in use
        """
        pass

    @abstractmethod
    def prevImage(self) -> None:
        """
        Previous image in the animation in use
        """
        pass

    @abstractmethod
    def nextImage(self) -> None:
        """
        Next image in the animation in use
        """
        pass