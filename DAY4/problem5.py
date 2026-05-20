import numpy as np

marks = np.array([45, 67, 82, 90, 55, 38, 76])# my todays concept is about filtering of students marks
mask = marks>50
print("The marks of student which have passed the exams are :\n",marks[mask])# These were the studnets from the current array which i have created using numpy array and filter marks of those students which are passed in the exams with the use of boolean mssking
