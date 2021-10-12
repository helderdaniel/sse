from __future__ import annotations
from typing import List, Tuple, Optional
from abc import ABC, abstractmethod
import pygame
from pygame import Surface, Rect, Mask, Color
from pygame.font import Font


class Shape:
    """
    Holds image, Rect, Mask (for collisions) and layer
    """
    def __init__(self, image:Surface, mask:Mask, rect:Rect=None, layer:int=0) -> None:
        self._image: Surface = image
        self._mask : Mask    = mask
        self._rect : Rect    = rect
        if rect is None:
            self._rect = image.get_rect()
        
        self._layer: int     = layer

    @property
    def image(self) -> Surface:
        return self._image

    @property
    def rect(self) -> Rect:
        return self._rect

    @property
    def mask(self) -> mask:
        return self._mask

    @property
    def layer(self) -> int:
        return self._layer


class Animation(ABC):
    """
    Define animation sequences for actors and background
    """

    def reset(self) -> None:
        """
        Resets shape
        """
        pass

    @abstractmethod
    def current(self) -> Shape:
        """
        Return current image, rect and mask
        """
        pass


class Scroll(Animation):
    """
    Used to implement a window that shows part of an image
    window can be moved to show the desired portion of the image
    """
    def __init__(self,  imageFile       : str,
                        dim             : Tuple[int, int],
                        resize          : Optional[Tuple[int, int]]=None) -> None:
        """
        :param ImageFile       is the filename of the images: jpg, bmp, png (preserves alpha channel)
        :param dim             is the desired dimension of area to show (width, height)
        :param resize          is an optional desired redimension (width, height)
        """
        
        #load and resize image
        i = pygame.image.load(imageFile)
        if resize is not None:             
            i = pygame.transform.scale(i, (resize[0], resize[1]))
            i = pygame.Surface.convert_alpha(i) 
        self.image = i
        self.rect = i.get_rect()
        self.rect.w = dim[0]
        self.rect.h = dim[1]
        self.mask   = pygame.mask.from_surface(self.image)

    def current(self) -> Shape:
        """
        Return current definition
        """
        return Shape(self.image, self.mask, self.rect)

    def show(self, x:int, y:int) -> None:
        self.rect.x = x
        self.rect.y = y

    
class FlipBook(Animation):
    """
    A group of images that can be changed in 2 directions
    """
    def __init__(self,  imageFiles   : List[str],
                        resize       : Optional[Tuple[int, int]]=None,
                        initialImage : Optional[int]=0) -> None:
        """
        :param ImageFile    is a list of filenames to images: jpg, bmp, png (preserves alpha channel)
        :param initialImage is the index of the initial image to set as current
        :param resize       is an optional desired redimension (width, height)
        """
        self._initialImage : int = initialImage
        self._currentImage : int = self._initialImage
        self._images : List[Surface] = []
        self._masks  : List[Mask]    = []   #avoid recomputing of mask when changed
        for f in imageFiles:
            i = pygame.image.load(f)
            if resize is not None:             #resize image
                i = pygame.transform.scale(i, (resize[0], resize[1]))
            i = pygame.Surface.convert_alpha(i)    #convert for fast blitting keeping alpha channel
            self._images.append(i)
            m = pygame.mask.from_surface(i)
            self._masks.append(m)

    def copy(self):
        #Implement shallow copy to reuse images and masks.
        #Present implementation is similar to copy.copy()
        fb : FlipBook = self.__class__([])  #This way can be used with subclasses
        fb._images = self._images
        fb._masks  = self._masks
        fb._initialImage = self._initialImage
        fb._currentImage = self._currentImage
        return fb
    
    def size(self) -> int:
        """
        return number of images in flipbook
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
        decrement the index of current image back to the first
        """
        if self._currentImage > 0:
            self.set(self._currentImage - 1)

    def next(self) -> None:
        """
        increment the index of current image until the last
        """
        if self._currentImage < self.size()-1:
            self.set(self._currentImage + 1)

    def current(self) -> Shape:
        """
        Return current definition
        """
        i = self._images[self._currentImage]
        m = pygame.mask.from_surface(i)
        return Shape(i, m)


class FlipBookCircular(FlipBook):
    """
    A group of images that can be changed in a circular fashion
    """

    def prev(self) -> None:
        """
        decrement the index of current image in a circular fashion
        """
        self.set(self._currentImage - 1)

    def next(self) -> None:
        """
        increment the index of current image in a circular fashion
        """
        self.set(self._currentImage + 1)


class Text(Animation):
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

    def current(self) -> Shape:
        """
        Return current definition
        """
        i = self._font.render(self._fmt.format(self._text), True, self._color)
        m = pygame.mask.from_surface(i)
        return Shape(i, m)
    