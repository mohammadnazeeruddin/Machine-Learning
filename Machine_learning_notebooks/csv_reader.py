students_marks = []
with open('student_marks.csv') as f:
    for line in f:
        columns = line.split(',')
        columns[-1] = int(columns[-1].rstrip('\n'))
        students_marks.append(tuple(columns))

subject_faculty = []
with open('subject_faculty.csv') as f:
    for line in f:
        columns = line.split(',')
        columns[-1] = columns[-1].rstrip('\n')
        students_marks.append(tuple(columns))

