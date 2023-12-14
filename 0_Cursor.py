import pyautogui
import time
import random

i = 0

while True:
    # Generate random x and y offsets between -5 and 5 pixels
    x_offset = random.randint(-100, 100)
    y_offset = random.randint(-100, 100)
    # Move the cursor by the random offsets
    pyautogui.move(x_offset, y_offset)
    # Wait for 10 seconds
    time.sleep(10)
    print(i)
    i += 1
