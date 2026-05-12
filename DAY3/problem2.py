import numpy as np
arr1 = np.array([[10,20,30],
               [40,50,60],
               [10,20,30],
               [40,50,60]])
#here we use simple proprties to change its shape as well as make 2d or 3d array into 1d array
a = arr1.reshape(2,6) # we can change shapes but need to to reminf one thing in my mind is no of elements must be same while giving new shape here 2*6 = 12 elements
print(a)
b = arr1.flatten()
print(b) #it is normally used for making 1d array