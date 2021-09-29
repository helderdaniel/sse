from __future__ import annotations
from typing import List, Tuple, Optional
from abc import ABC, abstractmethod


class ActorInfo(ABC):
    """
    Basic actor info, such as:

    value
    strength
    stamina
    (...)

    Must be defined for the type of actor desired
    """
    pass


class ValueStrengthInfo(Info):
    """
    basic actor info on:
        value
        strength
    """
    def __init__(self, value:float, strength:float) -> None:
        super.__init__()
        self._value   :float = value
        self._strength:float = strength

    @property        
    def value(self) -> float:
        return self._value

    @property        
    def strength(self) -> float:
        return self._strength
