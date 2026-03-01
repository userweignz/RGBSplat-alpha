from ursina import * 
from ursina.prefabs.first_person_controller import *
import math
from random import randint

box_color = 'red'

app = Ursina()

    
ai_enabled = True
    
bullets = []
splats = []
npcs = []

redboxes = []
greenboxes = []
blueboxes = []


score = 0
score_str = str(score)
player = FirstPersonController()
player.fov = 90
player.speed = 10
target_speed = 0

velocity = Vec3(0,0,0)
acceleration = 20
friction = 8

Sky()

ai_timer = 0
box_timer = 0

mouse.locked = True
mouse.visible = False


current_weapon = 2
life = 100
red_am = 10; green_am = 10; blue_am = 10

walk_bob_amount = 0.05 
walk_bob_speed = 16    
walk_bob_timer = 0

default_cam_y = player.camera_pivot.y

player.jump_height = 2      
player.jump_duration = 0    
player.gravity = 0.98

npc_speed = 5