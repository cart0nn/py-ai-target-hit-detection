import vidstream.mediaHandler as mediaHandler
import searcher
import tkinter
import time
import threading

# just gonna be function spam for now/gui creation in the future
def main():
   global mode
   mode = 0
   # mode 0 = unselected, mode 1 = opeartor, mode 2 = autonomous
   modeSelector = input("Would you like to run in operator mode or autonomous mode? o/a")
   while mode == 0:
      if modeSelector == "o":
         mode = 1
         print("Operator mode.")
      if modeSelector == "a":
         mode = 2
         print("Autonomous mode.")
   

if __name__ == '__main__':
   main()
   mediaHandler.newStream()
   t1 = threading.Thread(target=mediaHandler.runMediaFeed)
   t2 = threading.Thread(target=searcher.visualDifference)
   t1.start()
   t2.start()