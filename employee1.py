import logging

logging.basicConfig(filename='employee1.log', level=logging.INFO, format='%(asctime)s : %(levelname)s : %(message)s ')

class Employee:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    
    logging.info(f"Created Employee: {self.name} {self.surname}")
    
  @property
  def email(self):
    return f"{self.name}{self.surname}@email.com"
    
  @property
  def fullname(self):
    return f"{self.name}{self.surname}"
  
emp_1 = Employee('Mvano', 'Mgam')
emp_2 = Employee('Cecilia', 'Rangwanasha')
emp_3 = Employee('Emil', 'Boeke')