import numpy as np

arr = np.array([2,5,8,1,9,3,10])
mask1 = arr>5
mask2 = arr<5
print(arr[mask1])#This is for greater than 5
print(arr[mask2])#I can also print less than 5 by reversing comparison operator from greater than to less than in the same method

#It is one of the famous method masking as well as there is also one of the method like this but that use for indexing multiple elements at one time by this feature of numpy 

arr = np.array([2,5,8,1,9,3,10])

mask3 = (arr>2) & (arr<9) #Here one thing need to be kept in my mind that in numpy is we have to do boolean masking with two conditions than we have to seperate them with brackets first than use sign of and / or operator between them
print(arr[mask3])