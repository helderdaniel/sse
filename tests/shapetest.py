import unittest
import pygame
from pygame.display import init
from sse.ui.shape import *
from sse.ui.gui import GUI


class TestShape(unittest.TestCase):
    
    ui = GUI("Testing", 100, 100)  #needed to initialize Pygame Window
    imagesPath = ["tests/ship0.png", "tests/ship1.png"]
    
    def setImageDefs(self, fname):
        i : Surface = pygame.image.load(fname)
        m : Mask    = pygame.mask.from_surface(i)
        r : Rect    = i.get_rect()
        d : ImageDefinition = ImageDefinition(i, m)
        return i,m,r,d

    def test_ImageDefinition(self):
        i,m,r,d = self.setImageDefs(self.imagesPath[0])

        self.assertIs(i, d.image)
        self.assertIs(m, d.mask)
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

        fp.reset()
        self.assertEqual(1, fp._currentImage)
        fp.next()
        self.assertEqual(0, fp._currentImage)
        fp.next()
        self.assertEqual(1, fp._currentImage)
        fp.set(5)
        self.assertEqual(1, fp._currentImage)
        fp.prev()
        self.assertEqual(0, fp._currentImage)
        fp.prev()
        self.assertEqual(1, fp._currentImage)


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

