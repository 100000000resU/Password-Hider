#python file hider by gubbna(1resU)
import win32con, win32api,os
import sys


run = True
file='test.txt'
password = "god"






def write():
        message = input("What message do you want to write?")
        f = open('test.txt','a')
        f.write(message)
        f.close()
        




def hideornot():
    choice = input("hide? Y or N?")
    if choice == "N":
        win32api.SetFileAttributes(file, win32con.FILE_ATTRIBUTE_NORMAL)
        run = False
    if choice == "Y":
        win32api.SetFileAttributes(file, win32con.FILE_ATTRIBUTE_HIDDEN)
        run = False
    else:
        run = False

def control():
    wanna = input("Do you want to write to the file? Y or N")
    if wanna == "Y":
        write()
        run = False
    else:
        hideornot()
        run = False
while run:
    passcheck = input("What is the password")
    if passcheck == password:
        print ("correct")
        control()
        run = False
    else:
        print("Wrong")
        run = False
           



