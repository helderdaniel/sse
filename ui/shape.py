from __future__ import annotations
from typing import List, Tuple, Optional
from abc import ABC, abstractmethod
import pygame
from pygame import Surface, Rect, Mask, Color
from pygame.font import Font


class ImageDefinition:
    """
    Holds image, Rect and Mask (for collisions)
    """
    def __init__(self, image:Surface, mask:Mask) -> None:
        self._image: Surface = image
        self._rect : Rect    = image.get_rect()
        self._mask : Mask    = mask

    @property
    def image(self) -> Surface:
        return self._image

    @property
    def rect(self) -> Rect:
        return self._rect

    @property
    def mask(self) -> mask:
        return self._mask


class Shape(ABC):
    """
    Define shapes for entities and background
    """

    @abstractmethod
    def reset(self) -> None:
        """
        Resets shape
        """
        pass

    @abstractmethod
    def current(self) -> ImageDefinition:
        """
        Return current image, rect and mask
        """
        pass



class FlipBook(Shape):
    """
    A group of images that can be changed with some criteria to
    implement animation
    """
    def __init__(self,  imageFiles   : List[str],
                        dim          : Optional[Tuple[int, int]]=None,
                        initialImage : int = 0) -> None:
        """
        ImageFile    is a list of filenames to images: jpg, bmp, png (preserves alpha channel)
        dim          is the desired dimension (width, height)
        initialImage is the index of the initial image to set as current
        """
        self._initialImage : int = initialImage
        self._currentImage : int = self._initialImage
        self._images : List[Surface] = []
        self._masks  : List[Mask]    = []   #avoid recomputing of mask when changed
        for f in imageFiles:
            i = pygame.image.load(f)
            if dim is not None:             #resize image
                i = pygame.transform.scale(i, (dim[0], dim[1]))
            i = pygame.Surface.convert_alpha(i)    #convert for fast blitting keeping alpha channel
            self._images.append(i)
            m = pygame.mask.from_surface(i)
            self._masks.append(m)
        self.reset()


    def copy(self):
        """
        Implement shallow copy to reuse images and masks.
        Present implementation is similar to copy.copy()
        """
        fb : FlipBook = self.__class__([])
        fb._images = self._images
        fb._masks  = self._masks
        fb._currentImage = self._currentImage
        return fb

    def size(self) -> int:
        """
        return number of images in shape
        """
        return len(self._images)

    def reset(self) -> None:
        """
        Set the index of current image to: initialImage
        """
        self._currentImage = self._initialImage

    def set(self, idx:int) -> None:
        """
        sets index of current image.
        Index is put in range with: idx % self.size
        """
        self._currentImage = idx % self.size()

    def prev(self) -> None:
        """
        decrement the index of current image
        """
        self.set(self._currentImage - 1)

    def next(self) -> None:
        """
        increment the index of current image
        """
        self.set(self._currentImage + 1)

    def current(self) -> ImageDefinition:
        """
        Return current definition
        """
        i = self._images[self._currentImage]
        m = pygame.mask.from_surface(i)
        return ImageDefinition(i, m)


class Text(Shape):
    """
    Shape to display text messages
    """
    def __init__(self, font:Font, size:int, color:Color,
                       bold:bool=False, italic:bool=False, fmt:str="{}"):
        self._color : Color  = color
        self._fmt   : str    = fmt
        self._font  : Font   = pygame.font.SysFont(font, size, bold, italic)
        self._text = ""
        self.reset()

    def reset(self) -> None:
        """
        Clear text message to display
        """
        self._text = ""

    def set(self, message:str) -> None:
        """
        Sets text message to display
        """
        self._text = message

    def current(self) -> ImageDefinition:
        """
        Return current definition
        """
        i = self._font.render(self._fmt.format(self._text), True, self._color)
        m = pygame.mask.from_surface(i)
        return ImageDefinition(i, m)
    