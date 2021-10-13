from __future__ import annotations
from typing import List, Tuple, Optional
from abc import ABC, abstractmethod
from copy  import deepcopy
from pygame.sprite import Sprite
from sse.engine.imoveable import IMoveable
from sse.engine.vector import Vector
from sse.engine.bounds import Bounds

class IController(ABC):
    """
    IController interface for IMoveable entities
    """
    def __init__(self, initialPosition:Vector, speed:Vector,
                       bounds:Bounds, 
                       removeAtEdge: Optional[bool] = False) -> None:
        """
        :param  initialPosition     [x,y]
        :param  speed               [x,y,z] in pixels per second
        :param  bounds              [xmin,xmax,ymin,ymax,zmin,zmax]
        :param  removeAtEdge        remove 
        """
        self._entity       : IMoveable = None
        self._initialPos   : Vector = initialPosition  #initial position 
        self._position     : Vector = deepcopy(initialPosition)  #current position 
        self._speed        : Vector = speed           
        self._bounds       : Bounds = bounds    
        self._removeAtEdge : bool   = removeAtEdge     #Remove if reached the bounds edge   
        
    
    @property
    def entity(self) -> IMoveable:
        return self._entity 
        
    @entity.setter        
    def entity(self, entity:IMoveable) -> None:
        self._entity = entity

    @property                              
    def position(self):
        return self._position                    
    
    def reset(self):
        self._position = deepcopy(self.initialPosition)

    @abstractmethod
    def read(self, dt:float, colList:List[Sprite]) -> None:
        """
        Control associated entity
        By default does nothing, override in descendant to implement behaviouy
        :param dt:     time elapsed since last frame
        :param colList list of entities that overlaped in current frame
        """
        pass