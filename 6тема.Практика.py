# Створити словник оцінок передбачуваних студентів (Ключ – ПІ студента, значення – список оцінок студентів). Знайти
# найуспішнішого і самого слабенького за середнім балом.

students_score = {
    'student_1': [85, 90, 92, 88],
    'student_2': [76, 82, 80, 78],
    'student_3': [92, 95, 88, 90],
    'student_4': [60, 70, 65, 68]
}
def middle_score(score):
    return sum(score) / len(score)
    best_student = max(students_score, key=lambda student: midlle_score(students_score[student]))
    bad_student = min(students_score, key=lambda student: middle_score(students_score[student]))

    print("Best student:")
    print("Bad student:")
