import logging

# Confugure a logger so that useful information can be presented:
# level=logging.DEBUG means the level from which the logging or outputing should start, INFO is this case.
# filename is the name of the file to which the log should go to.
# filemode creates the file and overrides the file it already exits.
# format creates the time of the log, level name of the log, the message being logged, etc 

logging.basicConfig(level=logging.INFO, filename='log3.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

# separate log files are often prefered for large projects and this is done create custom loggings:

# __name__ gives the name of the current module which will be unique.
logger = logging.getLogger(__name__)

# A seperate file to contain the above logs can be created by using handlers.

# Set up a handler such that logs will go to log4.log in this example:
handler = logging.FileHandler('log4.log')

# Set up a formatter that will be used to configure or format the handler:
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Configure or set the format of the handler:
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# use the custom logger to log a message
logger.info('Test the custom logger')
