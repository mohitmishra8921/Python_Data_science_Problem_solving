import numpy as np

arr = np.array([2,5,8,1,9,3,10])
mask = arr>5
print(arr[mask])#It is one of the famous method masking as well as there is also one of the method like this but that use for indexing multiple elements at one time by this feature of numpy 