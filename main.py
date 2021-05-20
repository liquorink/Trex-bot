from PIL import ImageGrab, ImageOps
import time
import pyautogui
from numpy import *

while True:
    # The position of the square collision (based on your resulotion)
    x1, y1, a, b = 1200, 495, 87, 18
    # The calculation required for the box to know how far it should scan for 
    box = (x1, y1, x1 + a, y1 + b)
    image = ImageGrab.grab(box)
    gray = ImageOps.grayscale(image)
    a = array(gray.getcolors())
    value = a.sum()
    print(value)
    if value != 1813:
        time.sleep(0.05)
        pyautogui.keyDown("space")
 