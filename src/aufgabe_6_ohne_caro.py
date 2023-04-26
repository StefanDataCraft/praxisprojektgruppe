import pywizards as pyw

person1 = pyw.Person("Stepsi")
person1.introduce()

dozent1 = pyw.Dozent("Karli", "Ich bin ich, und du bist mein Sofa")
dozent1.introduce()
dozent1.add_skill("C++")
print(dozent1.get_skills())

student1 = pyw.Student("Ralf", "Reason")

workshop = pyw.Workshop("20.11.2023","20.12.2023","efeww")
workshop.add_participants(dozent1)
workshop.add_participants(dozent1)
workshop.add_participants(student1)
dozenten_in_workshop = workshop.dozenten
for dozent in dozenten_in_workshop:
    print(dozent.name)
print(workshop.start_date)
print(workshop.end_date)

studenten_df, dozenten_df = workshop.print_members()
print("studenten_df:")
print(studenten_df)
print("dozenten_df:")
print(dozenten_df)

