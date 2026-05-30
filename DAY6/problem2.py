#Todays problem of my block B part 
import numpy as np
arr = np.random.randint(1, 101, 15)#Shortcut feature of numpy to create random integers list of random integers
print(arr)
# a = sorted(arr)
# print(a)

#Some important features apply on list of random integers
a1 = arr.max()
print(f"Maximum integer among of all random integers:\n{a1}")
b1 = arr.min()
print(f"Minimum integer among of all random integers:\n{b1}")
c1 = arr.mean()
print(f"Average of random integers:\n{c1}")