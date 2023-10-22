import logging

# create an internal logger with the name of the module
logger = logging.getLogger(__name__) 
# set propation False so that nothing is printed when helper is imported.
logger.propagate = False
logger.info('Hello from helper')