import numpy as np

marks = np.array([78,45,90,66,84,39,72,91,58,88])

grades = []

for mark in marks:
    if mark>=85:
        grades.append('A')
    elif mark>=70:
        grades.append('B')
    elif mark>=50:
        grades.append('C')
    else:
        grades.append('F')
print(grades)