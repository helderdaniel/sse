from __future__ import annotations
from typing import List
import math

class Vector:

    _xpos = 0
    _ypos = 1
    _zpos = 2

    """
    Defines a 3D vector
    Can be used to give a position, a speed vector, etc.
    """
    def __init__(self, x:float=0, y:float=0, z:float=0):
        self._data : List[float] = [x,y,z]

    def copy(self):
        return self.__class__(self.x, self.y, self.z)

    def dim(self):
        return len(self._data)

    @property
    def data(self) -> List:
        return self._data
    
    @property
    def x(self) -> float:
        return self._data[self._xpos]
    
    @x.setter
    def x(self, x) -> float:
        self._data[self._xpos] = x

    @property
    def y(self) -> float:
        return self._data[self._ypos]
    
    @y.setter
    def y(self, y) -> float:
        self._data[self._ypos] = y

    @property
    def z(self) -> float:
        return self._data[self._zpos]
    
    @z.setter
    def z(self, z) -> float:
        self._data[self._zpos] = z


    def add(self, s) -> Vector:
        """
        scalar and vector addition. To subtract use the symmetric
        :param s    a float or a Vector to add
        :returns    a Vector
        """
        if isinstance(s, float):
            return Vector(self.x + s, self.y + s, self.z + s)
        if isinstance(s, Vector):                
            return Vector(self.x + s.x, self.y + s.y, self.z + s.z)
        raise NotImplementedError("argument must be a float or a Vector")


    def scalarProduct(self, n:float) -> Vector:
        """
        :param n    a scalar to multiply with this vector
        :returns:   a new vector, which is product of scalar n by this Vector
        """
        return Vector(self.x * n, self.y * n, self.z * n)


    def dotProduct(self, v:Vector) -> float:
        """
        :param v    a vector to operate with this vector
        :returns:   a new vector, which is dot product of this Vector and v
        """
        return self.x * v.x + self.y * v.y + self.z * v.z
        

    def move(self, dx,dy,dz):
        """
        Move this vector
        :param dx   x-axis differential to move
        :param dy   y-axis differential to move
        :param dz   z-axis differential to move
        """
        self.x += dx
        self.y += dy
        self.z += dz


    def length(self):
        """
        :return the length or modulus of this vector
        """
        sum = 0
        for i in range(self.dim()):
            sum += self._data[i] * self._data[i]
        return math.sqrt(sum)

    def __str__(self):
        return "({},{},{})".format(self._data[self._xpos], 
                                   self._data[self._ypos], 
                                   self._data[self._zpos])

