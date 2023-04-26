from datetime import datetime as dt
import pandas as pd


class Person:
    personality_characteristics = []

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_personality_characteristic(self, skill_name):
        self.personality_characteristics.append(skill_name)

    def get_personality_characteristics(self):
        return self.personality_characteristics

    def introduce(self):
        print(f"Hallo, mein Name ist {self.name}, ich bin {self.age} Jahre alt")


class Student(Person):
    soft_skills = []
    hard_skills = []

    def __init__(self, name, age, reason):
        super().__init__(name, age)
        self.reason = reason

    def add_soft_skill(self, soft_skill_name):
        self.soft_skills.append(soft_skill_name)

    def get_soft_skills(self):
        return self.soft_skills

    def add_hard_skill(self, hard_skill_name):
        self.hard_skills.append(hard_skill_name)

    def get_hard_skills(self):
        return self.hard_skills


class Professor(Person):
    skills = []

    def __init__(self, name, age, biographie):
        super().__init__(name, age)
        self.biographie = biographie

    def add_skill(self, skill_name):
        self.skills.append(skill_name)

    def get_skills(self):
        return self.skills


class Workshop:
    professors = []
    students = []

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

    def add_participants(self, person):
        if type(person) is Student:
            self.students.append(person)
        elif type(person) is Professor:
            self.professors.append(person)

    def get_members(self):
        students_list = []
        professors_list = []
        for student in self.students:
            student_to_insert = dict()
            student_to_insert['name'] = student.name
            student_to_insert['age'] = student.age
            student_to_insert['personality_characteristics'] = student.personality_characteristics
            student_to_insert['soft_skills'] = student.soft_skills
            student_to_insert['hard_skills'] = student.hard_skills
            student_to_insert['reason'] = student.reason
            students_list.append(student_to_insert)
        students_df = pd.DataFrame(students_list)
        for professor in self.professors:
            professor_to_insert = dict()
            professor_to_insert['name'] = professor.name
            professor_to_insert['age'] = professor.age
            professor_to_insert['personality_characteristics'] = professor.personality_characteristics
            professor_to_insert['skills'] = professor.skills
            professors_list.append(professor_to_insert)
        professors_df = pd.DataFrame(professors_list)
        return {"students": students_df, "professors": professors_df}

    def get_workshop(self):
        return {"start_date": self.start_date, "end_date": self.end_date, "thema": self.thema}

    def get_details(self):
        members = self.get_members()
        workshop = self.get_workshop()
        students = members["students"]
        professors = members["professors"]
        return {"workshop": workshop, "students": students, "professors": professors}

    def print_members(self):
        members = self.get_members()
        print("members")
        print(members)
        print("*************************")
        print("Studenten: ")
        for student in members["students"]:
            print(student)
            print(f"Name: "+student["name"])
            print(f"Alter: {student.age}")
            print("Persönlichkeitsmerkmale:")
            for personal_characteristic in student.personal_characteristics:
                print(personal_characteristic)
            print("Soft skills:")
            for soft_skill in student.soft_skills:
                print(soft_skill)
            print("Soft skills:")
            for hard_skill in student.hard:
                print(hard_skill)
        print("*************************")
        print("Dozenten: ")
        for professor in members["professors"]:
            print(f"Name: {professor.name}")
            print(f"Alter: {professor.age}")
            print("Persönlichkeitsmerkmale:")
            for personal_characteristic in professor.personal_characteristics:
                print(personal_characteristic)
            print("Skills:")
            for skill in professor.soft_skills:
                print(skill)
        print("*************************")

    def print_workshop(self):
        workshop = self.get_workshop()
        start_date = workshop["start_date"]
        formatted_start_date = start_date.strftime("%d.%m.%Y")
        end_date = workshop["end_date"]
        formatted_end_date = end_date.strftime("%d.%m.%Y")
        thema = workshop["thema"]
        print(f"Von: {formatted_start_date} bis {formatted_end_date}")
        print(f"Thema: {thema}")
        print("*************************")

    def print_details(self):
        self.print_workshop()
        self.print_members()
