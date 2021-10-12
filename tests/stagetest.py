import unittest

import pygame
from sse.engine.stage import Stage

class TestStage(unittest.TestCase):
    
    def test_stage(self):
        name  = "Testing"
        w = 100
        h = 200
        stage = Stage(name, w, h,0)
        r = stage._screen.get_rect()
        self.assertEqual(w, r.w)
        self.assertEqual(h, r.h)
        t = pygame.display.get_caption()[0]
        self.assertEqual(name, t)

if __name__ == '__main__':
    unittest.main()

