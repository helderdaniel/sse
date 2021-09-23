import unittest

class Test_some(unittest.TestCase):

    def test_inc_01(self):
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
