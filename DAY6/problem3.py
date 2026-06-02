
# Task 4  Count Conditions

# Using the same array find
import numpy as np
arr = np.random.randint(50,150,10)
a = (arr % 2 == 0).sum()
print(a)
b = (arr % 2 != 0).sum()
print(b)
c = avg = arr.mean()
print(c)
d = (arr > avg).sum()
print(d)

#perform properties on random integers to get meaningful insight from data 
