from rooms import *
import numpy as np
import turtle as t
from furniture import *

# get size of the object
def get_size(a):
    if(a == 'bed'):
        return 42
    elif(a == 'sofa'):
        return 18
    elif(a == 'table'):
        return 42
    elif(a == 'sbed'):
        return 18

# recommendation for the size of the object
def size_recommendation (object, x, y, z, room_details, arr, rooms):
    # x,y,z is the x y coordinates and the angle of the object
    object_size = get_size(object)
    #get room coordinates
    start_x, start_y, room_length, room_width = findroom(x, y, room_details)
    if(object_size > room_length * room_width * 0.4):
        print("object too large for the room ")
        flag = int(input("1. just leave it 2. remove it 3. show recommendations"))
        if(flag == 1):
           return False
        elif(flag == 2):
            if(object == 'bed'):
                bed(x, y, z, 1)
            elif(object == 'sbed'):
               singlebed(x, y, z, 1)
            elif(object == 'sofa'):
               sofa(x, y, z, 1)
            elif(object == 'table'):
                table(x, y, z, 1)
            else:
                print("invalid choice")
            return False
        elif(flag == 3):
            if(object == 'table' or object == 'sbed'  or object == 'sofa'):
                print("sorry no recommendation developed yet")
                return False
            bed(x, y, z, 1)
            singlebed(x, y, z, 2)
            ask = int(input("is this recommendation okay (1/0)? "))
            if(ask == 1):
                new_x, new_y, new_z = position_recommendation(x, y, z)
                singlebed(new_x, new_y, new_z, 3)
                return True
            else:
                singlebed(x, y, z, 1)
                bed(x, y, z, 3)
                return False
            
        else:
            print("invalid flag")
            return       

def position_recommendation(object, x, y, z, rooms, room_details):
    print("position_recommendation")
    door_x, door_y = find_door(rooms, x, y, z, room_details)
    if(object == 'bed'):
        if(y > door_y ):
            door_position = 'down'
        elif(y < door_y):
            door_position = 'up'
        elif(x < door_x):
            door_position = 'right'
        elif(x > door_x):
            door_position = 'left'
    else:
        print("recommendation system not yet developed")
        
    if(door_position == 'up'):
        wall_x, wall_y = walls_position(x, y, room_details, rooms, 1, 1)
        obj_x = wall_x - 1
        obj_y = wall_y + 1
        obj_z = 180
    elif(door_position =='right'):
        wall_x, wall_y = walls_position(x, y, room_details, rooms, 1, -1)
        obj_x = wall_x + 1
        obj_y = wall_y + 1
        obj_z = 270
    elif(door_position =='left'):
        wall_x, wall_y = walls_position(x, y, room_details, rooms, -1, 1)
        obj_x = wall_x - 1
        obj_y = wall_y - 1
        obj_z = 90
    elif(door_position =='down'):
        wall_x, wall_y = walls_position(x, y, room_details, rooms, -1, -1)
        obj_x = wall_x + 1
        obj_y = wall_y - 1
        obj_z = 0
        
       
    return obj_x, obj_y, obj_z

def find_door(rooms, x, y, z, room_details):
    start_x, start_y, room_length, room_width = findroom(x, y, room_details)
    b = start_x // 5
    a = (start_y // 5) * -1 - 1
    
    for i in range(room_length):
        if(rooms[a, b+i] == 2):
            return (a * -5 + 1), b*5 + 2
        elif(rooms[a-i,b] == 2):
            return (a * -5 + 3), b*5

def walls_position(x, y, room_details, rooms, xi, yi):
    start_x, start_y, room_length, room_width = findroom(x, y, room_details)
    b = x // 5
    a = (y // 5) * -1 - 1
    for i in range(start_x - x):
        if(rooms[a+xi,b] == 1):
            wall_y = (a - i) * -5 + 1
            break
    for i in range(start_y - y):
        if(rooms[a,b+yi] == i):
            wall_x = b * 5
            break
    return wall_x, wall_y