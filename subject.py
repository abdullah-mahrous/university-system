class Subject:
    def __init__(self,name,credit,major):
        self.name = name
        self.credit = credit
        self.major = major
        self.exams = []
        self.gpa = 0

    def calc_subject_gpa(self):
        total = 0
        for exam in self.exams:
            total += exam.mark
        if total/len(self.exams) >= 90:
            self.gpa = 4
        elif total/len(self.exams) >= 80:
            self.gpa = 3.5
        elif total/len(self.exams) >= 70:
            self.gpa = 3
        elif total/len(self.exams) >= 60:
            self.gpa = 2.5
        elif total/len(self.exams) >= 50:
            self.gpa = 2
        elif total/len(self.exams) < 50:
            self.gpa = 0

    def display_data(self):
        print(f"name: {self.name}\ncredits: {self.credit}\nmajor: {self.major}\n")
        for exam in self.exams:
            print(f"exam name: {exam.name}\nexam duration: {exam.duration}\nnumber of questions: {len(exam.questions)}\n")
