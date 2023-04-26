class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hallo, mein Name ist {self.name}")


class Dozent(Person):
    skill_list = []

    def __init__(self, name, biographie):
        super().__init__(name)
        self.biographie = biographie

    def add_skill(self, skill_name):
        self.skill_list.append(skill_name)

    def get_skills(self):
        return self.skill_list


person1 = Person("Stepsi")
person1.introduce()

dozent1 = Dozent("Karli", "Ich bin ich, und du bist mein Sofa")
dozent1.introduce()
dozent1.add_skill("C++")
print(dozent1.get_skills())
