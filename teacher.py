from person import Person
from exam import Exam

class Teacher (Person):
    def __init__(self, name, email, password, dob, academic_number, phone_number, address,start_date,salary,rule):
        super().__init__(name, email, password, dob, academic_number, phone_number, address,rule)
        self.start_date = start_date
        self.salary = salary

    def display_data(self):
        print("name: " + self.name + "\nemail: " + self.email)
        encrypted_password = ""
        for i in range(len(self.password) - 2):
            encrypted_password += "*"
        encrypted_password += self.password[-2]; encrypted_password += self.password[-1]
        print("password : " + encrypted_password)
        print("age: " + str(self.age) + "\nacademic number: " + str(
            self.academic_code) + "\nphone number: " + self.phone_number + "\naddress: " + self.address + "\nsalary: " + str(
            self.salary) + "\n" + "start date: " + self.start_date)

    def make_exam(self):
        questions_number = int(input("how many question is in your exam?"))
        questions = []
        answers = []

        exam_name = input("enter exam name: ")
        for i in range(questions_number):
            questions.append(input("enter your questions with answers separated by \\n:\n"))
        for i in range(questions_number):
            answers.append(input("enter your answers with respect to questions order:\n"))
        duration = int(input("enter exam duration: "))

        if len(questions) <= 0 or len(answers) != len(questions) or duration <= 0:
            print("every question must have an answer and must has at-least 1 question, duration must be more than 1 minute")
            return

        return Exam(questions,answers,duration,exam_name)
    