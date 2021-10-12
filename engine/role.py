from __future__ import annotations
from typing import List, Tuple, Optional
from abc import ABC, abstractmethod
from copy  import deepcopy
from pygame.sprite import Sprite
from sse.engine.vector import Vector
from sse.engine.bounds import Bounds
#from sse.engine.actor import Actor #circular import, cause Actor imports Role


class Role(ABC):
    """
    Role (controller) for actor to play
    Controls the actor
    """
    def __init__(self, initialPosition:Vector, speed:Vector,
                 animFPS: int, bounds:Bounds, 
                 removeAtEdge:Optional[bool]=False,
                 value:Optional[float]=0) -> None:
        """
        :param  initialPosition     [x,y]
        :param  speed               [x,y,z] in pixels per second
        :param  bounds              [xmin,xmax,ymin,ymax,zmin,zmax]
        :param  removeAtEdge
        :param  value
        """
        self._actor        : Actor  = None
        self._initialPos   : Vector = initialPosition  #initial position 
        self._position     : Vector = deepcopy(initialPosition)  #current position 
        self._speed        : Vector = speed           
        self._bounds       : Bounds = bounds          
        self._animPeriod   : float  = 1/animFPS        #Animation period
        self._animDT       : float  = 0
        self._removeAtEdge : bool   = removeAtEdge     #Remove if reached the bounds edge
        self._value        : float  = value            #value if destroyed

    @property
    def actor(self) -> Actor:
        return self._actor 
        
    @actor.setter        
    def actor(self, actor:Actor) -> None:
        self._actor = actor

    @property                              
    def position(self):
        return self._position

    """
    def copy(self) -> Role:
        #Shalow copy
        r = self.__class__(self, self._initialPosition, self._speed,
                                 self._bounds, self._removeAtEdge,
                                 self._value)
        r.actor = self._actor                              
        r.position = self._position
    """                         
    
    def reset(self):
        self._position = deepcopy(self.initialPosition)

    def read(self, dt:float, colList:List[Sprite]) -> None:
        """
        Control associated actor
        By default does nothing, override in descendant to implement behaviouy
        :param dt:     time elapsed since last frame
        :param colList list of actors that overlap in current frame
        """
        pass



class RoleNone(Role):
    """
    Does not do anything.
    Default Role for Actors
    """
    def __init__(self) -> None:
        super().__init__(Vector(), Vector(), 1, Bounds())



class RoleBounceSweep(Role):
    """
    Sweep left to right with margins
    """
    def __init__(self, initialPosition: Vector, speed: Vector,
                       animFPS: int, bounds: Bounds, margins: Bounds,
                       removeAtEdge: Optional[bool] = False, 
                       value: Optional[float] = 0) -> None:
        super().__init__(initialPosition, speed, animFPS, bounds,
                         removeAtEdge=removeAtEdge, value=value)
        self._margins  : Bounds = margins
        self._diretion : Vector = Vector(1,1,1)


    def read(self, dt:float, colList:List[Sprite]) -> None:
        """
        :param dt:     time elapsed since last frame
        :param colList list of actors that overlap in current frame
        """

        #Handle collisions
        if len(colList) > 0:
            #self._actor.kill()
            #return
            self._speed = self._speed.scalarProduct(-1)
            

        #Anim with specified frames/sec
        self._animDT += dt
        if self._animDT > self._animPeriod:
            self._animDT = 0
            self._actor.nextImage()
        
        #Move with specified speed in pixels/sec
        #Move after anim to update position
        for i in range(self._position.dim()):
            if  self._position.data[i] < self._bounds.data[i][0]+self._margins.data[i][0] or \
                self._position.data[i] > self._bounds.data[i][1]-self._margins.data[i][1]-self._actor.dim[i]:
                    self._diretion.data[i] *= -1 #invert
            self._position.data[i] += dt * self._speed.data[i] * self._diretion.data[i]

        self._actor.move(self._position)  
        


class RoleScroll(Role):
    """
    Sweep left to right with margins
    """
    def __init__(self, initialPosition: Vector, speed: Vector,
                       bounds: Bounds) -> None:
        speed.y *= -1                       
        super().__init__(initialPosition, speed, 1, bounds)
        
    
    def read(self, dt:float, colList:List[Sprite]) -> None:
        """
        :param dt:     time elapsed since last frame
        :param colList list of actors that overlap in current frame
        """
        #Move with specified speed in pixels/sec
        for i in range(self._position.dim()):
            self._position.data[i] += dt * self._speed.data[i]
            if self._position.data[i] < self._bounds.data[i][0]:
                self._position.data[i] = self._initialPos.data[i]
            if self._position.data[i] > self._bounds.data[i][1]:
                self._position.data[i] = self._initialPos.data[i]

        #Invert coordinate to display
        pos = self._position.scalarProduct(-1)
        self._actor.move(pos)  

        print(self._position)
