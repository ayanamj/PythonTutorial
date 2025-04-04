class Student:
    def __init__(self):
        self.rollno = 0
        self.mark1 = 0
        self.mark2 = 0
    def readData(self, rollno, mark1, mark2):
        self.rollno = rollno
        self.mark1 = mark1
        self.mark2 = mark2
    def computeTotal(self):
        return self.mark1 + self.mark2
    def printDetails(self):
        total = self.computeTotal()
        print(f"Roll Number: {self.rollno}, Mark 1: {self.mark1}, Mark 2: {self.mark2}, Total Marks: {total}")
student1 = Student()
student1.readData(44, 23, 32)
student1.printDetails()
