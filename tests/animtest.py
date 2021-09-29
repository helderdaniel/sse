import unittest
import pygame
from sse.ui.animation import *
from sse.ui.stage import Stage

class TestAnimation(unittest.TestCase):
    
    stage = Stage("Testing", 100, 100, 0)  #needed to initialize Pygame Window
    imagesPath = ["tests/data/ship0.png", "tests/data/ship1.png", "tests/data/ship2.png"]
    
    def setImageDefs(self, fname, layer=None):
        i : Surface = pygame.image.load(fname)
        m : Mask    = pygame.mask.from_surface(i)
        r : Rect    = i.get_rect()
        if layer is None:
            d : Shape   = Shape(i, m)
        else:
            d : Shape   = Shape(i, m, layer)
        return i,m,r,d

    def test_Shape01(self):
        i,m,r,d = self.setImageDefs(self.imagesPath[0])

        self.assertIs(i, d.image)
        self.assertIs(m, d.mask)
        self.assertEqual(0, d.layer)
        self.assertEqual(r, d.rect)

    def test_Shape02(self):
        l = 4
        i,m,r,d = self.setImageDefs(self.imagesPath[0], l)

        self.assertIs(i, d.image)
        self.assertIs(m, d.mask)
        self.assertEqual(l, d.layer)
        self.assertEqual(r, d.rect)
        

    def test_FlipBook(self):
        #Default args
        fp = FlipBook(self.imagesPath)
        i,m,r,d = self.setImageDefs(self.imagesPath[0])
        self.assertEqual(0, fp._currentImage)
        
        d0 = fp.current()
        self.assertEqual(r.w, d0.rect.w)
        self.assertEqual(r.h, d0.rect.h)

        #Full args
        w = 60
        h = 40
        s = 1
        fp = FlipBook(self.imagesPath, (w, h), s)
        self.assertEqual(s, fp._currentImage)
        self.assertEqual(len(self.imagesPath), fp.size())

        d0 = fp.current()
        self.assertEqual(w, d0.rect.w)
        self.assertEqual(h, d0.rect.h)

        #circular
        fp.reset()
        self.assertEqual(1, fp._currentImage)
        fp.nextc()
        self.assertEqual(2, fp._currentImage)
        fp.nextc()
        self.assertEqual(0, fp._currentImage)
        fp.nextc()
        self.assertEqual(1, fp._currentImage)
        fp.set(4)
        self.assertEqual(1, fp._currentImage)
        fp.prevc()
        self.assertEqual(0, fp._currentImage)
        fp.prevc()
        self.assertEqual(2, fp._currentImage)
        fp.prevc()
        self.assertEqual(1, fp._currentImage)

        #bounded
        fp.reset()
        self.assertEqual(1, fp._currentImage)
        fp.prev()
        self.assertEqual(0, fp._currentImage)
        fp.prev()
        self.assertEqual(0, fp._currentImage)
        fp.next()
        self.assertEqual(1, fp._currentImage)
        fp.next()
        self.assertEqual(2, fp._currentImage)
        fp.next()
        self.assertEqual(2, fp._currentImage)

    def test_Text(self):
        text = Text("Arial", 12, (0,20,0))

        self.assertEqual("", text._text)
        message = "Testing"
        text.set(message)
        self.assertEqual(message, text._text)
        text.reset()
        self.assertEqual("", text._text)



if __name__ == '__main__':
    unittest.main()

