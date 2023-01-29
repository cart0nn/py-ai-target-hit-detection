import cv2 as cv
import keyboard
import os
import vidstream.mediaHandler as mediaHandler
from vidstream.mediaHandler import path
import __main__

def visualDifference():
    global image_files
    image_files = [f for f in os.listdir(path) if f.endswith(".jpg") or f.endswith(".png")]    
    for mediaHandler.i in range(0, len(image_files), 2):
        img1 = cv.imread(os.path.join(path, image_files[mediaHandler.i]))
        img2 = cv.imread(os.path.join(path, image_files[mediaHandler.i + 1]))

        gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
        gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

        diff = float(cv.absdiff(gray1, gray2))
        print(diff)

        thresh = cv.threshold(diff, 0, 255, cv.THRESH_BINARY)[1]

        if diff > 0.01 and __main__.mode == 1:
            cv.imshow("Image 1", img1)
            cv.imshow("Image 2", img2)
            cv.imshow("Difference", thresh)
        if keyboard.is_pressed("f"):
            break