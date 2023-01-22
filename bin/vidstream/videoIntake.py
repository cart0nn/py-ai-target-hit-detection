import os
import ffmpeg as fmpg
import time

filename = "streamSession_" + str(time.time()) + ".mp4"

def startStream():
    # create empty video file
    vid = open('bin/vidstream/' + filename, mode='w')
    try:
       vid.write('placeholder')
    except:
        print('yea that dont work')
    finally:
        print('done, fuck you python')