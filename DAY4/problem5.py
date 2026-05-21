#TASK 1 
import numpy as np

marks = np.array([45, 67, 82, 90, 55, 38, 76])# my todays concept is about filtering of students marks
mask = marks>75
print("The marks of student which have passed the exams are :\n",marks[mask])# These were the studnets from the current array which i have created using numpy array and filter marks of those students which are passed in the exams with the use of boolean mssking

#TASK2
mask = marks<50
print("The marks of student which have failed the exams are :\n",marks[mask])
#Marks of students which failed in the exam

#TASK3
#Now we add grace marks in the array of using vectorisation in array
marks1 = marks + 5
print(marks1)

#TASK4
# marks[marks<40]=-1 #last task of day replace -1 to show whiuch of the students are failed in the exam
# print(marks)


#Now its time to do bonus challenge of day4

#1) First i will find the average marks of total marks of student
#2) Second i will find the highest marks in the marks of students
#3) Third i will find the lowest marks in the array of marks of student

average_marks = marks.mean()
print("Average marks of the students are:\n",average_marks)

highest_marks = marks.max()
print("Highest marks of the students are:\n",highest_marks)

lowest_marks = marks.min()
print("Lowest marks of the students are:\n",lowest_marks)


