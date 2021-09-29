import unittest

import pygame
from sse.ui.stage import Stage

class TestGUI(unittest.TestCase):     
    
    def test_gui(self):
        name  = "Testing"
        w = 100
        h = 200
        ui = Stage(name, w, h)
        r = ui._screen.get_rect()
        self.assertEqual(w, r.w)
        self.assertEqual(h, r.h)
        t = pygame.display.get_caption()[0]
        self.assertEqual(name, t)

if __name__ == '__main__':
    unittest.main()

