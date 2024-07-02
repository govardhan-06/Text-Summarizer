import os
import sys
import logging

'''
This module sets up logging for the project. It creates a logger object that can be used to log messages to the console and a log file. The log file is stored in the logs directory. The logger object is named "textSummarizerLogger" and is used to log messages at the INFO level. The log messages are formatted with the timestamp, logger name, log level, and message. The log messages are written to the console and the log file. The log file is created if it does not exist. The log file is named "runtime.log" and is stored in the logs directory. The log messages are written to the log file in append mode
'''

# Set up logging
logging_str='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
log_dir="logs"
log_filepath=os.path.join(log_dir, 'runtimeLogs.log')
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# Create a logger
logger = logging.getLogger("textSummarizerLogger")