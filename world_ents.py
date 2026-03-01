from ursina import * 
from world_setgs import *



scoreui = Entity(
    model='quad',              
    texture='textures/sb.png',
    parent=camera.ui,
    scale=(0.3,0.2),               
    position=(-0.74, 0.4, 0)         
)

lrgbui = Entity(
    model='quad',              
    texture='textures/lrgb.png',
    parent=camera.ui,
    scale=(0.5,0.2),               
    position=(-0.64, -0.4, 0)         
)


scoretext = Text(str(score), position=(-0.85, 0.45), scale=5, color=color.red)

redtext = Text(str(red_am), position=(-0.45, -0.37), scale=1, color=color.red)  
greentext = Text(str(green_am), position=(-0.45, -0.41), scale=1, color=color.green)  
bluetext = Text(str(blue_am), position=(-0.45, -0.47), scale=1, color=color.blue)

lifetext = Text(life, position=(-0.45, -0.33))
pickuptext = Text(f"Press E to pickup {box_color} box.", visible=False)

dbgtext = Text("", position=(-0.5,-0.5))

room1f = Entity(
    model='models/room1floor.obj',
    texture='textures/floor.png',
    texture_scale=(10, 6),
    double_sided=True,
    scale=2,
    z=3,
    color=color.white,
    collider='mesh'
)
  
ground = Entity(
    model='models/room1walls.obj',
    texture='textures/wall.png',
    texture_scale=(4, 1),
    double_sided=True,
    scale=2,
    z=3,
    color=color.white,
    collider='mesh'
)



redgun = Entity(parent=player, rotation_y=-100, visible=False)

rg_main = Entity(
    model='models/redgun_main.obj',
    color=color.gray,
    parent=redgun,
    scale=(0.1, 0.1, 0.1),
    position=(-1.4,-0.2,-0.5)
)
rg_barrel = Entity(
    model='models/redgun_barrel.obj',
    color=color.white,
    parent=redgun,
    scale=(0.1, 0.1, 0.1),
    position=(-1.4,-0.2,-0.5)
)
rg_paint = Entity(
    model='models/redgun_paint.obj',
    color=color.red,
    parent=redgun,
    scale=(0.1, 0.1, 0.1),
    position=(-1.4,-0.2,-0.5)
)

greengun = Entity(parent=player, scale=(0.1,0.1,0.1), rotation_y=-10)

gg_main = Entity(
    model='models/greengun_main.obj',
    color=color.gray,
    parent=greengun,
    position=(2.5,-0.2,-17.5)
)
gg_barrel = Entity(
    model='models/greengun_barrel.obj',
    color=color.white,
    parent=greengun,
    position=(2.5,-0.2,-17.5)
)
gg_paint = Entity(
    model='models/greengun_paint.obj',
    color=color.green,
    parent=greengun,
    position=(2.5,-0.2,-17.5)
)

bluegun = Entity(parent=player, scale=(0.11,0.11,0.11), rotation_y=-10, visible=False)

bg_main = Entity(
    model='models/bluegun_main.obj',
    color=color.gray,
    parent=bluegun,
    position=(2.5,-0.2,-17.5)
)
bg_barrel = Entity(
    model='models/bluegun_barrel.obj',
    color=color.white,
    parent=bluegun,
    position=(2.5,-0.2,-17.5)
)
bg_paint = Entity(
    model='models/bluegun_paint.obj',
    color=color.blue,
    parent=bluegun,
    position=(2.5,-0.2,-17.5)
)

guns = [redgun, greengun, bluegun]
