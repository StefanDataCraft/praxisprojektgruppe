class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hallo, mein Name ist {self.name}")


class Student(Person):
    def __init__(self, name,reason):
        super().__init__(name)
        self.reason = reason

    def introduce(self):

        print(f"Ich bin {self.name}")



name1 = Student("Jürgen","Ich möchte Python lernen")
name1.introduce()
print(name1.reason)