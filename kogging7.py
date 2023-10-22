import logging
import employee2

# when importing a module, it runs a the code from that specific module.

# when the code is runned the operations.log file is not created.

# this is because the root logger is configured once and in this case this will inside the employee2 module where the level is info because it runs when it's imported.

# this can be solved by setting debug to info but will log into the employee2.log file instead of creating an operations.log file.

# this can be solve creating a logger inside the employee2 module
 
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
logging.info(f"Add: {num1} + {num2} = {addResult}")

subtractResult = subtract(num1, num2)
logging.info(f"Subtract: {num1} - {num2} = {subtractResult}")

multiplyResult = multiply(num1, num2)
logging.info(f"Multiply: {num1} * {num2} = {multiplyResult}")

divideResult = divide(num1, num2)
logging.info(f"Divide: {num1} / {num2} = {divideResult}")