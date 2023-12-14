import random
import time

import pyautogui

# Set the initial delay before starting the automation
initial_delay = 5  # 5 seconds

# Get the screen size
screen_width, screen_height = pyautogui.size()

# Main loop
while True:
    # Wait for a random interval between 5 to 10 seconds
    random_interval = random.uniform(3, 7)
    time.sleep(random_interval)

    # Choose a random action (1 = scroll, 2 = move cursor)
    random_action = random.randint(1, 2)

    if random_action == 1:
        # Scroll the mouse wheel
        # Adjust this value for scrolling intensity
        scroll_amount = random.randint(-100, 100)
        pyautogui.scroll(scroll_amount)
    else:
        # Move the cursor to a random position on the screen
        new_x = random.randint(0, screen_width)
        new_y = random.randint(0, screen_height)
        pyautogui.moveTo(new_x, new_y)
