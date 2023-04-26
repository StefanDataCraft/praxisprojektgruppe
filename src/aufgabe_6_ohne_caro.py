import pywizards as pyw

person1 = pyw.Person("Stepsi")
person1.introduce()

professor1 = pyw.Professor("Karli", "Ich bin ich, und du bist mein Sofa")
professor1.introduce()
professor1.add_skill("C++")
professor1.add_skill("PHP")
print(professor1.get_skills())

student1 = pyw.Student("Ralf", "Reason")

workshop = pyw.Workshop("20.11.2223","20.12.9999","efeww")
workshop.add_participants(professor1)
workshop.add_participants(professor1)
workshop.add_participants(student1)
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
