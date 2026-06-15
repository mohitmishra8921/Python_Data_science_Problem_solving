import pandas as pd

students = {
    "Name": [
        "Aman", "Riya", "Karan", "Neha", "Mohit", "Raju", "Sejal", "Sneha", "Pranjal", "Geeta",
        "Rahul", "Anjali", "Vikram", "Pooja", "Amit", "Sonia", "Deepak", "Kiran", "Arjun", "Divya",
        "Rohan", "Megha", "Aditya", "Tanvi", "Yash", "Isha", "Kunwar", "Ridhima", "Vivek", "Preeti"
    ],
    "Math": [
        78, 90, 85, 92, 98, 45, 67, 98, 28, 90,
        82, 74, 91, 63, 88, 55, 79, 95, 42, 87,
        71, 93, 60, 84, 96, 38, 77, 89, 65, 81
    ],
    "Science": [
        80, 88, 79, 95, 78, 90, 85, 92, 98, 45,
        85, 91, 76, 84, 69, 88, 93, 72, 81, 90,
        64, 87, 78, 95, 83, 70, 89, 74, 92, 86
    ],
    "English": [
        75, 91, 83, 89, 80, 88, 79, 95, 78, 90,
        89, 82, 85, 78, 91, 74, 80, 87, 93, 69,
        88, 76, 92, 81, 85, 79, 90, 83, 77, 94
    ],
    "SST": [
        80, 88, 79, 95, 78, 90, 75, 91, 83, 89,
        77, 85, 90, 73, 84, 92, 68, 81, 89, 76,
        95, 82, 70, 88, 79, 84, 91, 67, 83, 90
    ],
    "Computer": [
        83, 89, 80, 88, 79, 95, 95, 78, 90, 75,
        92, 80, 87, 91, 76, 84, 96, 69, 85, 78,
        90, 93, 82, 74, 88, 91, 83, 79, 86, 95
    ]
}


students_marks= pd.DataFrame(students)

print(students_marks,
      "\n")# Today  I have taken a large dataset to work for analysis

# First aim to do EDA ON #  USE SOME FUNCTION WHICH HELP ME TO TO UNDERSTAND THE STUDENTS DATASET THAN I WILL ABLE TO GET SOME INSIGHTS FROM IT TO GET INSIGHTS
print("Get first five rows:\n")
print(students_marks.head())

print("Get last five rows:\n")
print(students_marks.tail())

print("Get description:\n")
print(students_marks.describe())

print("Get info of students:\n")
print(students_marks.info())

s = students_marks["Math"].astype("float64").copy()
print(s)
# i Challenge
# students whose Math marks are greater than 80.

maths_marks = ((students_marks["Math"] > 80) & (students_marks["SST"]>75)) 
result = students_marks[maths_marks]

print(result)
a = result.sort_values(["Math","Science","English","SST","Computer"],ascending= False)
print(a)
b= a[["English","Science","Math","SST","Computer"]]
print(b)

b.reset_index(drop = True,inplace= True)
print(b)
print(b.rename(columns={"SST":"Sst"}))

print("Name of student which get maximum marks in  maths as well as the index of that studnet in maths column:\n",b["Math"].max(),b["Math"].argmax())

# print(students_marks)

# Min