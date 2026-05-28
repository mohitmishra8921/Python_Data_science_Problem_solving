import numpy as np
# Today apart from vectorisation and boolean masking as well as from indexing today iam going to perform one more important property of numpy fetaure that is "Broadcasing"
arr = np.array([1,2,3,4,5])
broadcasting = arr + 10
print(broadcasting)

#Solving best example of broadcasting
data = np.array([[10, 20, 30],
                 [15, 25, 35],
                 [20, 30, 40],
                 [25, 35, 45],
                 [30, 40, 50]])
# Calculating mean and standard deviation 
mean = data.mean(axis=0)
std = data.std(axis=0)

# Normalizing the data using broadcasting
normalised_data = (data-mean)/std
print(normalised_data)

