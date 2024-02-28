from check import *
from furniture import *
from rooms import *

# adding a new object to object array
# x - x coordinate in pixels
# y - y coordinate in pixels
# z - angle
# object - array containing placed object details
# count - count of each object placed [bed, sofa, window, door, table, tv, sbed, stable]


def add(x, y, z, a, object, count):
    if a == 'bed':
        # creating unique object if with name and number
        temp = a + str(count[0])
        object.append([x, y, z, temp])
        count[0] = count[0] + 1
        
    elif a == 'sofa':
        temp = a + str(count[1])
        object.append([x, y, z, temp])
        count[1] = count[1] + 1
        
    elif a == 'window':
        temp = a + str(count[2])
        object.append([x, y, z, temp])
        count[2] = count[2] + 1
        
    elif a == 'door':
        temp = a + str(count[3])
        object.append([x, y, z, temp])
        count[3] = count[3] + 1
        
    elif a == 'table':
        temp = a + str(count[4])
        object.append([x, y, z, temp])
        count[4] = count[4] + 1
        
    elif a == 'tv':
        temp = a + str(count[5])
        object.append([x, y, z, temp])
        count[5] = count[5] + 1
        
    elif a == 'sbed':
        temp = a + str(count[6])
        object.append([x, y, z, temp])   
        count[6] = count[6] + 1 
        
    elif a == 'stable':
        temp = a + str(count[7])
        object.append([x, y, z, temp])
        count[7] = count[7] + 1

# removing object a - userinput
# arr - array 
# object - contains placed objects


def remove(a, arr, object, room_details):
    flag = 0
    for i in object:
        # i = [x, y, z, object_name]
        if i[3] == a:
            # check for substring
            if i[3].__contains__('sbed'):
                # if true remove object from arr and object 
                # 1 - white colour
                singlebed(i[0], i[1], i[2], 1)
                if checksinglebed(i[0], i[1], i[2], arr, 0):
                    # 0 - remove value
                    start_x, start_y, room_length, room_width = findroom(i[0], i[1], room_details)
                    room(start_x, start_y, room_length, room_width, 3)
                    object.pop(flag)
                    return True
                else:
                    return False
            elif i[3].__contains__('stable'):
                sidetable(i[0], i[1], i[2], 1)
                if checksidetable(i[0], i[1], i[2], arr, 0):
                    start_x, start_y, room_length, room_width = findroom(i[0], i[1], room_details)
                    room(start_x, start_y, room_length, room_width, 3)
                    object.pop(flag)
                    return True
                else:
                    return False
            elif i[3].__contains__('bed'):
                bed(i[0], i[1], i[2], 1)
                if checkbed(i[0], i[1], i[2], arr, 0):
                    start_x, start_y, room_length, room_width = findroom(i[0], i[1], room_details)
                    room(start_x, start_y, room_length, room_width, 3)
                    object.pop(flag)
                    return True
                else:
                    return False
            elif i[3].__contains__('sofa'):
                sofa(i[0], i[1], i[2], 1)
                if checksofa(i[0], i[1], i[2], arr, 0):
                    start_x, start_y, room_length, room_width = findroom(i[0], i[1], room_details)
                    room(start_x, start_y, room_length, room_width, 3)
                    object.pop(flag)
                    return True
                else:
                    return False
            elif i[3].__contains__('window'):
                window(i[0], i[1], i[2], 1)
                if checkwindow(i[0], i[1], i[2], arr, 0):
                    start_x, start_y, room_length, room_width = findroom(i[0], i[1], room_details)
                    room(start_x, start_y, room_length, room_width, 3)
                    object.pop(flag)
                    return True
                else:
                    return False
            elif i[3].__contains__('door'):
                door(i[0], i[1], i[2], 1)
                if checkdoor(i[0], i[1], i[2], arr, 0):
                    start_x, start_y, room_length, room_width = findroom(i[0], i[1], room_details)
                    room(start_x, start_y, room_length, room_width, 3)
                    object.pop(flag)
                    return True
                else:
                    return False
            elif i[3].__contains__('table'):
                table(i[0], i[1], i[2], 1)
                if checktable(i[0], i[1], i[2], arr, 0):
                    start_x, start_y, room_length, room_width = findroom(i[0], i[1], room_details)
                    room(start_x, start_y, room_length, room_width, 3)
                    object.pop(flag)
                    return True
                else:
                    return False
        elif i[3].__contains__('tv'):
            tv(i[0], i[1], i[2], 1)
            if checktv(i[0], i[1], i[2], arr, 0):
                start_x, start_y, room_length, room_width = findroom(i[0], i[1], room_details)
                room(start_x, start_y, room_length, room_width, 3)
                object.pop(flag)
                return True
            else:
                return False
        flag = flag + 1
        