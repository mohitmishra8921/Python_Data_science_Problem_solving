import numpy as np

sales = np.array([
    [120,140,130],
    [90,100,110],
    [200,180,190],
    [80,70,75]
])
print(sales.sum(axis=1))#here each rows showed sales of each employee in three consecutive months and byu using sum funct with axis parametr i found total expenditure of there three months