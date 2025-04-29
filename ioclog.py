'''
JMoody
ISS 212
4.2025 Wk 12 Tool Development 8 - reg1.py
NOTE: Use files: ioc-bfa.log, ioc-malexec.log, ioc-unauth.log
'''

import logging
from logging.handlers import TimedRotatingFileHandler

#Sets up basic logging to specific file
def basic_logging(output_file):
    logging.basicConfig(filename=output_file, level=logging.DEBUG)

#Sets up file rotating log
def file_rotation_logging(output_file):
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #Configures file handler to rotate logs daily
    file_handler = TimedRotatingFileHandler(output_file, when='midnight', backupCount=7)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    #Attaches handler to log
    logger.addHandler(file_handler)

#Logs error along with traceback if exception occurs
def log_error_with_traceback(output_file):
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename=output_file, level=logging.DEBUG)
    try:
        #Attempts to open file that does not exist to force error
        open('non_existent_file.txt', 'rb')  # Using a non-existent file path
    except Exception as exception:
        #Logs error message with traceback details
        logger.error('Failed to open file', exc_info=True)
        logger.exception('Failed to open file')

if __name__ == "__main__":
    #Prompts user to enter names for each log in output file
    output_file_basic = input("Enter log file name for basic logging: ")
    output_file_rotation = input("Enter log file name for file rotataion logging: ")
    output_file_error = input("Enter log file name for logging errors with traceback: ")
    output_file_combined = input("Enter log file name to combine all logs: ")

    #Runs each logging setup
    basic_logging(output_file_basic)
    file_rotation_logging(output_file_rotation)
    log_error_with_traceback(output_file_error)

    # Combine logs into a single file
    with open(output_file_combined, 'w') as combined_file:
        for log_file in [output_file_basic, output_file_rotation, output_file_error]:
            with open(log_file, 'r') as log:
                combined_file.write(log.read())
