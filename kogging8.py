import logging

# if this logger does not exist then it will be created.
logger = logging.getLogger(__name__)

# set the log level on the logger
logger.setLevel(logging.DEBUG)

# create a formatter for the logger
formatter = logging.Formatter('%(asctime)s : %(name)s : %(message)s ')

# created a file handler to specify a file that will be logged to.
file_handler = logging.FileHandler('operations2.log')

# add the formatter to the file handler 
file_handler.setFormatter(formatter)

# add the operations2.log file to the logger 
logger.addHandler(file_handler)

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

num1 = 10
num2 = 5

addResult = add(num1, num2)
logger.debug(f"Add: {num1} + {num2} = {addResult}")

subtractResult = subtract(num1, num2)
logger.debug(f"Subtract: {num1} - {num2} = {subtractResult}")

multiplyResult = multiply(num1, num2)
logger.debug(f"Multiply: {num1} * {num2} = {multiplyResult}")

divideResult = divide(num1, num2)
logger.debug(f"Divide: {num1} / {num2} = {divideResult}")