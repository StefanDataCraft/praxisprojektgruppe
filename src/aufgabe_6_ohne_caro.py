import pywizards as pyw

person1 = pyw.Person("Stepsi")
person1.introduce()

professor1 = pyw.Professor("Karli", "Ich bin ich, und du bist mein Sofa")
professor1.introduce()
professor1.add_skill("C++")
print(professor1.get_skills())

student1 = pyw.Student("Ralf", "Reason")

workshop = pyw.Workshop("20.11.2023","20.12.2023","efeww")
workshop.add_participants(professor1)
workshop.add_participants(professor1)
workshop.add_participants(student1)
professors_in_workshop = workshop.professors
for professor in professors_in_workshop:
    print(professor.name)
print(workshop.start_date)
print(workshop.end_date)

students_df, professors_df = workshop.get_workshops()
print("students_df:")
print(students_df)
print("professors_df:")
print(professors_df)

