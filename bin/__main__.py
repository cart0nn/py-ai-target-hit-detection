from datetime import datetime
import multiprocessing as mp
import os
import cv2 as cv
import keyboard
import time
import subprocess

class mediaFeedHandler:
    def __init__(self):
        self.path = "bin/vidstream/streamSession_" + str(datetime.now().strftime("%Y%m%d_%H%M"))
        self.mode = 0

    def mode_selector(self):
        global mode
        self.mode = 0
        # mode 0 = unselected, mode 1 = opeartor, mode 2 = autonomous
        modeSelector = input("Would you like to run in operator mode or autonomous mode? o/a ")
        if modeSelector == "o":
            self.mode = 1
            print("Operator mode selected.")
        if modeSelector == "a" or modeSelector != "a" or modeSelector != "o":
            self.mode = 2
            print("Autonomous mode selected or invalid input received.")
            
    def start_media_feed(self):
        # create new empty directory        
        try:
            os.mkdir(self.path)
        except OSError as error:
            print(error)
        finally:
            print(':)')
            
    def path_error_handler(self):
        # pseudocode cause idk how to do this... yet
        # if start_media_feed() returns WinError 183
            # self.path = "bin/vidstream/streamSession_" + str(datetime.now().strftime("%Y%m%d_%H%M%s"))
        pass

    def run_media_feed(self):  
        cap = cv.VideoCapture(0)
        global ret
        i = 0
        # start dumping frames into stream directory from camera
        while(cap.isOpened()):
            global frame_name
            frame_name = self.path + "/Frame" + str(i) + ".jpg"
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
        
    def visual_difference(self):
        while True:
            image_files = [f for f in os.listdir(self.path) if f.endswith(".jpg") or f.endswith(".png")]    
            for i in range(0, len(image_files), 1):
                print(i, len(image_files), i + 1)

                img1 = cv.imread(os.path.join(self.path, image_files[i]))
                img2 = cv.imread(os.path.join(self.path, image_files[i + 1]))

                gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
                gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

                diff = float(cv.absdiff(gray1, gray2))
                print(diff)

                thresh = cv.threshold(diff, 0, 255, cv.THRESH_BINARY)[1]

                if diff > 0.01 and self.mode == 1:
                    cv.imshow("Image 1", img1)
                    cv.imshow("Image 2", img2)
                    cv.imshow("Difference", thresh)
                if keyboard.is_pressed("f"):
                    break
                
    def main(self):
        self.__init__()
        self.mode_selector()
        self.start_media_feed()
        # self.path_error_handler()
        p1 = mp.Process(target=self.run_media_feed)
        p2 = mp.Prorcess(target=self.visual_difference)
        p1.start()
        time.sleep(5)
        p2.start()
        p1.join()
        p2.join()
                
class guiHandler:

    def __init__(self):
        self.path = "../bin/gui.ts"
    
    def ts_launcher(self):
        result = subprocess.run(['tsc', self.path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print(f"TypeScript file {self.path} compiled successfully")
        else:
            print(f"Error compiling TypeScript file {self.path}: {result.stderr.decode()}")
            
    def main(self):
        self.ts_launcher("gui.ts")
   

if __name__ == '__main__':
    mediaFeedHandler.main()