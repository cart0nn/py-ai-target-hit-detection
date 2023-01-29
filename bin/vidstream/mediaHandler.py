import os
import ffmpeg as fmpg
import time
import cv2 as cv
import keyboard

path = "bin/vidstream/streamSession_" + str(time.time())

def newStream():
    # create new empty directory
    try:
        os.mkdir(path)
    except OSError as error:
        print(error)
    finally:
        print(':)')
        

def runMediaFeed():
    cap = cv.VideoCapture(0)
    global i
    i = 0
    # start dumping frames into stream directory from camera
    while(cap.isOpened()):
        global frame_name
        frame_name = path + "/Frame" + str(i) + ".jpg"
        ret, frame = cap.read()
        if ret == False:
            break
        if keyboard.is_pressed('f') == True:
            break 
        cv.imwrite(frame_name, frame)
        i += 1
    cap.release()
    cv.destroyAllWindows()
    print("Camera feed lost :(")  