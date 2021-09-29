from __future__ import annotations
from typing import List, Tuple, Optional
from abc import ABC, abstractmethod
#from sse.engine.actor import Actor #circular import, cause Actor imports Role


class Role:
    """
    Role (controller) for actor to play
    Controls the actor
    """
    def __init__(self, initialPosition:List[float,float], 
                 speed:List[float,float,float,float],
                 bounds:List[float,float,float,float], 
                 removeAtEdge:Optional[bool]=False,
                 value:Optional[float]=0) -> None:
        self._actor      : Actor                         = None
        self._initialPos : List[float,float]             = initialPosition #initial position 
        self._position   : List[float,float]             = initialPosition #current position 
        self._speed      : List[float,float,float,float] = speed           #[up, down, left, right]
        self._bounds     : List[float,float,float,float] = bounds          #[up, down, left, right]
        self._removeAtEdge : bool                        = removeAtEdge    #Remove if reached the bounds edge
        self._value      : float                         = value           #value if destroyed

    @property
    def actor(self) -> Actor:
        return self._actor 
        
    @actor.setter        
    def actor(self, actor:Actor) -> None:
        self._actor = actor

    """
    def copy(self) -> Role:
        #Shalow copy
        r = self.__class__(self, self._initialPosition, self._speed,
                                 self._bounds, self._removeAtEdge,
                                 self._value)
        r.actor = self._actor                              
        r.position = self._position
    """                         

    def read(self, dt:float) -> None:
        """
        :param dt:  time elapsed since last frame
        """
        #actor.move(3,4)