# PIR sensor test script for Raspberry Pi
import time
import RPi.GPIO as io
import pygame
import os, sys
import random

_prev_songs = os.listdir("/home/pi/Downloads/tracks/prev_track")
_next_songs = os.listdir("/home/pi/Downloads/tracks/next_track")

io.setmode(io.BCM)
pir_pin = 18
io.setup(pir_pin, io.IN)         

while True:
    if io.input(pir_pin):
        print("Motion Detected, playing music...")
        pygame.mixer.init()
        music1 = random.choice(_prev_songs)
        pygame.mixer.music.load('/home/pi/Downloads/tracks/prev_track/'+music1)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue;
        music2 = random.choice(_next_songs)
        pygame.mixer.music.load('/home/pi/Downloads/tracks/next_track/'+music2)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
#   time.sleep(0.25)
