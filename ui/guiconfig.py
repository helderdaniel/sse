import pygame

class GUIconfig:
    """
    Gui default configuration, such as:

        Pause key
        Quit event handling

    descendant classes can override methods and class variables 
    to change default behaviour    
    """

    pauseKey = pygame.K_p

    def pause(self, event):
        """
        Predicate that tests if Pause key was pressed
        """
        if event.type == pygame.KEYDOWN:
            if (pygame.key.get_mods() & pygame.KMOD_LCTRL  or  \
                pygame.key.get_mods() & pygame.KMOD_RCTRL) and \
                event.key == self.pauseKey:
                    return True
        return False


    def quit(self, event):
        """
        Predicate that tests if quit event was triggered
        """
        if event.type == pygame.QUIT:
            return True
        return False
