import logging
"""
# set the basic configuration so that all the loggings below are printed:
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%y %H:%M:%S')

# The logging below indicate the severity of the events:
logging.debug(' This is a debug message')
logging.info(' This is a info message')

# By default only the loggings below will be printed:
logging.warning(' This is a warning message')
logging.error(' This is a error message')
logging.critical(' This is a critical message')

# By default the name of the logger is called root and it's not the best way to use when logging modules.

# Instead create a separate module with a user defined logger and then import the module:

import helper

# The creation of user defined logger means that there is now a heirachy starting from the root logger and this can be changed by setting propagation to False on the user defined module.
"""

"""
# log handlers are responsible for dispacthing appropriate log messages to the hendler specific destination.

# create a logger 
logger = logging.getLogger(__name__)

# create a handler - stream handler in this example
stream_h = logging.StreamHandler()

# create a file handler that logs to the file
file_h = logging.FileHandler('file.log')

# Set the level for each handler
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

# create a formatter and then set the format for each handler
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

# add the handlers to the formatters
logger.addHandler(stream_h)
logger.addHandler(file_h)

# use the logger
logger.warning('This is a warning')
logger.error('This is an error')

# user defined configuration by creating a separate file and then import it: 
import logging.config

logging.config.fileConfig('logging.config')

# Then create a logger

logger = logging.getLogger('simpleExample')

# use the logger
logger.debug('This is a debug message')
"""

"""
# capturing stack traces in logs - helpful for troubleshooting

try:
  x = [1, 2, 3, 4, 5]
  val = x[10]
except IndexError as Error:
  logging.error(Error, exc_info=True)

# exc_info gives the tracebakc, line where the error occurs

# if the error raised is not known:
import traceback

try:
  x = [1, 2, 3, 4, 5]
  val = x[10]
except:
  logging.error(f'The error is {traceback.format_exc()}')
  
# rorating file handers

from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over the log after 2kb to another log file and keep 5 buckup logs, i.e. app.log.1, app.log.2, etc

handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

# As an example, log a lot of messages
for _ in range(10000):
  logger.info('Hello, world!')
"""
  
# an application will be running for long time - create a rotating log based on how much time has passed

from logging.handlers import TimedRotatingFileHandler
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# when can it can roll over, s for seconds, m for minutes, h for hours, d for day, midnight or weekdays w0 for monday, w1 for Tuesdat, etc

handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

# As an example, log a lot of messages
for _ in range(6):
  logger.info('Hello, world!')
  time.sleep(5)
  