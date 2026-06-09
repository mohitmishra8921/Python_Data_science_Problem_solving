import numpy as np

sales = np.array([
    [120,140,130],
    [90,100,110],
    [200,180,190],
    [80,70,75]
])
total_sales = sales.sum(axis=1)#here each rows showed sales of each employee in three consecutive months and byu using sum funct with axis parametr i found total expenditure of there three months
print("Total sales of each employee in three consecutive months:\n",total_sales)

#task 2 part 1 
highest_sale = total_sales.max()
print("Sale of that employee which makes highest sale:\n",highest_sale)
#task2 part2 
highest_sale_index = total_sales.argmax()
print("Index of that employee in the sales that which makes highest sale:\n",highest_sale_index)

#Now iam going to to make performance analysis on the basis of sales analysis
performance_analysis = []
for i in total_sales:
    if i>=500:
        performance_analysis.append("Star")
    elif 350<i<499:
        performance_analysis.append("Good")
    elif 250<349:
        performance_analysis.append("Average")
    else:
        performance_analysis.append("Need improvement")
print("Performance of each employee according to their total sales:\n",performance_analysis)


