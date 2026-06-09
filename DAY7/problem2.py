import numpy as np

arr = np.array([78, 45, 90, 66, 84, 39, 72, 91, 58, 88])
a = np.sort(arr)
print(a)

b =a[-3:]
print(f"First three highest marks:\n{b}")
c = []
for i in b[::-1]:
        c.append(i)
print("First three highest marks:\n",c)


