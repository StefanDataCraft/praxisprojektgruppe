# Classes definition
from datetime import datetime as dt


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.personality_characteristics = []

    def add_personality_characteristic(self, skill_name):
        self.personality_characteristics.append(skill_name)

    def get_personality_characteristics(self):
        return self.personality_characteristics

    def introduce(self):
        print(f"Hallo, mein Name ist {self.name}, ich bin {self.age} Jahre alt und bin {', '.join(self.personality_characteristics)}.")


class Student(Person):
    def __init__(self, name, age, reason):
        super().__init__(name, age)
        self.reason = reason
        self.soft_skills = []
        self.hard_skills = []

    def add_soft_skill(self, soft_skill_name):
        self.soft_skills.append(soft_skill_name)

    def get_soft_skills(self):
        return self.soft_skills

    def add_hard_skill(self, hard_skill_name):
        self.hard_skills.append(hard_skill_name)

    def get_hard_skills(self):
        return self.hard_skills


class Professor(Person):
    def __init__(self, name, age, biographie):
        super().__init__(name, age)
        self.biographie = biographie
        self.skills = []

    def add_skill(self, skill_name):
        self.skills.append(skill_name)

    def get_skills(self):
        return self.skills


class Workshop:
    def __init__(self, start_date, end_date, thema):
        try:
            self.start_date = dt.strptime(start_date, "%d.%m.%Y").date()
        except ValueError:
            print("Invalid start date")
            exit()
        try:
            self.end_date = dt.strptime(end_date, "%d.%m.%Y").date()
        except ValueError:
            print("Invalid end date")
            exit()
        self.thema = thema
        self.professors = []
        self.students = []

    def add_participants(self, person):
        if type(person) is Student:
            self.students.append(person)
        elif type(person) is Professor:
            self.professors.append(person)

    # Returns workshop info
    def get_workshop(self):
        return {"start_date": self.start_date, "end_date": self.end_date, "thema": self.thema}

    # Prints members from workshop info
    def print_members(self):
        print("Studenten:")
        print("----------------------------")
        for student in self.students:
            print(f"Name: {student.name}")
            print(f"Alter: {student.age}")
            print("Persönlichkeitsmerkmale:")
            for personality_characteristic in student.personality_characteristics:
                print(personality_characteristic)
            print("Soft skills:")
            for soft_skill in student.soft_skills:
                print(soft_skill)
            print("Hard skills:")
            for hard_skill in student.hard_skills:
                print(hard_skill)
            print("----------------------------")
        print("+++++++++++++++++++++++++++++++++")
        print("Dozenten: ")
        for professor in self.professors:
            print(f"Name: {professor.name}")
            print(f"Alter: {professor.age}")
            print("Persönlichkeitsmerkmale:")
            for personality_characteristic in professor.personality_characteristics:
                print(personality_characteristic)
            print("Skills:")
            for skill in professor.skills:
                print(skill)
            print("----------------------------")
        print("*************************")

    # Print workshop info
    def print_workshop(self):
        workshop = self.get_workshop()
        start_date = self.start_date
        formatted_start_date = start_date.strftime("%d.%m.%Y")
        end_date = self.end_date
        formatted_end_date = end_date.strftime("%d.%m.%Y")
        thema = self.thema
        print(f"Von: {formatted_start_date} bis {formatted_end_date}")
        print(f"Thema: {thema}")

    # Prints workshop details ((calling print_workshop & print_members
    def print_details(self):
        self.print_workshop()
        print("****************************************************")
        self.print_members()
