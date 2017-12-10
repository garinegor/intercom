from time import sleep
import config,telebot,json,os,pygame
from telebot import types
import RPi.GPIO as GPIO
from picamera import PiCamera

bot = telebot.TeleBot(config.token)
users=[202226598, 56345999]
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
camera = PiCamera()
camera.vflip = True
camera.hflip = True
pygame.init()
my_sound = pygame.mixer.Sound('./foo.wav')

while True:
    input_state = GPIO.input(21)
    if input_state == False:
        my_sound.play()
        bot.send_message(202226598, "кто-то пришел")
        camera.start_preview()
        sleep(2)
        camera.capture('./image.jpg')
        camera.stop_preview()
        bot.send_photo(chat_id=202226598, photo=open('./image.jpg', 'rb'))
        sleep(0.2)

if __name__ == '__main__':
    bot.polling(none_stop=True)
