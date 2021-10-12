"""
Simple actor animation 

set 2021
hdaniel@ualg.pt
"""
from sse.ui.animation import *
from sse.engine.director import Director
from sse.engine.stage import SimpleStage
from sse.engine.role import *
from sse.engine.actor import Actor
from sse.ui.camera import Camera
from sse.engine.vector import Vector
from sse.engine.bounds import Bounds


imagesPath = ["tests/data/ship0.png", "tests/data/ship1.png", 
              "tests/data/ship0.png", "tests/data/ship2.png"]
background = ["samples/resources/images/background/planetRising.png"]
scrollImage = "samples/resources/images/background/spacerunV.png"
#scrollImage = "samples/resources/images/background/spacerunH.png"
initialPosition0 = Vector(380,300,0)
initialPosition1 = Vector(300,300,0)

#To scroll down, illusion moving up:
#   Init at bottom of image
#   set y-axis speed positive (move backimage down)
#   set y-min (top) bounds == 1 to wrap down when at that y
#   set y-max (bottom) bounds == 16379 to wrap up when at that y
#   Note: must set both y-min and y-max
initialPosition2 = Vector(0,16380,0)  #full height is: 17180
speed2   = Vector(0,1500,0)
bounds2  = Bounds(0,0,1,16379,0,0)


#To scroll image left, illusion moving right:
#   Init at left of image
#   set x-axis speed positive (move backimage left)
#   set x-min (left) bounds == 1 to wrap right when at that x
#   set x-max (bottom) bounds == 16099 to wrap left when at that x
#   Note: must set both x-min and x-max
#initialPosition2 = Vector(0,0,0)  #full height is: 17180
#speed2   = Vector(1500,0,0)
#bounds2  = Bounds(1,16099,0,00,0)


#To scroll image up, illusion moving down:
#   Init at top of image
#   set y-axis speed negative (move backimage up)
#   set y-min (top) bounds == 1 to wrap down when at that y
#   set y-max (bottom) bounds == 16379 to wrap up when at that y
#   Note: must set both y-min and y-max
#initialPosition2 = Vector(0,0,0)  #full height is: 17180
#speed2   = Vector(0,-1500,0)
#bounds2  = Bounds(0,0,1,16380,0,0)

#To scroll image right, illusion moving left:
#   Init at rigth of image
#   set x-axis speed negative (move backimage right)
#   set x-min (left) bounds == 1 to wrap right when at that x
#   set x-max (bottom) bounds == 16099 to wrap left when at that x
#   Note: must set both x-min and x-max
#initialPosition2 = Vector(16100,0,0)  #full height is: 17180
#speed2   = Vector(-1500,0,0)
#bounds2  = Bounds(1,16099,0,00,0)

width    = 1024
height   = 800
speed0   = Vector(-50,20,0)
speed1   = Vector(50,-20,0)
margins  = Bounds(10,10,10,10,0,0)
bounds0  = Bounds(0,width-1,0,height-1,0,0)
fps      = 30
actorFPS = 5


#main
camera   = Camera('Simple actor demo', width, height, fps)

fp0      = FlipBookCircular(imagesPath, resize=(40,40))
role0    = RoleBounceSweep(initialPosition0, speed0, actorFPS, 
                               bounds0, margins, False, 0)
actor0   = Actor([fp0], role0)

fp1      = FlipBookCircular(imagesPath, resize=(40,40))
role1    = RoleBounceSweep(initialPosition1, speed1, actorFPS, 
                               bounds0, margins, False, 0)
actor1   = Actor([fp1], role1)

'''
fp       = FlipBook(background, resize=(width,height))
scenario = Actor([fp])
'''
scroll   = Scroll(scrollImage, (width,height))
role2    = RoleScroll(initialPosition2, speed2, bounds2)
scenario = Actor([scroll], role2)

stage    = SimpleStage(None)
stage.addFoe(actor0)
stage.addFriend(actor1)
stage.addNeutral(scenario)
director = Director(camera, [stage])
director.action()
