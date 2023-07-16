from person import Person

class Student(Person):
    def __init__(self, name, email, password, dob, academic_number, phone_number, address, status, major, level,rule):
        super().__init__(name, email, password, dob, academic_number, phone_number, address,rule)
        self.gpa = 0
        self.subjects = []
        self.status = status
        self.major = major
        self.level = level
        self.taken_exams = []

    def enroll(self,subject):
        try:
            self.subjects.append(subject)
            print(f"you have been enrolled successfully in {subject.name}")
        except:
            print("could not enroll in subject")

    def unroll(self,subject):
        try:
            self.subjects.remove(subject)
            print(f"you have been unenrolled successfully in {subject.name}")
        except:
            print("you did not enroll in this subject")

    def calc_gpa(self):
        subjects_credits = 0
        total_credits = 0
        for subject in self.subjects:
            subjects_credits += subject["credit"] * subject["gpa"]
            total_credits += subject["credit"]
        self.gpa = subjects_credits / total_credits

    def display_data(self):
        try:
            for subject in self.subjects:
                subject.calc_subject_gpa()
            self.calc_gpa()
        except:
            pass

        print("name: " + self.name + "\nemail: " + self.email)
        encrypted_password = ""
        for i in range(len(self.password) - 2):
            encrypted_password += "*"
        encrypted_password += self.password[-2];encrypted_password += self.password[-1]
        print("password : " + encrypted_password)
        print("age: " + str(self.age) + "\nacademic number: " + str(self.academic_code) + "\nphone number: " + self.phone_number + "\naddress: " + self.address + "\ngpa: " + str(self.gpa) + "\nsubjects: ")
        for subject in self.subjects:
            print(subject.name + "\t")
        print("major: " + self.major + "\nlevel: " + str(self.level))