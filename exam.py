import threading
import time

class Exam:
    def __init__(self,questions,answers,duration,name):
        self.questions = questions
        self.answers = answers
        self.duration = duration
        self.name = name
        self.grade = 0
        self.mark = self.grade/len(questions) * 100
        self.finished = False

    def start_exam(self):
        thread1 = threading.Thread(target=self.timer)
        thread1.start()
        for question in self.questions:
            print(question)
            answer = input("enter your answer: ")
            if answer == self.answers[question]:
                self.grade += 1
        self.finished = True
        self.end_exam()

    def end_exam(self):
        print(f"Exam has ended, you have answered {self.grade} questions right")
        self.finished = True

    def timer(self):
        time.sleep(self.duration * 60)
        if not(self.finished):
            self.end_exam()
