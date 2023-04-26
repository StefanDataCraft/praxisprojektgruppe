from datetime import datetime as dt
import pandas as pd


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hallo, mein Name ist {self.name}")


class Student(Person):
    def __init__(self, name, reason):
        super().__init__(name)
        self.reason = reason


class Professor(Person):
    skill_list = []

    def __init__(self, name, biographie):
        super().__init__(name)
        self.biographie = biographie

    def add_skill(self, skill_name):
        self.skill_list.append(skill_name)

    def get_skills(self):
        return self.skill_list


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
            student_to_insert['reason'] = student.reason
            students_list.append(student_to_insert)
        students_df = pd.DataFrame(students_list)
        for professor in self.professors:
            professor_to_insert = dict()
            professor_to_insert['name'] = professor.name
            professor_to_insert['skills'] = professor.skill_list
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
        print("Studenten: ")
        print(members["students"])
        print("*************************")
        print("Dozenten: ")
        print(members["professors"])
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
