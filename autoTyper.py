#!/bin/python3

import pyautogui
import time

delay = 10 # Inital Delay in Seconds
time.sleep(delay)

name = "./file.txt"   # File Name
interval = 0.07   # In Seconds

with open(name) as f:
	data = f.read()
	pyautogui.write(data, interval=interval)