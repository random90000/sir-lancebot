import os
import logging.handlers

# set up logging

log_dir = 'log'
log_file = log_dir + os.sep + 'hackbot.log'
os.makedirs(log_dir, exist_ok=True)

# file handler sets up rotating logs every 5 MB
file_handler = logging.handlers.RotatingFileHandler(
    log_file, maxBytes=5*(2**20), backupCount=10)
file_handler.setLevel(logging.DEBUG)

# console handler prints to terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# remove old loggers if any
root = logging.getLogger()
if root.handlers:
    for handler in root.handlers:
        root.removeHandler(handler)

# setup new logging configuration
logging.basicConfig(format='%(asctime)s - %(name)s %(levelname)s: %(message)s', datefmt="%D %H:%M:%S",
                    level=logging.DEBUG,
                    handlers=[console_handler, file_handler])

logging.info('Logging Process Started')