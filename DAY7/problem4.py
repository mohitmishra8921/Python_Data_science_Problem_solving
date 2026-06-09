import numpy as np

sales = np.array([
    [120,140,130],
    [90,100,110],
    [200,180,190],
    [80,70,75]
])
total_sales = sales.sum(axis=0)#here each rows showed sales of each employee in three consecutive months and byu using sum funct with axis parametr i found total expenditure of there three months
print(total_sales)

#task 2 part 1 
highest_sale = total_sales.max()
print(highest_sale)
