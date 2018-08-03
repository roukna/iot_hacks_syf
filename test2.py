# PIR sensor test script for Raspberry Pi
import time
import RPi.GPIO as io
import pygame
import os, sys
import random

io.setmode(io.BCM)
pir_pin = 18
io.setup(pir_pin, io.IN)         

while True:
    if io.input(pir_pin):
        print "Motion Detected, playing music..."
#   time.sleep(0.25)
