import logging

# Confugure a logger so that useful information can be presented:
# level=logging.DEBUG means the level from which the logging or outputing should start, DEBUG is this case.
# filename is the name of the file to which the log should go to.
# filemode creates the file and overrides the file it already exits.
# format creates the time of the log, level name of the log, the message being logged, etc 

logging.basicConfig(level=logging.DEBUG, filename='log2.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

# There are different levels of logging:

logging.debug("This is a debug message")
logging.info("This is an info message")

# By default the program will print anything from warning level and above:
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

# root stands for whihc logger is being used.



