import pandas as pd
# df = {"Name":["Aman","Riya","Karan","Sneha"],
#       "Maths":[85,78,92,88],
#       "Science":[90,82,87,95],
#       "English":[88,80,91,89]
#       } 
# a = pd.DataFrame(df)
# print(a)

#Using EDA processes to check framed dataframe
# b = a.info()
# print(b)
# b1= a.describe()
# print(b1)     

# now we can store the data and frame that data by using python library

# df1 = [['Ajay',45,"good"],
#        ['Mohit',65,"bad"],
#        ['Manjeet',23,"good"]]
# b = pd.DataFrame(df1)
# print(b)
# when we frame the above data we can see is in thr name of indices which means  when we have to store data using list of list which means we have to specify the column names by its self 
#so we can take the above example and frame it with column names to make it more understanding 


df2 = [['Ajay',45,"good"],
       ['Mohit',65,"bad"],
       ['Manjeet',23,"good"]]
column_names = ["Names","Age","Quality"]
b1 = pd.DataFrame(df2,columns=column_names)
print(b1)
b2=b1.describe()
print(b2)# using properties
b2 = b1.info()
print(b2)