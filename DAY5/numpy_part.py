import numpy as np
marks = np.array([10,0,72,0,14,44,85])# It looks very easy for day 5 numpy part but when i strat doing this question i have learned two things one never name your file as module name before i saved my folder as numpy.py so it arises an attribute error
a = np.sort(marks)# Arrray comes in an ascending order
b = np.std(marks)#Standard deviation of above array mean meadian i had already done in previous practice questions 
c = np.unique(marks)#Get a list of elements whiich avoid duplicates

print(a)
print(b)
print(c)

#now one main thing i can replace any of the item in the array by using boolean masking property of numpy
marks[marks < 0] = 0
print(marks)
