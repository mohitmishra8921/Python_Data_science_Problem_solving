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
