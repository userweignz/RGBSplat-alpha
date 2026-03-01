from ursina import * 
from ursina.prefabs.first_person_controller import *
import math
from random import randint
from world_setgs import *

def create_npc(npc_position, npctype):
    npc = Entity(position=npc_position)
    
    
    npc.body = Entity(
        model='models/body.obj',
        parent=npc,
        collider=None,
        )
    
    npc.face = Entity(  
        model='models/face.obj',
        parent=npc,
        
        color=color.black
    )
    
    if npctype == 'red':
        npc.body.color = color.red
    if npctype == 'green':
        npc.body.color = color.green
    if npctype == 'blue':
        npc.body.color = color.blue
    
    npc.type = npctype
    npc.damage_timer = 0
    
    return npc

  
def create_bullet(clr):
    bullet = Entity(
        model='sphere',
        collider='sphere',
        position=camera.world_position + camera.forward + Vec3(0.74,-0.4,0)
        )
    
    if clr == 1:
        bullet.color = color.red
    if clr == 2:
        bullet.color = color.green
    if clr == 3:
        bullet.color = color.blue
    
    bullet.direction = camera.forward
    bullets.append(bullet)
    
def create_bb(pos, clr):
    box = Entity(position=pos, scale=0.6, collider='box')
    box_ud = Entity(
        model='models/box_ud.obj',
        double_sided=True,
        parent=box)
    box_s = Entity(
        model='models/box_s.obj',
        double_sided=True,
        parent=box)
    
    if clr == 1:
        box_ud.texture = 'textures/redbud.png'
        box_s.texture = 'textures/redbs.png'
        redboxes.append(box)
    elif clr == 2:
        box_ud.texture = 'textures/greenbud.png'
        box_s.texture = 'textures/greenbs.png'
        greenboxes.append(box)
    elif clr == 3:
        box_ud.texture = 'textures/bluebud.png'
        box_s.texture = 'textures/bluebs.png'
        blueboxes.append(box)
    