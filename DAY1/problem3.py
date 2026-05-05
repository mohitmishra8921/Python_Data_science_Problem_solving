import pandas as pd
df = {"Name":["Aman","Riya","Karan","Sneha"],
      "Maths":[85,78,92,88],
      "Science":[90,82,87,95],
      "English":[88,80,91,89]
      } 
a = pd.DataFrame(df)
print(a)

#Using EDA processes to check framed dataframe
b = a.info()
print(b)
b1= a.describe()
print(b1)         