import numpy as np
from furniture import *
import turtle as t

# x is the x cordinate
# y is the y cordinate
# w is the angle
# arr is the matrix to update
# c is the value to update (1 for add object, 0 for remove object)


def checkbed(x, y, w, arr, c):
    # x values are in pixels must be converted to feet
    # 10 pixels = 1 feet, here it is divided by 5 to get accuracy upto 0.5 feet
    # necessary conversion is dont to map onject to array
    # temp is used to check if object add(1)/remove(0)
    b = x // 5 
    a = (y // 5) * -1 - 1
    temp = True if c == 0 else False
    
    # different usecases
    if w == 0:
        
        # esceeding limit of workspace
        if x > 240 or y > 230:
            return False
        
        # if object remove fill array with 0 and return
        if temp:
            arr[a:a - 14:-1, b:b + 12] = c
            return True
        
        # else check if space is occupied
        if np.sum(arr[a:a - 14:-1, b:b + 12]) == 0:
            # 2 - green colour to ask for confirmation
            bed(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            
            # if confirmed fill the array - object will be turned black in the main function
            if flag:
                arr[a:a - 14:-1, b:b + 12] = c
                return True
            # else fill with white and return
            else:
                for i in range(46):
                    t.undo()
                return False
            
        # if space occupied return false
        else:
            return False
        
    elif w == 90:
        if x > 230 or y < 60:
            return False
        if temp:
            arr[a:a + 12, b:b + 14] = c
            return True
        if np.sum(arr[a:a + 12, b:b + 14]) == 0:
            bed(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a + 12, b:b + 14] = c
                return True
            else:
                for i in range(46):
                    t.undo()
                return False
        else:
            return False
    elif w == 180:
        if x < 60 or y < 70:
            return False
        if temp:
            arr[a:a + 14, b:b - 12:-1] = c
            return True
        if np.sum(arr[a:a + 14, b:b - 12:-1]) == 0:
            bed(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a + 14, b:b - 12:-1] = c
                return True
            else:
                for i in range(46):
                    t.undo()
                return False
        else:
            return False
    elif w == 270:
        if x < 70 or y > 240:
            return False
        if temp:
            arr[a:a - 12:-1, b:b - 14:-1] = c
            return True
        if np.sum(arr[a:a - 12:-1, b:b - 14:-1]) == 0:
            bed(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a - 12:-1, b:b - 14:-1] = c
                return True
            else:
                for i in range(46):
                    t.undo()
                return False
        else:
            return False


def checksofa(x, y, w, arr, c):
    b = x // 5
    a = (y // 5) * -1 - 1
    temp = True if c == 0 else False
    if w == 0:
        if x > 240 or y > 275:
            return False
        if temp:
            arr[a:a - 5:-1, b:b + 12] = c
            return True
        if np.sum(arr[a:a - 5:-1, b:b + 12]) == 0:
            sofa(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a - 5:-1, b:b + 12] = c
                return True
            else:
                for i in range(41):
                    t.undo()
                return False
        else:
            return False
    elif w == 90:
        if x > 275 or y < 60:
            return False
        if temp:
            arr[a:a + 12, b:b + 5] = c
            return True
        if np.sum(arr[a:a + 12, b:b + 5]) == 0:
            sofa(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a + 12, b:b + 5] = c
                return True
            else:
                for i in range(41):
                    t.undo()
                return False
        else:
            return False
    elif w == 180:
        if x < 60 or y < 25:
            return False
        if temp:
            arr[a:a + 5, b:b - 12:-1] = c
            return True
        if np.sum(arr[a:a + 5, b:b - 12:-1]) == 0:
            sofa(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a + 5, b:b - 12:-1] = c
                return True
            else:
                for i in range(41):
                    t.undo()
                return False
        else:
            return False
    elif w == 270:
        if x < 25 or y > 240:
            return False
        if temp:
            arr[a:a - 12:-1, b:b - 5:-1] = c
            return True
        if np.sum(arr[a:a - 12:-1, b:b - 5:-1]) == 0:
            sofa(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a - 12:-1, b:b - 5:-1] = c
                return True
            else:
                for i in range(41):
                    t.undo()
                return False
        else:
            return False


def checkwindow(x, y, w, arr, c):
    b = x // 5
    a = (y // 5) * -1 - 1
    temp = True if c == 0 else False
    if w == 0:
        if x > 260 or y > 295:
            return False
        if temp:
            arr[a:a - 1:-1, b:b + 8] = c
            return True
        if np.sum(arr[a:a - 1:-1, b:b + 8]) == 0:
            window(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a - 1:-1, b:b + 8] = c
                return True
            else:
                for i in range(11):
                    t.undo()
                return False
        else:
            return False
        
    elif w == 90:
        if x > 295 or y < 40:
            return False
        if temp:
            arr[a:a + 8, b:b + 1] = c
            return True
        if np.sum(arr[a:a + 8, b:b + 1]) == 0:
            window(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a + 8, b:b + 1] = c
                return True
            else:
                for i in range(11):
                    t.undo()
                return False
        else:
            return False
        
    elif w == 180:
        if x < 40 or y < 5:
            return False
        if temp:
            arr[a:a + 1, b:b - 8:-1] = c
            return True
        if np.sum(arr[a:a + 1, b:b - 8:-1]) == 0:
            window(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a + 1, b:b - 8:-1] = c
                return True
            else:
                for i in range(11):
                    t.undo()
                return False
        else:
            return False
    elif w == 270:
        if x < 5 or y > 260:
            return False
        if temp:
            arr[a:a - 8:-1, b:b - 1:-1] = c
            return True
        if np.sum(arr[a:a - 8:-1, b:b - 1:-1]) == 0:
            window(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a - 8:-1, b:b - 1:-1] = c
                return True
            else:
                for i in range(11):
                    t.undo()
                return False
        else:
            return False


def checkdoor(x, y, w, arr, c):
    b = x // 5
    a = (y // 5) * -1 - 1
    temp = True if c == 0 else False
    if w == 0:
        if x > 275 or y < 25:
            return False
        if temp:
            arr[a:a + 5, b:b + 5] = c
            return True
        if np.sum(arr[a:a + 5, b:b + 5]) == 0:
            door(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a + 5, b:b + 5] = c
                return True
            else:
                for i in range(6):
                    t.undo()
                return False
        else:
            return False
    elif w == 90:
        if x > 275 or y > 275:
            return False
        if temp:
            arr[a:a - 5: -1, b:b + 5] = c
            return True
        if np.sum(arr[a:a - 5: -1, b:b + 5]) == 0:
            door(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a - 5: -1, b:b + 5] = c
                return True
            else:
                for i in range(6):
                    t.undo()
                return False
        else:
            return False
    elif w == 180:
        if x < 25 or y > 275:
            return False
        if temp:
            arr[a:a - 5: -1, b:b - 5: -1] = c
            return True
        if np.sum(arr[a:a - 5: -1, b:b - 5: -1]) == 0:
            door(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a - 5: -1, b:b - 5: -1] = c
                return True
            else:
                for i in range(6):
                    t.undo()
                return False
        else:
            return False
    elif w == 270:
        if x < 25 or y < 25:
            return False
        if temp:
            arr[a:a + 5, b:b - 5: -1] = c
            return True
        if np.sum(arr[a:a + 5, b:b - 5: -1]) == 0:
            door(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a + 5, b:b - 5: -1] = c
                return True
            else:
                for i in range(6):
                    t.undo()
                return False
        else:
            return False


def checktable(x, y, w, arr, c):
    b = x // 5
    a = (y // 5) * -1 - 1
    temp = True if c == 0 else False
    if w == 0:
        if x > 230 or y > 240:
            return False
        if temp:
            arr[a:a - 12:-1, b:b + 14] = c
            return True
        if np.sum(arr[a:a - 12:-1, b:b + 14]) == 0:
            table(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a - 12:-1, b:b + 14] = c
                return True
            else:
                for i in range(97):
                    t.undo()
                return False
        else:
            return False
    elif w == 90:
        if x > 240 or y < 70:
            return False
        if temp:
            arr[a:a + 14, b:b + 12] = c
            return True
        if np.sum(arr[a:a + 14, b:b + 12]) == 0:
            table(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a + 14, b:b + 12] = c
                return True
            else:
                for i in range(97):
                    t.undo()
                return False
        else:
            return False
    elif w == 180:
        if x < 70 or y < 60:
            return False
        if temp:
            arr[a:a + 12, b:b - 14:-1] = c
            return True
        if np.sum(arr[a:a + 12, b:b - 14:-1]) == 0:
            table(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a + 12, b:b - 14:-1] = c
                return True
            else:
                for i in range(97):
                    t.undo()
                return False
        else:
            return False
    elif w == 270:
        if x < 60 or y > 230:
            return False
        if temp:
            arr[a:a - 14:-1, b:b - 12:-1] = c
            return True
        if np.sum(arr[a:a - 14:-1, b:b - 12:-1]) == 0:
            table(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a - 14:-1, b:b - 12:-1] = c
                return True
            else:
                for i in range(97):
                    t.undo()
                return False
        else:
            return False


def checktv(x, y, w, arr, c):
    b = x // 5
    a = (y // 5) * -1 - 1
    temp = True if c == 0 else False
    if w == 0:
        if x > 255 or y > 285:
            return False
        if temp:
            arr[a:a - 2:-1, b:b + 9] = c
            return True
        if np.sum(arr[a:a - 2:-1, b:b + 9]) == 0:
            tv(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a - 2:-1, b:b + 9] = c
                return True
            else:
                for i in range(34):
                    t.undo()
                return False
        else:
            return False
    elif w == 90:
        if x > 285 or y < 45:
            return False
        if temp:
            arr[a:a + 9, b:b + 2] = c
            return True
        if np.sum(arr[a:a + 9, b:b + 2]) == 0:
            tv(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a + 9, b:b + 2] = c
                return True
            else:
                for i in range(34):
                    t.undo()
                return False
        else:
            return False
    elif w == 180:
        if x < 45 or y < 15:
            return False
        if temp:
            arr[a:a + 2, b:b - 9:-1] = c
            return True
        if np.sum(arr[a:a + 2, b:b - 9:-1]) == 0:
            tv(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a + 2, b:b - 9:-1] = c
                return True
            else:
                for i in range(34):
                    t.undo()
                return False
        else:
            return False
    elif w == 270:
        if x < 15 or y > 255:
            return False
        if temp:
            arr[a:a - 9:-1, b:b - 2:-1] = c
            return True
        if np.sum(arr[a:a - 9:-1][b:b - 2:-1]) == 0:
            tv(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag and temp:
                arr[a:a - 9:-1, b:b - 2:-1] = c
                return True
            else:
                for i in range(34):
                    t.undo()
                return False
        else:
            return False


def checksinglebed(x, y, w, arr, c):
    b = x // 5
    a = (y // 5) * -1 - 1
    temp = True if c == 0 else False
    if w == 0:
        if x > 270 or y > 240:
            return False
        if temp:
            arr[a:a - 12:-1, b:b + 6] = c
            return True
        if np.sum(arr[a:a - 12:-1, b:b + 6]) == 0:
            singlebed(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a - 12:-1, b:b + 6] = c
                return True
            else:
                for i in range(34):
                    t.undo()
                return False
        else:
            return False
    elif w == 90:
        if x > 240 or y < 30:
            return False
        if temp:
            arr[a:a + 6, b:b + 12] = c
            return True
        if np.sum(arr[a:a + 6, b:b + 12]) == 0:
            singlebed(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a + 6, b:b + 12] = c
                return True
            else:
                for i in range(34):
                    t.undo()
                return False
        else:
            return False
    elif w == 180:
        if x < 30 or y < 60:
            return False
        if temp:
            arr[a:a + 12, b:b - 6:-1] = c
            return True
        if np.sum(arr[a:a + 12, b:b - 6:-1]) == 0:
            singlebed(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a + 12, b:b - 6:-1] = c
                return True
            else:
                for i in range(34):
                    t.undo()
                return False
        else:
            return False
    elif w == 270:
        if x < 60 or y > 270:
            return False
        if temp:
            arr[a:a - 6:-1][b:b - 12:-1] = c
            return True
        if np.sum(arr[a:a - 6:-1, b:b - 12:-1]) == 0:
            singlebed(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a - 6:-1, b:b - 12:-1] = c
                return True
            else:
                for i in range(34):
                    t.undo()
                return False
        else:
            return False
      
      
def checksidetable(x, y, w, arr, c):
    b = x // 5
    a = (y // 5) * -1 - 1
    temp = True if c == 0 else False
    if w == 0:
        if x > 275 or y > 280:
            return False
        if temp:
            arr[a:a - 4:-1, b:b + 6] = c
            return True
        if np.sum(arr[a:a - 4:-1, b:b + 6]) == 0:
            sidetable(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a - 4:-1, b:b + 6] = c
                return True
            else:
                for i in range(19):
                    t.undo()
                return False
        else:
            return False
    elif w == 90:
        if x > 280 or y < 25:
            return False
        if temp:
            arr[a:a + 6, b:b + 4] = c
            return True
        if np.sum(arr[a:a + 6, b:b + 4]) == 0:
            sidetable(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a + 6, b:b + 4] = c
                return True
            else:
                for i in range(19):
                    t.undo()
                return False
        else:
            return False
    elif w == 180:
        if x < 25 or y < 20:
            return False
        if temp:
            arr[a:a + 4, b:b - 6:-1] = c
            return True
        if np.sum(arr[a:a + 4, b:b - 6:-1]) == 0:
            sidetable(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a + 4, b:b - 6:-1] = c
                return True
            else:
                for i in range(19):
                    t.undo()
                return False
        else:
            return False
    elif w == 270:
        if x < 20 or y > 275:
            return False
        if temp:
            arr[a:a - 6:-1, b:b - 4:-1] = c
            return True
        if np.sum(arr[a:a - 6:-1, b:b - 4:-1]) == 0:
            sidetable(x, y, w, 2)
            flag = int(input("Is this position okay (1/0) : "))
            if flag:
                arr[a:a - 6:-1, b:b - 4:-1] = c
                return True
            else:
                for i in range(19):
                    t.undo()
                return False
        else:
            return False
