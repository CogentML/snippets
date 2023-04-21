import logging

# Create a logger and set its level to DEBUG
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler that logs all messages to a file named 'output.log'
file_handler = logging.FileHandler('output.log')
file_handler.setLevel(logging.DEBUG)

# Create a formatter that formats log messages
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

def square_n_numbers(n):
    for i in range(1, n+1):
        square = i * i
        print(f"{i} squared is {square}")
        logger.debug(f"{i} squared is {square}")

# Test the function
square_n_numbers(5)