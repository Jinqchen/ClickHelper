import os
import sys
import threading

import pyautogui
from datetime import datetime
import pynput
import time
from pynput import keyboard
from pynput.keyboard import Key, Controller

print("This is a auto click program, After running the program, enter the number of times you want to click,"
      "\n and then select the position to click within five seconds, and the mouse will click on that place "
      "\nfor how many times in a row. Press 'e' in keyboard to exit ")
times_clicks=input("How many times you wanna click")
times_clicks=int(times_clicks)
print("please click the position that you want this program clicks.\n"
      "press 'e' in keyboard can stop this program")







x_position = 0
y_position = 0
def on_click(x, y, button, pressed):
    global x_position
    global y_position
    x_position = x
    y_position=y


mouse_listener = pynput.mouse.Listener(on_click=on_click)
mouse_listener.start()
print("click within 5 seconds")
time.sleep(1)
print("click within 4 seconds")

time.sleep(1)
print("click within 3 seconds")

time.sleep(1)
print("click within 2 seconds")

time.sleep(1)
print("click within 1 seconds")

time.sleep(1)
print("click within 0 seconds")
def on_press(key):
    try:
        if format(key.char) == 'e':
            try:
                os._exit(0)
            except:
                print('Program is dead.')
    except:
        print("This key is not a char")



keybord_listener = pynput.keyboard.Listener(on_press=on_press)
keybord_listener.start()







def loop():

    click_point = pyautogui.Point(x=x_position , y=y_position)

    pyautogui.moveTo(click_point, duration=0)
    pyautogui.click(click_point)

for i in range (0,times_clicks):
    loop()


