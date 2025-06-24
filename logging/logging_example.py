import logging

# Create a logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG) 

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  

# Create a file handler (saves logs to a file)
file_handler = logging.FileHandler('app.log', mode='w')  # Overwrite file each time
file_handler.setLevel(logging.DEBUG)  # Save DEBUG and above in the file

# Create a common log format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Apply the formatter to both handlers
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add both handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Example log messages
logger.debug("This is a DEBUG message.")
logger.info("This is an INFO message.")
logger.warning("This is a WARNING message.")
logger.error("This is an ERROR message.")
logger.critical("This is a CRITICAL message.")

print("Logging done. Check the terminal and 'app.log' file.")

