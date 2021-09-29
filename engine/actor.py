from __future__ import annotations
from typing import List, Tuple, Optional
import pygame
from pygame import Surface, Mask, Rect
from sse.ui.animation import Shape, Animation
from sse.engine.role import Role


class Actor(pygame.sprite.DirtySprite):
    
    def __init__(self, animations:List[Animation], role:Role) -> None:
        pygame.sprite.Sprite.__init__(self)
        self._animations : List[Animation] = animations #Sequence of images
        self._role       : Role            = role       #actor controller
        role.actor                         = self       #to call: role.read() 

        #Set initial image
        self.dirty           = 1
        self._animations[0].reset()  #todo select animation (from dict)
        shape      : Shape   = self._animations[0].current()
        self.image : Surface = shape.image
        self.mask  : Mask    = shape.mask
        self.rect  : Rect    = self.image.get_rect()
        

    """
    def copy(self) -> Actor:
        #Shalow copy
        return self.__class__(self, self._animations.copy(), self._role.copy())
    """                                

    def update(self, dt:float):
        """
        Updates actor according to role and time elapsed since last frame
        :param dt:  time elapsed since last frame
        """
        self._role.read(dt)

        """
        att   : Attitude    = self._getAttitude()
        move  : List[float] = att.move
        image : int         = att.image
        self._fire          = att.fire
        
        if att.kill:
            self.kill()
            return

        #update image if changed
        if image != 0:
            self.dirty = 1
            self._images.nextImage(image)
            self.image = self._images.image()
            self.mask  = self._images.mask() #current mask        

        #update position if changed
        if move[0]!=0:  
            self.dirty = 1    
            newx = self.rect.x + move[0]
            if newx >= self._area[0] and newx <= self._area[2]-self.rect.w:
                self.rect.x = newx
            else:
                if self._removeAtEdge:
                    self.kill()
            
        if move[1]!=0:  
            self.dirty = 1    
            newy = self.rect.y + move[1]
            if newy >= self._area[1] and newy <= self._area[3]-self.rect.h:
                self.rect.y = newy
            else:
                if self._removeAtEdge:
                    self.kill()                
        """
        

class Character(Actor):
    def __init__(self, Animation:Animation, role:Role,
                       blow:Optional[Actor]=None,
                       missile:Optional[Actor]=None) -> None:
        super().__init__(Animation, role)

        #Auxiliar Tool
        #Must have a select
        #The blow is not to be implemented here
        #use a dict of flipbook

        #Auxiliar actors (blow, shot)
        self._blow         : Actor     = blow
        self._missile      : Actor     = missile
        self._fire         : bool      = False

    """
    def copy(self) -> Actor:
        c = self.__class__(self, self._animations.copy(), self._role.copy())
        if self._blow is not None:          
            c._blow = self._blow.copy()
        if self._missile is not None:          
            c._missile = self._missile.copy()            
        c._fire = self._fire                           
        return c
    """
    
    """
    def shoot(self) -> Optional[Actor]:
        if not self._fire: return None

        self._fire = False
        if self._missile is not None:
            missile = self._missile.copy()
            x = self.rect.x + self.rect.width/2 
            y = self.rect.y + self.rect.height/2
            missile.rect.x = x
            missile.rect.y = y
        return missile

    def hit(self) -> Optional[Actor]:
        if self._blow is not None:
            x = self.rect.x - self.rect.width/2 
            y = self.rect.y - self.rect.height/2
            self._blow.rect.x = x
            self._blow.rect.y = y
        return self._blow
    """


"""
class Follower(Character):
    
    #Initialize with a controller already defined to make this class instances follow it
    
    def __init__(self, position : List[float], area : List[int,int,int,int],
                 value : float, images : ImageSequence, control : Controller,
                 blow : Actor = None, missile : Actor = None,
                 removeAtEdge : bool = False) -> None:
        super().__init__(position, area, value, images,
                         control, blow, missile,removeAtEdge)

    def _getAttitude(self):
        return self._control.lastAttitude()
"""