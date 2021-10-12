from __future__ import annotations
from typing import Optional, Tuple
import pygame
from sse.engine.actor import Actor

class Collider:

    def detect(self, actor0:Actor, actor1:Actor) -> Optional[Tuple(int, int)]:
        """
        Predicate to define how collisions are tested
        By default tests with mask
        """
        if actor0.position.z != actor1.position.z:
            #todo. implement actors depth
            return None
        return pygame.sprite.collide_mask(actor0, actor1)
        

    

