class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hallo, mein Name ist {self.name}")





class Student(Person):
    def __init__(self, name, reason):
        super().__init__(name)
        self.reason = reason


student1 = Student("Jürgen","Pyton lernen")
student1.introduce()

print(student1.reason)









