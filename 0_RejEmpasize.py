import random
import time

import pyautogui

# Set the initial delay before starting the automation
initial_delay = 5  # 5 seconds

# Get the screen size
screen_width, screen_height = pyautogui.size()

# Main loop
while True:
    # Wait for a random interval between 10 to 20 seconds
    random_interval = random.randint(10, 20)
    time.sleep(random_interval)

    # Calculate the center of the screen
    center_x, center_y = screen_width // 2, screen_height // 2

    # Choose a random action (1 = scroll, 2 = type, 3 = click)
    random_action = random.randint(1, 3)

    if random_action == 1:
        # Scroll the mouse wheel
        scroll_amount = random.randint(-100, 100)  # Adjust this value for scrolling intensity
        pyautogui.scroll(scroll_amount)
    elif random_action == 2:
        # Simulate a random number of key presses (typing)
        num_key_presses = random.randint(5, 20)  # Adjust this value for the number of key presses
        random_chars = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(num_key_presses))
        pyautogui.moveTo(center_x, center_y)  # Move to the center before typing
        pyautogui.typewrite(random_chars)
    else:
        # Simulate a mouse click around the center
        click_radius = 50  # Adjust this value for the click radius
        click_x = random.randint(center_x - click_radius, center_x + click_radius)
        click_y = random.randint(center_y - click_radius, center_y + click_radius)
        pyautogui.click(click_x, click_y)

# To stop the script, you can manually interrupt it (e.g., Ctrl+C)




# import random
# import time

# import pyautogui

# # Set the initial delay before starting the automation
# initial_delay = 5  # 5 seconds

# # Get the screen size
# screen_width, screen_height = pyautogui.size()

# # Main loop
# while True:
#     # Wait for a random interval between 10 to 20 seconds
#     random_interval = random.randint(5, 10)
#     time.sleep(random_interval)

#     # Calculate the center of the screen
#     center_x, center_y = screen_width // 2, screen_height // 2

#     # Choose a random action (1 = scroll, 2 = type, 3 = click)
#     random_action = random.randint(1, 3)

#     if random_action == 1:
#         # Scroll the mouse wheel
#         scroll_amount = random.randint(-100, 100)  # Adjust this value for scrolling intensity
#         pyautogui.scroll(scroll_amount)
#     elif random_action == 2:
#         # Simulate a random number of key presses (typing)
#         num_key_presses = random.randint(5, 20)  # Adjust this value for the number of key presses
#         random_chars = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(num_key_presses))
#         pyautogui.moveTo(center_x, center_y)  # Move to the center before typing
#         pyautogui.typewrite(random_chars)
#     else:
#         # Simulate a mouse click
#         pyautogui.click(center_x, center_y)

# To stop the script, you can manually interrupt it (e.g., Ctrl+C)

#---------------------------------Code01-------------------------------------------
# import pyautogui
# import time
# import random

# # Set the initial delay before starting the automation
# initial_delay = 5  # 5 seconds

# # Main loop
# while True:
#     # Wait for a random interval between 10 to 20 seconds
#     random_interval = random.randint(10, 20)
#     time.sleep(random_interval)

#     # Generate random mouse movements
#     x, y = random.randint(0, 1920), random.randint(0, 1080)
#     pyautogui.moveTo(x, y, duration=1)

#     # Simulate a random number of key presses (typing)
#     num_key_presses = random.randint(5, 20)  # Adjust this value for the number of key presses
#     random_chars = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(num_key_presses))
#     pyautogui.typewrite(random_chars)

#     # Scroll the mouse wheel
#     scroll_amount = random.randint(-3, 3)  # Adjust this value for scrolling intensity
#     pyautogui.scroll(scroll_amount)

#     # Simulate a mouse click
#     pyautogui.click()

# # To stop the script, you can manually interrupt it (e.g., Ctrl+C)
#---------------------------------Code01-------------------------------------------

