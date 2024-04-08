def countStudents(students, sandwiches):
    if students.count(1) == sandwiches.count(1) and students.count(0) == sandwiches.count(0):
        return 0

    else:
        current_student = 0
        while sandwiches and sandwiches[0] in students:
            if students[current_student] == sandwiches[0]:
                students.remove(students[current_student])
                sandwiches.pop(0)
                current_student = 0
            else:
                current_student += 1
                if current_student >= len(students):
                    current_student = 0

    return len(students)


std = [0,0,1,1,0,0,0,0,1,0,0,1,1,0,1,1]
sand = [1,0,0,0,0,0,0,1,0,0,1,0,1,1,1,0]



print(countStudents(std, sand))