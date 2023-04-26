class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hallo, mein Name ist {self.name}")


class Student(Person):
    def __init__(self):
        pass


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
    #start_datum
    #end_datum
    #thema

    dozenten = []
    studenten = []

    def __init__(self):
        pass

    def add_participants(self, person):
        if type(person) is Student:
            self.studenten.append(person)
        elif type(person) is Dozent:
            self.dozenten.append(person)


person1 = Person("Stepsi")
person1.introduce()

dozent1 = Dozent("Karli", "Ich bin ich, und du bist mein Sofa")
dozent1.introduce()
dozent1.add_skill("C++")
print(dozent1.get_skills())

student1 = Student()

workshop = Workshop()
workshop.add_participants(dozent1)
workshop.add_participants(dozent1)
workshop.add_participants(student1)
dozenten_in_workshop = workshop.dozenten
for dozent in dozenten_in_workshop:
    print(dozent.name)
