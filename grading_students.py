#!/bin/python3

import os

"""
HackerLand University has the following grading policy:
    - Every student receives a grade in the inclusive range from to.
    - Any grade less than 40 is a failing grade
Sam is a professor at the university and likes to round each student's grade according to these rules:
    - If the difference between the grade and the next multiple of 5 is less than 3, round up to the next multiple of 5.
    - If the value of is less than 38, no rounding occurs as the result will still be a failing grade.
"""


def gradingStudents(grades):
    for i, grade in enumerate(grades):
        if grade < 38:
            continue
        rounded_grade = grade
        while rounded_grade % 5 != 0:
            rounded_grade += 1
        if rounded_grade - grade < 3:
            grades[i] = rounded_grade
    return grades


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
