import numpy as np
arr = np.array([1,2,3,4,5,6])

arr[arr>3]=100

print(arr)#Using boolean masking to replace some values in the numpy array
