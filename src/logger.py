'''
'logger.py'

Purpose:
This script sets up a logging system for the project.

Key Components:

Sets up a logging configuration, including a filename based on the current date and time.

Steps:
1. Create a logs directory if it doesn't exist.
2. Configure the logging system to write logs to a file with a timestamped filename.

Execution:
If run as the main script, it logs a message indicating that logging has started.
'''

import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s  %(lineno)d %(name)s - %(levelname)s - %(message)s]",
    level=logging.INFO

)
if __name__=="__main__":
    logging.info("Logging has started")