from __future__ import annotations
from typing import List, Tuple, Optional
from pygame.sprite import Sprite
from sse.engine.vector import Vector
from sse.engine.bounds import Bounds
from sse.engine.icontroller import IController

class Role(IController):
    """
    Role interface (controller) for Actors
    """
    def __init__(self, initialPosition:Vector, speed:Vector,
                 bounds:Bounds, 
                 removeAtEdge:Optional[bool]=False,
                 animFPS: Optional[int]=1, 
                 value:Optional[float]=0) -> None:
        """
        :param  initialPosition     [x,y]
        :param  speed               [x,y,z] in pixels per second
        :param  bounds              [xmin,xmax,ymin,ymax,zmin,zmax]
        :param  removeAtEdge
        :param  animFPS             Frames per second to animate actor
        :param  value
        """
        super().__init__(initialPosition, speed, bounds, removeAtEdge=removeAtEdge)

        self._animPeriod   : float  = 1/animFPS        #Animation period
        self._animDT       : float  = 0
        self._value        : float  = value            #value if destroyed




class RoleNone(Role):
    """
    Does not do anything.
    Default Role for Actors
    """
    def __init__(self) -> None:
        super().__init__(Vector(), Vector(), Bounds())



class RoleBounceSweep(Role):
    """
    Sweep left to right with margins
    """
    def __init__(self, initialPosition: Vector, speed: Vector,
                       bounds: Bounds, 
                       removeAtEdge: Optional[bool] = False, 
                       animFPS: Optional[int]=1, 
                       value: Optional[float]=0) -> None:
        super().__init__(initialPosition, speed, bounds, 
                         removeAtEdge, animFPS, value)
        self._diretion : Vector = Vector(1,1,1)


    def read(self, dt:float, colList:List[Sprite]) -> None:
        """
        :param dt:     time elapsed since last frame
        :param colList list of actors that overlaped in current frame
        """

        #Handle collisions
        if len(colList) > 0:
            #self._entity.kill()
            #return
            self._speed = self._speed.scalarProduct(-1)
            

        #Anim with specified frames/sec
        self._animDT += dt
        if self._animDT > self._animPeriod:
            self._animDT = 0
            self._entity.nextImage()
        
        #Move with specified speed in pixels/sec
        #Move after anim to update position
        for i in range(self._position.dim()):
            if  self._position.data[i] < self._bounds.data[i][0] or \
                self._position.data[i] > self._bounds.data[i][1]-self._entity.dim[i]:
                    self._diretion.data[i] *= -1 #invert
            self._position.data[i] += dt * self._speed.data[i] * self._diretion.data[i]

        self._entity.move(self._position)  
        


class RoleScroll(Role):
    """
    Sweep left to right with margins
    """
    def __init__(self, initialPosition: Vector, speed: Vector,
                       bounds: Bounds) -> None:
        speed.y *= -1                       
        super().__init__(initialPosition, speed, bounds)
        
    
    def read(self, dt:float, colList:List[Sprite]) -> None:
        """
        :param dt:     time elapsed since last frame
        :param colList list of actors that overlaped in current frame
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
        self._entity.move(pos)  

        print(self._position)
