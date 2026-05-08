import numpy as  np
arr = np.array([10,20,30,40,50,60])
print(arr)
a = arr[1]# This is the most simplest way of indexing or accessing single elements from the the array 
print(a)
# we can also access elements from the array in the form of slicing to access the array 
a1 = arr[0:5]
print(a1)

b1= arr[0:4:2] #Another way of accesssing elements in a array
print(b1)

#This properties looks more comfortable while using them on 2D or 3D arrays to acces elements of rows and columns
arr1 = np.array([[10,20,30],
               [40,50,60]])
c1 =arr1[1,2]#here first number use for second row because indexing starts from 0 and 2 for third columns
print("Second row third column element is :\n",c1)

d1 = arr[::-1]# use for reversing the array
print(d1)

arr[2] = 100 #This make sure list are mutable and it returns view here bcz it changes the original array
print(arr)