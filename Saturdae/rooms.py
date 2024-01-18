import turtle as t
import numpy as np
from furniture import *
from check import *
from delete import *


# function to draw the room
def room (x, y, length, width, c):
    if c == 1:
        t.color('white')
    elif c == 2:
        t.color('green')
    else:
        t.color('black')
    length = length * 10
    width = width * 10
    t.speed(10)
    t.pensize(2)
    t.up()
    t.home()
    t.setx(x)
    t.sety(y)
    t.down()
    t.color('blue')
    t.forward(10)
    t.color('black')
    t.forward(length - 20)
    t.color('blue')
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.color('black')
    t.forward(width - 20)
    t.color('blue')
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.color('black')
    t.forward(length - 20)
    t.color('blue')
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.color('black')
    t.forward(width - 20)
    t.color('blue')
    t.forward(10)
    t.up()
    t.forward(3)
    t.right(90)
    t.forward(3)
    t.left(180)
    t.down()
    t.color('blue')
    t.forward(13)
    t.color('black')
    t.forward(length - 20)
    t.color('blue')
    t.forward(13)
    t.left(90)
    t.forward(13)
    t.color('black')
    t.forward(width - 20)
    t.color('blue')
    t.forward(13)
    t.left(90)
    t.forward(13)
    t.color('black')
    t.forward(length - 20)
    t.color('blue')
    t.forward(13)
    t.left(90)
    t.forward(13)
    t.color('black')
    t.forward(width - 20)
    t.color('blue')
    t.forward(13)
    t.hideturtle()


# function to draw floor
def floor(x, y):
    x = x * 10
    y = y * 10
    t.pensize(2)
    t.setx(0)
    t.sety(0)
    t.speed(10)
    t.color('blue')
    t.forward(10)
    t.color('black')
    t.forward(x - 20)
    t.color('blue')
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.color('black')
    t.forward(y - 20)
    t.color('blue')
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.color('black')
    t.forward(x - 20)
    t.color('blue')
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.color('black')
    t.forward(y -20)
    t.color('blue')
    t.forward(10)
    t.up()
    t.forward(3)
    t.right(90)
    t.forward(3)
    t.left(180)
    t.down()
    t.forward(13)
    t.color('black')
    t.forward(x - 20)
    t.color('blue')
    t.forward(13)
    t.left(90)
    t.forward(13)
    t.color('black')
    t.forward(y - 20)
    t.color('blue')
    t.forward(13)
    t.left(90)
    t.forward(13)
    t.color('black')
    t.forward(x - 20)
    t.color('blue')
    t.forward(13)
    t.left(90)
    t.forward(13)
    t.color('black')
    t.forward(y - 20)
    t.color('blue')
    t.forward(13)
    t.up()
    t.hideturtle()
    

# function to check if the room clashes with anyother room or object and map it
def checkobj(x, y, length, width, rooms, arr):
    # here x = object start x
    # y = object start y
    # length = length of the object
    # width = width of the object
    if (x + width * 10 > 300 or y + length * 10 > 300):
        return False
    elif (x < -2 or y < -2):
        return False
    length = length * 2
    width = width * 2
    b = x // 5
    a = (y // 5) * -1 -1
    
    if (np.sum(rooms[a:a - length + 1:-1, b:b + width - 1]) == 0):
        if (np.sum(arr[a:a - length:-1, b]) == 0 and np.sum(arr[b:b + width, a]) == 0 and 
            np.sum(arr[a:a - length :-1, b + width - 1]) == 0 and np.sum(arr[b:b + width, a + length]) == 0):
            rooms[a:a - length + 1:-1, b] = 1
            rooms[a, b:b + width - 1: 1] = 1
            rooms[a:a - length + 1:-1, b + width - 1] = 1
            rooms[a - length + 1, b:b + width: 1] = 1
            return True
    else:
        print("not a valid position for the room")


# function to check the if an object is clashing with a room or not
def checkroom (x, y, length, width, room_details):
    print(room_details)
    if (len(room_details) == 0):
        return True
    start_x, start_y, room_length, room_width = findroom(x, y, room_details)
    room_length = room_length * 10
    room_width = room_width * 10
    if (start_x == 0 and start_y == 0 and room_length == 0 and room_width == 0):
        return True
    print(x, y, start_x, start_y, length, width, room_length, room_width)
    if ((x + width) <= (start_x + room_width)) and ((y + length) <= (start_y + room_length)):
        return False
    else:
        return True


# function to find the room that matches the specifications
def findroom(x, y, room_details):
    # x = start x of the object
    # y = start y of the object
    for i in room_details: 
        if x >= i[0] and y >=  i[1] and x <= (i[0] + i[2] * 10) and y <= (i[1] + i[3] * 10):
            return i[0], i[1], i[2], i[3]
            # here i[0] = x position of the room
            # i[1] = y position of the room
            # i[2] = length of the room
            # i[3] = width of the room
    return 0, 0, 0, 0


# function the delete the room    
def delete_room(x, y, rooms, room_details):
    flag = 0
    for i in room_details:
        if (i[0] == x and i[1] == y):
            b = i[0] // 5 + 1
            a = (i[1] // 5) * -1 
            rooms[a:a - i[2] // 5:-1, b:b + i[3] // 5] = 0
            room(x, y, i[2], i[3], 1)
            room_details.pop(flag)
            print("removed room successfully...")
            break
        flag = flag + 1


# function to check if the window position is correct
def window_pos(x, y, z, rooms):
    b = x // 5 - 1
    a = (y // 5) * -1 - 1
    
    for i in range(60):
        for j in range(60):
            print(rooms[i,j], end=' ')
        print("")
        
    if rooms[a, b] == 1  and (rooms[a+8, b] == 1 or rooms[a-8, b] == 1 or rooms[a, b+8] == 1 or rooms[a, b-8] == 1):
        window(x, y, z, 2)
        flag = int(input("is this position okay (1/0) : "))
        if flag:
            return True
        else:
            for i in range(6):
                t.undo()
            return False
    else:
        print("not a valid position for the window")
        return False