import logging

# if this logger does not exist then it will be created.
logger = logging.getLogger(__name__)

# set the log level on the logger
logger.setLevel(logging.DEBUG)

# create a formatter for the logger
formatter = logging.Formatter('%(asctime)s : %(name)s : %(message)s ')

# created a file handler to specify a file that will be logged to.
file_handler = logging.FileHandler('operations4.log')

# add the formatter to the file handler and set the level to be logged to the log file.
# this means the debug statements below will not be logged.
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

# add the operations4.log file to the logger 
logger.addHandler(file_handler)

# rather the debug statements below can displayed on the console
stream_handler = logging.StreamHandler()

# add the formatter to the stream handler
stream_handler.setFormatter(formatter)

# add the stream handler to the logger
logger.addHandler(stream_handler)

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  try:
    result = x / y
  except ZeroDivisionError:
    # logger.error('Division by zero not allowed')
    
    # Instead of logger.error it's better to use traceback 
    logger.exception('Division by zero not allowed')
  else:
    return result
  
num1 = 10
num2 = 0

addResult = add(num1, num2)
logger.debug(f"Add: {num1} + {num2} = {addResult}")

subtractResult = subtract(num1, num2)
logger.debug(f"Subtract: {num1} - {num2} = {subtractResult}")

multiplyResult = multiply(num1, num2)
logger.debug(f"Multiply: {num1} * {num2} = {multiplyResult}")

divideResult = divide(num1, num2)
logger.debug(f"Divide: {num1} / {num2} = {divideResult}")