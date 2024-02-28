import turtle as t
from furniture import *
from check import *
from delete import *
from rooms import *
import numpy as np


def recommend_room(x, y, length, width, rooms):
    x = x // 10
    y = y // 10
    score = 0
    if x == 0 or x + width == 30:
        score += 1
    elif y == 0 or y + length == 30:
        score += 1
    if score == 1 or score == 2:
        return x * 10, y * 10, x * 10, y * 10, 0

    else:
        new_room_x = 0
        new_room_y = 0
        new_x = []
        new_y = []
        # quadrant lb
        if x < (30 - (x + width)) and y < (30 - (y + length)):
            # for room 1
            new_x.append(0 * 10)
            new_y.append(y * 10)
            # for room 2
            new_y.append(0 * 10)
            new_x.append(0 * 10)
            # for room 3
            new_y.append(0 * 10)
            new_x.append(x * 10)

        # quadrant tr
        elif x >= (30 - (x + width)) and y >= (30 - (y + length)):
            # for room 1
            new_x.append(x * 10)
            new_y.append((y + (30 - (y + length))) * 10)
            # for room 2
            new_y.append((y + (30 - (y + length))) * 10)
            new_x.append((x + (30 - (x + width))) * 10)
            # for room 3
            new_x.append((x + (30 - (x + width))) * 10)
            new_y.append(y * 10)

        # quadrant tl
        elif x < (30 - (x + width)) and y >= (30 - (y + length)):
            new_x.append(x * 10)
            new_y.append((y + (30 - (y + length))) * 10)

            new_x.append(0 * 10)
            new_y.append((y + (30 - (y + length))) * 10)

            new_x.append(0 * 10)
            new_y.append(y * 10)

        # quanrant br
        elif x >= (30 - (x + width)) and y < (30 - (y + length)):
            new_x.append((x + (30 - (x + width))) * 10)
            new_y.append(y * 10)

            new_x.append((x + (30 - (x + width))) * 10)
            new_y.append(0 * 10)

            new_x.append(x * 10)
            new_y.append(0 * 10)

        print("dont you think these rooms are in better position ??")
        print("room 1 is at the top, room 2 is in the middle, room 3 is at the bottom and room 4 is yours..")
        for i in range(3):
            if check_room_clash(new_x[i], new_y[i], length, width, rooms):
                room(new_x[i], new_y[i], length, width, 2)
            else:
                print("room {no} is not valid...".format(no=i+1))

        selected_room = int(input("which of these rooms would you like to keep : "))
        if selected_room < 0 or selected_room > 4:
            return x * 10, y * 10, x * 10, y * 10, 0

        for i in range(3):
            if selected_room == i + 1:
                new_room_x = new_x[i]
                new_room_y = new_y[i]
                break

        for i in range(3):
            room(new_x[i], new_y[i], length, width, 1)
        room(x * 10, y * 10, length, width, 1)
        # user selected the room he drew
        if selected_room == 4:
            return x * 10, y * 10, x * 10, y * 10, 0

        else:
            return x, y, new_room_x, new_room_y, 1


def hall_recommend(x, y, rooms, room_details):
    room_x, room_y, room_length, room_width = findroom(x, y, room_details)
    new_room = []
    print(room_x, room_y, room_length, room_width)
    # door bottom of the room
    if y == room_y:
        if room_x < 150:
            new_room.append([room_x, room_y - 100, 10, 16])
        else:
            new_room.append([room_x - (160 - room_width * 10), room_y - 100, 10, 16])
        new_room.append([room_x, room_y - room_length * 10, room_length, room_width])

    # door top of the room
    elif y == (room_y + room_length * 10):
        if room_x < 150:
            new_room.append([room_x, room_y + room_length * 10, 10, 16])
        else:
            new_room.append([room_x - (160 - room_width * 10), room_y + room_length * 10, 10, 16])
        new_room.append([room_x, room_y + room_length * 10, room_length, room_width])

    # door left of the room
    elif x == room_x:
        if room_y < 150:
            new_room.append([room_x - 100, room_y, 16, 10])
        else:
            new_room.append([room_x - 100, room_y - (160 - room_length * 10), 16, 10])
        new_room.append([room_x - room_width * 10, room_y, room_length, room_width])

    # door right of the room
    elif x == (room_x + room_width * 10):
        if room_y < 150:
            new_room.append([room_x + room_width * 10, room_y, 16, 10])
        else:
            new_room.append([room_x + room_width * 10, room_y - (160 - room_length * 10), 16, 10])
        new_room.append([room_x + room_width * 10, room_y, room_length, room_width])

    count = 0
    for i in new_room:
        count += 1
        if check_room_clash(i[0], i[1], i[2], i[3], rooms):
            room(i[0], i[1], i[2], i[3], 2)
        else:
            print("rooms {no} is clashing...".format(no=count))

    print("do you need these extra rooms...?")
    selected_room = int(input("1.big room 2.small room 3.no room : "))

    # clear the rooms
    for i in new_room:
        room(i[0], i[1], i[2], i[3], 1)

    # no room selected
    if selected_room == 3:
        for i in room_details:
            room(i[0], i[1], i[2], i[3])
        return False

    # big room selected
    elif selected_room == 1:
        room(new_room[0][0], new_room[0][1], new_room[0][2], new_room[0][3])
        b = new_room[0][0] // 5
        a = (new_room[0][1] // 5) * -1 - 1
        rooms[a:a - new_room[0][2] * 2:-1, b:b + new_room[0][3] * 2] = 1
        room_details.append([new_room[0][0], new_room[0][1], new_room[0][2], new_room[0][3]])
        name = input("enter the room name : ")
        t.setx(new_room[0][0] + 5)
        t.sety(new_room[0][1] + 5)
        t.write(name, font=("Verdana", 10, "normal"))
        return True

    # small room selected
    elif selected_room == 2:
        room(new_room[1][0], new_room[1][1], new_room[1][2], new_room[1][3])
        b = new_room[1][0] // 5
        a = (new_room[1][1] // 5) * -1 - 1
        rooms[a:a - new_room[1][2] * 2:-1, b:b + new_room[1][3] * 2] = 1
        room_details.append([new_room[1][0], new_room[1][1], new_room[1][2], new_room[1][3]])
        name = input("enter the room name : ")
        t.setx(new_room[1][0] + 5)
        t.sety(new_room[1][1] + 5)
        t.write(name, font=("Verdana", 10, "normal"))
        return True
     