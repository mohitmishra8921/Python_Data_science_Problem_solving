list1 = [4,5,1,2,0,4,1,2]

for i in list1:
    if list1.count(i)==1:
        print(f"First non repeating number in the list is :\n {i}")
        break
