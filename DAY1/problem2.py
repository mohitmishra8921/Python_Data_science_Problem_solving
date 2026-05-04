import numpy as np
arr1 = np.array([1,2,3,4,5])
print("1D array using numpy in python:\n",arr1)
print('')
arr2 = np.array([[2,4,6],[3,5,7]])
print("2D array using numpy in python:\n",arr2)
# now we use propertues of numpy to check the properties of numpy areays created by us 
a = arr1.shape
print(a)

b = arr2.size #tells total number of elements in a array
print(b)

a1 = arr1.ndim # it tells us that row or columns in an array
print(a1)

a2 = arr1.dtype 
print(a2)


