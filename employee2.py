import logging

# create a logger variable where __name__ means when this module is runned directly here, __name__ will equal to __main__ and when this module is imported, __name__ will equal to the name of this module.

# if this logger does not exist then it will be created.
logger = logging.getLogger(__name__)

# set the log level on the logger
logger.setLevel(logging.INFO)

# create a formatter for the logger
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s ')

# created a file handler to specify a file that will be logged to.
file_handler = logging.FileHandler('employee2.log')

# add the formatter to the file handler
file_handler.setFormatter(formatter)

# add the employee2.log file to the logger 
logger.addHandler(file_handler)

class Employee:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    
    logger.info(f"Created Employee: {self.name} {self.surname}")
    
  @property
  def email(self):
    return f"{self.name}{self.surname}@email.com"
    
  @property
  def fullname(self):
    return f"{self.name}{self.surname}"
  
emp_1 = Employee('Mvano', 'Mgam')
emp_2 = Employee('Cecilia', 'Rangwanasha')
emp_3 = Employee('Emil', 'Boeke')