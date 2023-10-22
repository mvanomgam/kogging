import logging

# loggings allows for specification of what exactly must be logged.

# DEBUG: Useful when only when diagnosing a problem.

# INFO: Useful for confirming that things are working as expected.

# WARNING: This is the default leveli which indicates that something unexpected has happened or there could be a problem in future.

# ERROR: Indicates that due to a problem the program has not performed some function.

# CRITICAL: Indicates the program is unable to continue running.

logging.basicConfig(filename='operations.log', level=logging.DEBUG, format='%(asctime)s : %(levelname)s : %(message)s')

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
logging.debug(f"Add: {num1} + {num2} = {addResult}")

subtractResult = subtract(num1, num2)
logging.debug(f"Subtract: {num1} - {num2} = {subtractResult}")

multiplyResult = multiply(num1, num2)
logging.debug(f"Multiply: {num1} * {num2} = {multiplyResult}")

divideResult = divide(num1, num2)
logging.debug(f"Divide: {num1} / {num2} = {divideResult}")