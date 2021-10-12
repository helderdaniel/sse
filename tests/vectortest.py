import math
import unittest
from sse.engine.vector import Vector

class TestVector(unittest.TestCase):
    
    _x=1
    _y=2
    _z=3
    _m=-1
    _s=-0.1

    def test_dim(self):        
        v = Vector(self._x, self._y, self._z)
        self.assertEqual(3, v.dim())

    def test_constructor00(self):
        expected = "(1,2,3)"
        v = Vector(self._x, self._y, self._z)
        self.assertEqual(self._x, v.x)
        self.assertEqual(self._y, v.y)
        self.assertEqual(self._z, v.z)
        self.assertEqual(expected, v.__str__())

    def test_constructor01(self):
        expected = "(-1,-1,-1)"
        v = Vector(self._x, self._y, self._z)
        v.x = self._m
        self.assertEqual(self._m, v.x)
        v.y = self._m
        self.assertEqual(self._m, v.y)
        v.z = self._m
        self.assertEqual(self._m, v.z)
        self.assertEqual(expected, v.__str__())       

    def test_constructor02(self):
        expected = "(3,1,2)"
        v = Vector(self._x, self._y, self._z)
        v.data[0] = self._z
        v.data[1] = self._x
        v.data[2] = self._y
        self.assertEqual(self._z, v.data[0])
        self.assertEqual(self._x, v.data[1])
        self.assertEqual(self._y, v.data[2])
        self.assertEqual(expected, v.__str__())

    def test_copy(self):
        expected = "(1,2,3)"
        v0 = Vector(self._x, self._y, self._z)
        v1 = v0.copy()
        self.assertEqual(expected, v0.__str__())         
        self.assertEqual(expected, v1.__str__())         

    def test_add_scalar(self):
        expectedv = "(1,2,3)"
        expectedr = "(0.9,1.9,2.9)"
        v = Vector(self._x, self._y, self._z)
        r = v.add(self._s)
        self.assertEqual(expectedv, v.__str__())
        self.assertEqual(expectedr, r.__str__())

    def test_add_vector(self):
        expectedv0 = "(1,2,3)"
        expectedv1 = "(-1,-1,-1)"
        expectedr  = "(0,1,2)"
        v0 = Vector(self._x, self._y, self._z)
        v1 = Vector(self._m, self._m, self._m)
        r = v0.add(v1)
        self.assertEqual(expectedv0, v0.__str__())
        self.assertEqual(expectedv1, v1.__str__())
        self.assertEqual(expectedr,  r.__str__())

    def test_scalar_product(self):
        expectedv = "(1,2,3)"
        expectedr = "(-1,-2,-3)"
        v = Vector(self._x, self._y, self._z)
        r = v.scalarProduct(self._m)
        self.assertEqual(expectedv, v.__str__())
        self.assertEqual(expectedr, r.__str__())        

    def test_dot_product(self):
        expectedv0 = "(1,2,3)"
        expectedv1 = "(-1,-1,-1)"
        expectedr  = -6
        v0 = Vector(self._x, self._y, self._z)
        v1 = Vector(self._m, self._m, self._m)
        r = v0.dotProduct(v1)
        self.assertEqual(expectedv0, v0.__str__())
        self.assertEqual(expectedv1, v1.__str__())
        self.assertEqual(expectedr,  r)

    def test_move(self):
        expected = "(0,1,2)"
        v = Vector(self._x, self._y, self._z)
        v.move(self._m, self._m, self._m)
        self.assertEqual(expected, v.__str__())

    def test_length(self):
        expected = math.sqrt(self._x**2 + self._y**2 + self._z**2)
        v = Vector(self._x, self._y, self._z)
        r = v.length()
        self.assertEqual(expected, r)
    


if __name__ == '__main__':
    unittest.main()

