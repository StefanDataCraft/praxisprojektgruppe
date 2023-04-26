import pywizards as pyw

person1 = pyw.Person("Stepsi", 55)
person1.introduce()

professor1 = pyw.Professor("Karli", 55, "Ich bin ich, und du bist mein Sofa")
professor1.introduce()
professor1.add_personality_characteristic("Pers char 1")
professor1.add_personality_characteristic("Pers char 2")
professor1.add_skill("C++")
professor1.add_skill("PHP")
print(professor1.get_skills())

professor2 = pyw.Professor("Mani", 55, "Ich bin ich, und du bist mein Sessel")
professor2.introduce()
professor2.add_personality_characteristic("Pers char 1.0")
professor2.add_personality_characteristic("Pers char 2.0")
professor2.add_skill("Javascript")
professor2.add_skill("HTML")

student1 = pyw.Student("Ralf", 35, "Reason")
student1.add_hard_skill("Hard skill 1")
student1.add_hard_skill("Hard skill 2")
student1.add_soft_skill("Soft skill 1")
student1.add_soft_skill("Soft skill 2")

student2 = pyw.Student("Peter", 35, "Why?")
student2.add_hard_skill("Hard skill 1.0")
student2.add_hard_skill("Hard skill 2.0")
student2.add_soft_skill("Soft skill 1.0")
student2.add_soft_skill("Soft skill 2.0")

workshop = pyw.Workshop("20.11.2223","20.12.9999","efeww")
workshop.add_participants(professor1)
workshop.add_participants(professor2)
workshop.add_participants(student1)
workshop.add_participants(student2)
professors_in_workshop = workshop.professors
for professor in professors_in_workshop:
    print(professor.name)
print(workshop.start_date)

print("Teilnehmer: ")
workshop.print_members()
print("Workshop: ")
workshop.print_workshop()
print("Details: ")
workshop.print_details()
