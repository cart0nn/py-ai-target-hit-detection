import os
import ffmpeg as fmpg
import time

filename = "streamSession_" + str(time.time()) + ".mp4"

def createVideo():
    # create empty video file
    vid = open('bin/vidstream/' + filename, mode='w')
    try:
       vid.write('placeholder')
    except:
        print('Something happened, and the file could not be written.')
    finally:
        pass
