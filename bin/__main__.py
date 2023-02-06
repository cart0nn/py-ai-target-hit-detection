import tkinter
from datetime import datetime
import multiprocessing as mp
import os
import cv2 as cv
import keyboard
import time


path = "bin/vidstream/streamSession_" + str(datetime.now().strftime("%Y%m%d_%H%M")) 


def runMediaFeed():  
    cap = cv.VideoCapture(0)
    global ret
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
    
def visualDifference():
    while True:
        image_files = [f for f in os.listdir(path) if f.endswith(".jpg") or f.endswith(".png")]    
        for i in range(0, len(image_files), 1):
            print(i, len(image_files), i + 1)

            img1 = cv.imread(os.path.join(path, image_files[i]))
            img2 = cv.imread(os.path.join(path, image_files[i + 1]))

            gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
            gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

            diff = float(cv.absdiff(gray1, gray2))
            print(diff)

            thresh = cv.threshold(diff, 0, 255, cv.THRESH_BINARY)[1]

            if diff > 0.01 and mode == 1:
                cv.imshow("Image 1", img1)
                cv.imshow("Image 2", img2)
                cv.imshow("Difference", thresh)
            if keyboard.is_pressed("f"):
                break  

# just gonna be function spam for now/gui creation in the future
def main():
   pass
   

if __name__ == '__main__':
   main()
   global mode
   mode = 0
   # mode 0 = unselected, mode 1 = opeartor, mode 2 = autonomous
   modeSelector = input("Would you like to run in operator mode or autonomous mode? o/a ")
   if modeSelector == "o":
      mode = 1
      print("Operator mode.")
   if modeSelector == "a":
      mode = 2
      print("Autonomous mode.")
   # create new empty directory
   
   try:
      os.mkdir(path)
   except OSError as error:
      print(error)
   finally:
      print(':)')
   p1 = mp.Process(target=runMediaFeed)
   p2 = mp.Process(target=visualDifference)
   p1.start()
   time.sleep(1)
   p2.start()
   p1.join()
   p2.join()