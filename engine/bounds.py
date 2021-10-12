from __future__ import annotations
from typing import List, Tuple
from typing import Tuple

class Bounds:
    """
    Defines 3D bounds
    """

    _xpos = 0
    _ypos = 1
    _zpos = 2

    def __init__(self, xmin:float=0, xmax:float=0,
                       ymin:float=0, ymax:float=0,
                       zmin:float=0, zmax:float=0):
        self._data : List[Tuple(float,float)] = [(xmin,xmax),(ymin,ymax),(zmin,zmax)]

    @property
    def data(self) -> List[Tuple(float,float)]: return self._data

    @property
    def x(self) -> Tuple(float,float): return self._data[self._xpos]
    @property
    def y(self) -> Tuple(float,float): return self._data[self._ypos]
    @property
    def z(self) -> Tuple(float,float): return self._data[self._zpos]