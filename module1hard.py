grades = [[[5, 3, 3, 5, 4],[3, 4, 5,  2, 5],[3, 2, 3, 5]], \
          [[2, 2, 2, 3],[5, 5, 4, 5],[5, 5, 5]], \
          [[4, 5, 5, 2],[4, 3, 5, 5],[3, 4, 4]], \
          [[4, 4, 3],[5, 2, 2, 4],[3, 4]], \
          [[5, 5, 5, 4, 5],[2, 3, 5],[3, 3]]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
disciplines = ['Mathematics', 'Python programming', 'Physical culture']
dict_avr_balls ={}
s = -1
d = -1
for student in sorted(students):
    s = s + 1
    d = -1
    student_avr_ball = 0
    print(student.upper(), ':')
    for discipline in disciplines:
        d = d + 1
        average = sum(grades[s][d])/len(grades[s][d])
        di = discipline + '\t'
        di = di.expandtabs(20)
        gr = str(grades[s][d]) + '\t'
        gr = gr.expandtabs(20)
        print('\t', di, ':', gr, ' - ', f"{average:.2}")
        student_avr_ball = student_avr_ball + average
    print("\t Individual average ball - ", f"{student_avr_ball / len(disciplines):.3}")
    dict_avr_balls[student] = student_avr_ball / len(disciplines)
print('------------')
print(dict_avr_balls)
