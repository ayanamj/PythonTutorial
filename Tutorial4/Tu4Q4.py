class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def dataprint(self):
        print(f"Name: {self.name}, Roll No: {self.roll}")

student1 = Student("Sony", 40)
student2 = Student("Shotta", 48)

student1.dataprint()
student2.dataprint()
