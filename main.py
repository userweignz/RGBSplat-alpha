from ursina import * 
from ursina.prefabs.first_person_controller import *
import math
from random import randint, choice
from world_setgs import *
from logic import *
from world_ents import *


def update():
 
    global walk_bob_timer
    global velocity_y
    global ai_timer
    global box_timer
    global ai_life_timer
    global score
    global target_speed
    global velocity
    global box_color
    global life
    
    
    allboxes = redboxes + greenboxes + blueboxes
    
    ai_timer += time.dt
    box_timer += time.dt
    ai_interval = 4.0
    box_interval = 5.0
    
    if ai_timer >= ai_interval and ai_enabled:
        npc = create_npc((randint(-10,10),1,randint(-10,10)), choice(['red','green','blue']))
        npcs.append(npc)
        ai_timer = 0
        
    if box_timer >= box_interval:
        create_bb((randint(-10,10),1.5,randint(-10,10)), choice([1,2,3]))
        box_timer = 0
        
    desired_distance = 3

    scoretext.text = str(score)
    
    redtext.text = str(red_am)
    greentext.text = str(green_am)
    bluetext.text = str(blue_am)
    
    lifetext.text = str(life)
    
    camera_direction = camera.forward
    
    for gun in guns:
        hit_info = raycast(camera.world_position, camera_direction, distance=desired_distance, ignore=[camera, gun])
        if hit_info.hit:
            gun.world_position = hit_info.world_point - camera_direction*0.1
        else:
            gun.world_position = camera.world_position + camera_direction*desired_distance
        
   

    for npc in npcs:
        
        direction = player.position - npc.position
        direction.y = 0  
        rotation_speed = 1
        
        
        distance_to_player = distance(npc.position, player.position)
        target_angle = math.degrees(math.atan2(direction.x, direction.z)) - 180
        
        if ai_enabled:     
            if distance_to_player > 1.5:
                direction = (player.position - npc.position).normalized()
                npc.position += direction * npc_speed * 0.02
                npc.damage_timer = 0
                
                npc.rotation_y = lerp_angle(
                     npc.rotation_y,
                     target_angle,
                     2 * time.dt
                    )
                npc.face.rotation_y = lerp_angle(
                     npc.face.rotation_y,
                     0,
                     100 * time.dt
                    )
            else:     
                npc.damage_timer += time.dt

                if npc.damage_timer >= 0.5:
                    life -= 2
                    npc.damage_timer -= 1
                    
                   
                 
                
                 
    hovered_box = None

    for box in allboxes:
        box.rotation_y += time.dt * 30
        
        if box.hovered:
            hovered_box = box
            break
        
    if hovered_box:
        if hovered_box in redboxes:
            box_color = 'red'
        elif hovered_box in greenboxes:
            box_color = 'green'
        elif hovered_box in blueboxes:
            box_color = 'blue'
        pickuptext.text = f"Press E to pick up the {box_color} box"
        pickuptext.visible = True
    else:
        pickuptext.visible = False
        
        
    ahb = any(box.hovered for box in allboxes)       
    pickuptext.visible = ahb
    
    pickuptext.text = f"Press E to pickup {box_color} box."
    
    bullet_speed = 100
    
    for bullet in bullets[:]:
        bullet.position += bullet.direction * bullet_speed * time.dt
    
        hit_info = raycast(bullet.position - bullet.direction * bullet_speed * time.dt,
                           bullet.direction,
                           distance=bullet_speed * time.dt,
                           ignore=[bullet])
        
    
        if hit_info.hit:
            hit_entity = hit_info.entity

            hit_npc = None
            wrong_npc = None
            
            for npc in npcs:
                if hit_entity in (npc.face, npc.body):
                    if ((npc.type == 'red' and current_weapon == 1) or
                        (npc.type == 'green' and current_weapon == 2) or
                        (npc.type == 'blue' and current_weapon == 3)):
                        hit_npc = npc
                    
                    else:
                        wrong_npc = npc
                    
                    break
                                     
            if hit_npc:   
                destroy(hit_npc)
                npcs.remove(hit_npc)                  
                bullet.disable()
                bullets.remove(bullet)
                destroy(bullet)
                score += 1
                
                
            elif wrong_npc:
                clone = create_npc(
                wrong_npc.position + Vec3(3,0,0),
                wrong_npc.type
                    )

                npcs.append(clone)
                bullet.disable()
                bullets.remove(bullet)
                destroy(bullet)
         
                
            else:
                decal = Entity(
                    model='plane',
                    texture='textures/splat.png',
                    double_sided=True,
                    scale=(3,3,3),
                    position=hit_info.world_point + hit_info.normal * 0.01
                    )
                
                if bullet.color == color.red:
                    decal.color = color.red
                elif bullet.color == color.green:
                    decal.color = color.green
                elif bullet.color == color.blue:
                    decal.color = color.blue
                    
                    
                decal.look_at(decal.position + hit_info.normal, 'up') 
                splats.append(decal)
                bullet.disable()
                bullets.remove(bullet)
                destroy(bullet)
        

    if len(splats) > 10:
        old_decal = splats.pop(0)
        destroy(old_decal)
        
    if life <= 0:
        print('you lose. score: ', score)
        application.quit()
        
        
            
        
    direction = Vec3(
        held_keys['d'] - held_keys['a'],
        0,
        held_keys['w'] - held_keys['s']
    )

    if direction.length() > 0:
        direction = (player.forward * direction.z + player.right * direction.x).normalized()

        if held_keys['shift']:
            target_speed = 15
        else:
            target_speed = 7

        velocity = lerp(velocity, direction * target_speed, acceleration * time.dt)
        walk_bob_timer += time.dt * walk_bob_speed * 1.5
        player.camera_pivot.y = default_cam_y + math.sin(walk_bob_timer) * walk_bob_amount

    else:
        velocity = lerp(velocity, Vec3(0,0,0), friction * time.dt)
        
    
    player.direction = velocity.normalized() if velocity.length() > 0.01 else Vec3(0,0,0)
    player.speed = velocity.length()

    
        
        
def input(key):
    global red_am, green_am, blue_am
    global current_weapon
    
    if key == 'left mouse down':
        if current_weapon == 1 and red_am > 0:
            create_bullet(1)
            red_am -= 1
        elif current_weapon == 2 and green_am > 0:
            create_bullet(2)
            green_am -= 1
        elif current_weapon == 3 and blue_am > 0:
            create_bullet(3)
            blue_am -= 1
    if key == 'e':      
        allboxes = redboxes + greenboxes + blueboxes
        
        for box in allboxes: 
            if box.hovered:      
                pickuptext.visible
                destroy(box)
                if box in redboxes:
                    box_color = 'red'
                    redboxes.remove(box)
                    red_am += 1
                elif box in greenboxes:
                    box_color = 'green'
                    greenboxes.remove(box)
                    green_am += 1
                elif box in blueboxes:
                    box_color = 'blue'
                    blueboxes.remove(box)
                    blue_am += 1
    if key == '1':
        current_weapon = 1
        redgun.visible = True
        greengun.visible = False
        bluegun.visible = False
        
    elif key == '2':
        current_weapon = 2
        redgun.visible = False
        greengun.visible = True
        bluegun.visible = False
    elif key == '3':
        current_weapon = 3
        redgun.visible = False
        greengun.visible = False
        bluegun.visible = True
        
        
app.run()
