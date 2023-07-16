from person import Person
from teacher import Teacher
from student import Student
from datetime import datetime
from subject import Subject
import random

class Admin(Person):
    def __init__(self, name, email, password, dob, academic_number, phone_number, address,rule):
        super().__init__(name, email, password, dob, academic_number, phone_number, address,rule)

    def display_data(self):
        print("name: " + self.name + "\nemail: " + self.email)
        encrypted_password = ""
        for i in range(len(self.password) - 2):
            encrypted_password += "*"
        encrypted_password += self.password[-2];
        encrypted_password += self.password[-1]
        print("password : " + encrypted_password)
        print("age: " + str(self.age) + "\nacademic number: " + str(
            self.academic_code) + "\nphone number: " + self.phone_number + "\naddress: " + self.address)

    def add_teacher(self):
        name = input("Enter teacher name: ")
        email = input("Enter teacher email: ")
        password = input("Enter teacher password: ")
        dob = datetime.strptime(input("Enter teacher date of birth: "), "%d-%m-%Y")
        an = random.randint(0,1000000)
        pn = input("Enter teacher phone number: ")
        address = input("Enter teacher address: ")
        sd = input("Enter teacher start date: ")
        salary = input("Enter teacher salary: ")
        rule = "Teacher"
        return Teacher(name,email,password,dob,an,pn,address,sd,salary,rule)

    def add_student(self):
        name = input("Enter student name: ")
        email = input("Enter student email: ")
        password = input("Enter student password: ")
        dob = datetime.strptime(input("Enter student date of birth: "), "%d-%m-%Y")
        an = random.randint(0,1000000)
        pn = input("Enter student phone number: ")
        address = input("Enter student address: ")
        status = input("Enter student status: ")
        major = input("Enter student major: ")
        level = input("Enter student level: ")
        rule = "Student"
        return Student(name,email,password,dob,an,pn,address,status,major,level,rule)

    def add_admin(self):
        name = input("Enter admin name: ")
        email = input("Enter admin email: ")
        password = input("Enter admin password: ")
        dob = datetime.strptime(input("Enter admin date of birth: "), "%d-%m-%Y")
        an = random.randint(0, 1000000)
        pn = input("Enter admin phone number: ")
        address = input("Enter admin address: ")
        rule = "Admin"
        return Admin(name,email,password,dob,an,pn,address,rule)

    def add_subject(self):
        name = input("Enter subject name: ")
        credits = input("Enter subject credits: ")
        major = input("Enter subject major: ")
        return Subject(name,credits,major)

