# collection exampels from https://www.youtube.com/watch?v=Zee665ssm8Y&t=12s

from collections import defaultdict, Counter


def ex1():
    exam_grades = [('bob', 100), ('joe', 92,), ('emily', 95), ('bob', 85), ('joe', 87), ('frazer', 91)]

    student_grades = defaultdict(list)  # defautdict takes in the `list` function

    # unpack the e
    for name, grade in exam_grades:
        student_grades[name].append(grade)

    print(f'type(exam_grades) = {type(student_grades)}')
    print(student_grades)
    print(student_grades['emma'])  # this will not fail/throw an error, return an emtpy list

# quick way counting occuring numbersd in a list
def ex2():
    num = [1, 2, 4, 5, 6, 7, 8, 3, 4, 5, 12, 2, 2, 4, 1, 2, 4, 5, 6, 7]
    # num = (1, 2, 4, 5, 6, 7, 8, 3, 4, 5, 12, 2, 2, 4, 1, 2, 4, 5, 6, 7) # works with both sets and list
    counts = Counter(num)
    print(counts)

    top2 = counts.most_common(2)
    print(top2)


if __name__ == '__main__':
    ex2()
