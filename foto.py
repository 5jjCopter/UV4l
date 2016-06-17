#!/usr/bin/python
import time
import picamera
DATE=$(date +"%Y-%m-%d_%H%M")
with picamera.PiCamera() as picx:
    picx.start_preview()
    time.sleep(1)
    picx.capture('/media/D571-1726/fotos/$DATE.jpg')
    picx.stop_preview()
    picx.close()
