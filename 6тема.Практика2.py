students = {
    'Dasha Ivanova': ['Python', 'FrontEnd'],
    'Oksana Petrenko': ['FullStack'],
    'Dima Nazarenko': ['Python', 'Java'],
    'Sergiy Novyi': ['FrontEnd'],
    'Tamara Vyazova': ['Java']
}

students_in_multiple_groups = [student for student, groups in students.items() if len(groups) >= 2]

students_not_in_frontend = [student for student, groups in students.items() if 'FrontEnd' not in groups]

students_python_or_java = [student for student, groups in students.items() if 'Python' in groups or 'Java' in groups]

print("Студенти, які навчаються у двох та більше групах:")
for student in students_in_multiple_groups:
    print(student)

print("\nСтуденти, які не навчаються на фронтенді:")
for student in students_not_in_frontend:
    print(student)

print("\nСтуденти, які вивчають Python або Java:")
for student in students_python_or_java:
    print(student)
