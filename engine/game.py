"""
Game functions as a service

User interfaces can run game methods to et info to be displayed

User interfaces must send user commands to game(eg.: pygame.events)

Collisions is detected outside the Game and must also be passed to the game



update(events, collisions)
    
    events
        user input
        system

    collisions: List of sprites that collided


    1) handle collisions
            update status of collided entity controller to: HIT or DEAD
    
    2) update entity controllers positions (move)
    
    3) update groups of sprites


"""