from datetime import datetime as dt
import pandas as pd

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hallo, mein Name ist {self.name}")


class Student(Person):
    def __init__(self, name,reason):
        super().__init__(name)
        self.reason = reason


class Dozent(Person):
    skill_list = []

    def __init__(self, name, biographie):
        super().__init__(name)
        self.biographie = biographie

    def add_skill(self, skill_name):
        self.skill_list.append(skill_name)

    def get_skills(self):
        return self.skill_list

class Workshop:
    #start_date
    #end_date
    #thema

    dozenten = []
    studenten = []

    def __init__(self, start_date, end_date, thema):
        try:
            self.start_date = dt.strptime(start_date, "%d.%m.%Y").date()
        except:
            print("Invalid start date")
            exit()
        try:
            self.end_date = dt.strptime(end_date, "%d.%m.%Y").date()
        except:
            print("Invalid end date")
            exit()
        self.thema = thema

    def add_participants(self, person):
        if type(person) is Student:
            self.studenten.append(person)
        elif type(person) is Dozent:
            self.dozenten.append(person)

    def print_members(self):
        studenten_df = pd.DataFrame()
        dozenten_df = pd.DataFrame()
        for student in self.studenten:
            student_to_insert = pd.DataFrame()
            student_to_insert['name'] = student.name
            studenten_df.loc[len(studenten_df)] = student_to_insert
        for dozent in self.dozenten:
            dozent_to_insert = pd.DataFrame()
            dozent_to_insert['name'] = dozent.name
            dozent_to_insert['skills'] = dozent.skill_list
            dozenten_df.loc[len(dozenten_df)] = dozent_to_insert
        return (studenten_df, dozenten_df)

