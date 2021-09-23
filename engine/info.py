from __future__ import annotations
from typing import List, Tuple, Optional
from abc import ABC, abstractmethod


class Info(ABC):
    '''
    Basic entities info, such as:

    value
    strength
    stamina
    (...)

    Must be defined for the type of entity desired
    '''
    pass


class ValueStrengthInfo(Info):
    '''
    basic entity info on:
        value
        strength
    '''
    def __init__(self, value:float, strenght:float) -> None:
        super.__init__()
        self._value   :float = value
        self._strength:float = strenght

    @property        
    def value(self) -> float:
        return self._value

    @property        
    def strength(self) -> float:
        return self._strength
