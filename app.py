from datetime import datetime
from admin import Admin
import random

the_admin = Admin("abdullah","rbkhg3@gmail.com","123dlf",datetime.strptime("14-11-2002", "%d-%m-%Y"),random.randint(0,1000000),
                   "01009204925","56 alexandria","Admin")

teachers = []
students = []
admins = [the_admin]
subjects = []

while True:
    start = input("sign in as\n1-admin\n2-teacher\n3-student\nq-to quite the program\n")

    if start == "q":
        break

    sign_up_email = input("Enter your email: ")
    sign_up_password = input("Enter your password: ")

    if start == "1":
        for admin in admins:
            if sign_up_email == admin.email and sign_up_password == admin.password:
                while True:
                    start = input("1-display data\n2-add admin\n3-add teacher\n4-add student\n5-add subject\nq-to go back\n"
                                  "6-display all admins\n7-display all teachers\n8-display all students\n9-display all subjects\n")
                    if start == "1":
                        admin.display_data()
                    elif start == "2":
                        admins.append(admin.add_admin())
                    elif start == "3":
                        teachers.append(admin.add_teacher())
                    elif start == "4":
                        students.append(admin.add_student())
                    elif start == "5":
                        subjects.append(admin.add_subject())
                    elif start == "6":
                        for admin in admins:
                            print(admin.display_data())
                            print("\n*******************************\n")
                    elif start == "7":
                        for teacher in teachers:
                            print(teacher.display_data())
                            print("\n*******************************\n")
                    elif start == "8":
                        for student in students:
                            print(student.display_data())
                            print("\n*******************************\n")
                    elif start == "9":
                        for subject in subjects:
                            print(subject.display_data())
                            print("\n*******************************\n")
                    elif start == "q":
                        break
            else:
                continue

    elif start == "2":
        for teacher in teachers:
            if sign_up_email == teacher.email and sign_up_password == teacher.password:
                while True:
                    start = input("1-display data\n2-make an exam\nq-to go back\n")
                    if start == "1":
                        teacher.display_data()
                    elif start == "2":
                        examed_subject = input("which subject do you want to make an exam for: ")
                        for subject in subjects:
                            if subject.name == examed_subject:
                                subject.exams.append(teacher.make_exam())
                            else:
                                continue
                    elif start == "q":
                        break
            else:
                continue

    elif start == "3":
        for student in students:
            if sign_up_email == student.email and sign_up_password == student.password:
                while True:
                    start = input("1-display data\n2-enroll in subject\n3-unroll in subject\n4-take an exam\nq-to go back\n")
                    if start == "1":
                        student.display_data()

                    elif start == "2":
                        selected_subject = input("enter subject name you want to enroll in: ")
                        for subject in subjects:
                            if subject.name == selected_subject:
                                student.enroll(subject)
                                break
                            else:
                                continue
                            print(f"no subject with name {selected_subject}")

                    elif start == "3":
                        selected_subject = input("enter subject name you want to unroll in: ")
                        for subject in subjects:
                            if subject.name == selected_subject:
                                student.unroll(subject)
                                break
                            else:
                                continue
                            print(f"no subject with name {selected_subject}")

                    elif start == "4":
                        selected_subject = input("enter the subject you want to take its exam: ")
                        for subject in student.subjects:
                            if subject.name == selected_subject:
                                exam_name = input("enter exam name: ")
                                try:
                                    for exam in student.subjects[subjects.index(subject)].exams:
                                        if exam_name == exam.name:
                                            exam.start_exam()
                                except:
                                    print("no exam with that name")

                    elif start == "q":
                        break