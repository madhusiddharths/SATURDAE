import turtle as t
from furniture import *
from check import *
from delete import *
from rooms import *
from room_recommend import *
import numpy as np


def drawGraph():
    t.setx(0)
    t.sety(0)
    t.forward(310)
    t.setx(0)
    t.sety(0)
    t.left(90)
    t.forward(310)
    for i in range(30):
        t.up()
        t.sety(-10)
        t.setx(10 * (i + 1))
        t.down()
        if i % 2 == 0:
            t.write(" ")
        else:
            t.write(i + 1, font=("Verdana", 6, 'bold'))

    for i in range(30):
        t.up()
        t.setx(-10)
        t.sety(10 * (i + 1))
        t.down()
        if i % 2 == 0:
            t.write(" ")
        else:
            t.write(i + 1, font=("Verdana", 6, 'bold'))

    t.up()
    t.setpos(0, -10)
    t.down()
    t.write(0, font=("Verdana", 6, 'bold'))


# to initialize the turtle workspace (30 x 30)
def initializeturtle():
    t.clear()
    t.setworldcoordinates(-30, -30, 320, 320)
    t.speed(10)
    t.bgcolor('white')
    t.color('black')
    drawGraph()
    t.home()
    floor(30, 30)

# main function
# arr - main array where object is mapped
# object - array containing details of placed objects
# count - array containing number of objects [bed, sofa, window, door, table, tv, sbed, stable]


def saturdae(arr, object, count, rooms, room_details, room_count):
    while True:
        # get user input
        print("1.bed 2.sofa 3.window 4.door 5.table 6.tv 7.singlebed 8.sidetable 9.remove object 10.room 11.delete room")
        d = int(input("enter your choice : "))
        
        # save
        if d==12:
            canvas = t.getcanvas()
            psFilename = "diagram.eps"
            canvas.postscript(file=psFilename)
            filename = input("enter file name : ")
            filename = filename + ".png"
            psimage = Image.open(psFilename)
            psimage.save(filename)
            os.remove(psFilename)
            
        # delete room
        if d == 11:
            x = int(input("enter x position : "))
            y = int(input("enter y position :"))
            x = x * 10
            y = y * 10
            delete_room(x, y, rooms, room_details)
             
        # rooms
        elif d == 10:
            length = int(input("enter room length : "))
            width = int(input("enter room width : "))
            x = int(input("enter x position : "))
            y = int(input("enter y position :"))
            x = x * 10
            y = y * 10
            if check_room_clash(x, y, width, length, rooms):
                room(x, y, length, width, 3)
                old_x, old_y, new_x, new_y, flag = recommend_room(x, y, length, width, rooms)
                if flag == 0:
                    room(x, y, length, width, 3)
                else:
                    room(new_x, new_y, length, width, 3)
                    for i in room_details:
                        room(i[0], i[1], i[2], i[3], 3)
                x = new_x
                y = new_y
                b = x // 5
                a = (y // 5) * -1 - 1
                rooms[a:a - length * 2:-1, b:b + width * 2] = 1
                name = input("enter the room name : ")
                t.setx(new_x + 5)
                t.sety(new_y + 5)
                room_details.append([new_x, new_y, length, width, name])
                t.write(name, font=("Verdana", 10, "normal"))
  
        # remove an object
        elif d == 9:
            a = input('enter object name :')
            if remove(a, arr, object, room_details):
                # returns true or false
                print("successfully removed")
            else:
                print("no such object found")
        
        elif d == 9:
            a = input('enter object name :')
            if remove(a, arr, object, room_details):
                # returns true or false
                print("successfully removed")
            else:
                print("no such object found")
            floor(30, 30, 0)


        # add object   
        elif (d < 9) and (d >= 0):
            x = int(input("enter x position : "))
            y = int(input("enter y position : "))
            z = int(input("enter the angle : "))
            x = x * 10
            y = y * 10

            # toilet
            if d == 0:
                bathroom(x, y, z)

            # bed
            elif d == 1:
                # to check if object is placed on room wall
                if z == 0:
                    if checkroom(x, y, 70, 60, room_details):
                        print("object outside room or object outside room or clashing with room...")
                        continue
                # changing values according to usecase as object rotates abuot a point only
                elif z == 90:
                    if checkroom(x, y, 60, 70, room_details):
                        print("object outside room or object outside room or clashing with room...")
                        continue
                    y = y + 60
                elif z == 180:
                    if checkroom(x, y, 70, 60, room_details):
                        print("object outside room or object outside room or clashing with room...")
                        continue
                    x = x + 60
                    y = y + 70
                elif z == 270:
                    if checkroom(x, y, 60, 70, room_details):
                        print("object outside room or object outside room or clashing with room...")
                        continue
                    x = x + 70

                # check if the space is occupied 
                if checkbed(x, y, z, arr, 1):
                    # x, y are coordinates, z is angle, 1 is fill value (0 is remove value)
                    add(x, y, z, 'bed', object, count)
                    # bed is object name will be concatenated with corresponding number in count
                    bed(x, y, z, 3)
                    # confirm object 3 - black colour
                else:
                    print("space occupied or object cancelled...")

            # sofa
            elif d == 2:
                if z == 0:
                    if checkroom(x, y, 20, 60, room_details):
                        print("object outside room or clashing with room...")
                        continue
                    x = x + 5
                elif z == 90:
                    if checkroom(x, y, 60, 20, room_details):
                        print("object outside room or clashing with room...")
                        continue
                    y = y + 55
                elif z == 180:
                    if checkroom(x, y, 20, 60, room_details):
                        print("object outside room or clashing with room...")
                        continue
                    x = x + 55
                    y = y + 30
                elif z == 270:
                    if checkroom(x, y, 60, 20, room_details):
                        print("object outside room or clashing with room...")
                        continue
                    x = x + 30
                    y = y + 5
                if checksofa(x, y, z, arr, 1):
                    add(x, y, z, 'sofa', object, count)
                    sofa(x, y, z, 3)
                else:
                    print("space occupied or object cancelled...")

            # window        
            elif d == 3:
                if window_pos(x, y, z, rooms):
                    add(x, y, z, 'window', object, count)
                    window(x, y, z, 3)

            # door
            elif d == 4:
                if checkdoor(x, y, z, arr, 1):
                    add(x, y, z, 'door', object, count)
                    door(x, y, z, 3)
                    temp = hall_recommend(x, y, rooms, room_details)
                    if temp:
                        print("room added successfully")
                    else:
                        print("rooms cleared...")
                else:
                    print("space occupied or object cancelled...")

            # table
            elif d == 5:
                if z == 0:
                    if checkroom(x, y, 60, 70, room_details):
                        print("object outside room or clashing with room...")
                        continue
                elif z == 90:
                    if checkroom(x, y, 70, 60, room_details):
                        print("object outside room or clashing with room...")
                        continue
                    y = y + 70
                elif z == 180:
                    if checkroom(x, y, 60, 70, room_details):
                        print("object outside room or clashing with room...")
                        continue
                    x = x + 70
                    y = y + 60
                elif z == 270:
                    if checkroom(x, y, 70, 60, room_details):
                        print("object outside room or clashing with room...")
                        continue
                    x = x + 60
                if checktable(x, y, z, arr, 1):
                    add(x, y, z, 'table', object, count)
                    table(x, y, z, 3)
                else:
                    print("space occupied or object cancelled...")

            # tv     
            elif d == 6:
                if z == 0:
                    if checkroom(x, y, 15, 45, room_details):
                        print("object outside room or clashing with room...")
                        continue
                elif z == 90:
                    if checkroom(x, y, 45, 15, room_details):
                        print("object outside room or clashing with room...")
                        continue
                    y = y + 50
                elif z == 180:
                    if checkroom(x, y, 15, 45, room_details):
                        print("object outside room or clashing with room...")
                        continue
                    x = x + 50
                    y = y + 10
                elif z == 270:
                    if checkroom(x, y, 45, 15, room_details):
                        print("object outside room or clashing with room...")
                        continue
                    x = x + 10
                if checktv(x, y, z, arr, 1):
                    add(x, y, z, 'tv', object, count)
                    tv(x, y, z, 3)
                else:
                    print("space occupied or object cancelled...")

            # single bed
            elif d == 7:
                if z == 0:
                    if checkroom(x, y, 60, 30, room_details):
                        print("object outside room or clashing with room...")
                        continue
                elif z == 90:
                    if checkroom(x, y, 30, 60, room_details):
                        print("object outside room or clashing with room...")
                        continue
                    y = y + 30
                elif z == 180:
                    if checkroom(x, y, 60, 30, room_details):
                        print("object outside room or clashing with room...")
                        continue
                    x = x + 30
                    y = y + 60
                elif z == 270:
                    if checkroom(x, y, 30, 60, room_details):
                        print("object outside room or clashing with room...")
                        continue
                    x = x + 60
                if checksinglebed(x, y, z, arr, 1):
                    add(x, y, z, 'sbed', object, count)
                    singlebed(x, y, z, 3)
                else:
                    print("space occupied or object cancelled...")

            # sidetable
            elif d == 8:
                if z == 0:
                    if checkroom(x, y, 20, 25, room_details):
                        print("object outside room or clashing with room...")
                        continue
                elif z == 90:
                    if checkroom(x, y, 25, 20, room_details):
                        print("object outside room or clashing with room...")
                        continue
                    y = y + 25
                elif z == 180:
                    if checkroom(x, y, 20, 25, room_details):
                        print("object outside room or clashing with room...")
                        continue
                    x = x + 25
                    y = y + 20
                elif z == 270:
                    if checkroom(x, y, 25, 20, room_details):
                        print("object outside room or clashing with room...")
                        continue
                    x = x + 20
                if checksidetable(x, y, z, arr, 1):
                    add(x, y, z, 'stable', object, count)
                    sidetable(x, y, z, 3)
                else:
                    print("space occupied or object cancelled...")
        else:
            print("Exit")
            break
            t.home()
        floor(30, 30, 90)

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()



if __name__ == '__main__':
    arr = np.zeros([60, 60])            # arr - main matrix to map objects
    rooms = np.zeros([60, 60])          # rooms - track placement of rooms
    object = []                         # object - keeps track of placed objects
    room_details = []                   # keep track of room details
    count = [1, 1, 1, 1, 1, 1, 1, 1]    # sufix for the objects
    room_count = 1                      # no of rooms
    initializeturtle()                  # initialize the turtle window
    
    saturdae(arr, object, count, rooms, room_details, room_count)
