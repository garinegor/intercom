from picamera import PiCamera
import RPi.GPIO as GPIO
from time import sleep
import os,funcs

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.OUT)

camera = PiCamera()
camera.vflip = True
camera.hflip = True

while True:
    if GPIO.input(21) == False:
        camera.start_preview()
        print("getting photo")
        sleep(2)
        camera.stop_preview()

        if 'came_new' in os.listdir():
            camera.capture('./came_new/image.jpg')
        else:
            camera.capture('./came/image.jpg')
            os.rename('came','came_new')

        if funcs.compare('george','./came_new/image.jpg'):
            GPIO.output(i, True)
            sleep(2)
            GPIO.output(i, False)
            os.rename('./came_new/image.jpg','./came_new/george.jpg')
        else:
            GPIO.output(i, True)
            sleep(1)
            GPIO.output(i, False)
            sleep(1)
            GPIO.output(i, True)
            sleep(1)
            GPIO.output(i, False)
            
        print('folder has been renamed')
        sleep(0.2)