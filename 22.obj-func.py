class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def on_honor_roll(self):
        return self.gpa >= 3.5
