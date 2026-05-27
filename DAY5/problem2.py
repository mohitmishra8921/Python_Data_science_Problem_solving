import numpy as np
#1st task
arr = np.array([12, 45, 67, 23, 89, 34, 90, 21])
mask = (arr>30) & (arr<80)
print(arr[mask])


a = arr.mean()#this was just used to complete the last task of this part means task task 3
print(a)

#2nd task (Thius task is used to find the numbers in array divide by zero using vectorisation to prevent use of control or looping statements)
b = arr%3
print(set(arr[b]))


#3rd task
mask1= arr>a # To find the numbers in array which is greater than the mean of the above elements of array 
print(arr[mask1])


#4th task 
#to replace all even numbvers with 0
# arr[arr%2==0]=0
# print(arr.copy())

#Mini project task
#marks of student mini project for data analyst
marks = np.array([78,45,90,66,84,39,72,91])
a = marks.max()#1toppr marks
print(f"Marks of toppr:\n{a}")
b = marks.argmax()#2 index of toprs marks
print(f"Index of topprs mask:\n{b}")

c = arr<40
print(f"marks of failed students:\n{arr[c]}")

d = arr>75
print(f"Marks of distinction student:\n{arr[d]}")

passed = marks>=40
print(f"No of students passed in exams :\n{passed}")

# In above step we got true for passe students in the terminal now by using one more function of numpy we count how many students pased the exam

print(f"No of studnets passed the exams:\n{passed.sum()}")

