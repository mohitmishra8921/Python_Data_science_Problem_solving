# Create a marks dataset for 5 students and perform analysis.

import numpy as np 
import pandas as pd
marks = np.array([[78,85,80],
                 [90,88,92],
                 [67,70,72],
                 [95,98,96],
                 [82,79,85]])
columns = ["Maths","Science","English"]
print(marks.shape)
df = pd.DataFrame(marks,columns=columns,index=["A","B","C","D","E"])
# print(df)
total = df.sum(axis=1)
print(total)

average = df.mean(axis=1)
print(average)
