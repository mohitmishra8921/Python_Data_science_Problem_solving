import numpy as np 
array =np.array([32, 34, 31, 29, 35, 36, 33])
a = array.mean()#Use to find the average temperature of given following temp of weaks
print("The average temp of the week is :",a)
b = array.max()#to calculate the maximum temp on any day of the week 
print("Maximum temp of week",b)
c = array.min()#minimum temp of the week 
print("Minimum temp of week",c)

#my todays work on this problem of temperature of the whole week is to vectorized it by add two degrees in each temp 
d = array + 2 # here in numpy we simply add 2 to each day temp without creatong another aaray without using loops due to which it becomes memory costly
print(d)
