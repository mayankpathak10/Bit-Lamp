# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 15:17:51 2018

@author: Darshan
"""
import time
import RPi.GPIO as GPIO

def Check_button_press():
    prev_input = 0
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17,GPIO.IN)
    input = GPIO.input(17)
    while True:
  #take a reading
  #if the last reading was low and this one high, print
      if ((not prev_input) and input):
          print("Button pressed")
          time.sleep(0.05)
          return True