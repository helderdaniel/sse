"""
Simple actor animation 

set 2021
hdaniel@ualg.pt
"""
from sse.ui.stage import Stage
from sse.ui.animation import FlipBook
from sse.engine.act import Act
from sse.engine.scene import SimpleScene
from sse.engine.role import Role
from sse.engine.actor import Actor


imagesPath = ["tests/data/ship0.png", "tests/data/ship1.png", "tests/data/ship2.png"]
initialPosition = [350,300]
width  = 800
height = 600
speed  = [1,1,1,1]
bounds = [0,height-1,0,width-1]
fps    = 30

#main
stage = Stage('Simple actor demo', width, height, fps)
fp    = FlipBook(imagesPath)
role  = Role(initialPosition, speed, bounds, False, 0)
actor = Actor([fp], role)
scene = SimpleScene(stage)
scene.addFoe(actor)
act   = Act([scene])
act.play()
