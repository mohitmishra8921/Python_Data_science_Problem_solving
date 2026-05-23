#Problem solving for the day 5
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
common_list = []
for i in list1:
    if i in list2:
        common_list.append(i)
print(common_list)