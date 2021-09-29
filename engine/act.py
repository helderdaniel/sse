from __future__ import annotations
from typing import List, Tuple, Optional
from abc import ABC, abstractmethod
from sse.engine.scene import Scene

class Act:
    """
    An act is a set of scenes that are played in order
    It can be seen as a game and a set of levels
    """
    def __init__(self, scenes:List[Scene]):
        self._scenes = scenes

    def play(self) -> None:
        """
        Play scenes one by one
        :return: True if act (game) completed
                 False if at some scene(level) the act(game) was interrupted
        """
        for sc in self._scenes:
            if sc.play() == False:  #interrupt
                return False    
        return True
