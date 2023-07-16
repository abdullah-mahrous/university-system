from abc import ABC,abstractmethod
from datetime import date
import random

class Person(ABC):
    def __init__(self,name,email,password,dob,academic_number,phone_number,address,rule):
        self.name = name
        self.email = email
        self.password = password
        self.dob = dob
        self.age = self.calc_age()
        self.academic_code = random.randint(0,1000000)
        self.phone_number = phone_number
        self.address = address
        self.rule = rule

    @abstractmethod
    def display_data(self):
        pass

    def calc_age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month,today.day) < (self.dob.month,self.dob.day))
