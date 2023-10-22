import logging

# Confugure a logger so that useful information can be presented:
# level=logging.DEBUG means the level from which the logging or outputing should start, DEBUG is this case.
# filename is the name of the file to which the log should go to.
# filemode creates the file and overrides the file it already exits.
# format creates the time of the log, level name of the log, the message being logged, etc 

logging.basicConfig(level=logging.DEBUG, filename='log3.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

# variable can also be logged

x = 10
logging.info(f"The value of x is {x}")

# logging a stack trace when an exceptions has occured

try:
  x = 1 / 0
except ZeroDivisionError as Error:
  logging.error('ZeroDivisionError', exc_info=True)
  
# or use

try:
  x = 1 / 0
except ZeroDivisionError as Error:
  logging.exception('ZeroDivisionError')