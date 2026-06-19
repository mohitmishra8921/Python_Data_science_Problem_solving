#Question 1
nums = [4, 1, 2, 1, 2]
numss = []
for i in nums:
    if nums.count(i)==1:
        numss.append(i)
print("The number in the list which appears only once in the list:\n",numss)

#Question 2
nums = [10, 20, 30, 40, 50]
reverse_nums = []
for i in nums[::-1]:
    reverse_nums.append(i)
print("Reverse of original list:\n",reverse_nums)

#Question 3

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = []
for i in list1:
    if i in list2:
        common_elements.append(i)
print("Common elements between both list:\n",common_elements)

#Question 4 
nums = [12, 15, 8, 21, 30, 17]
even = []
odd = []
for i in nums :
    if i %2==0 :
        even.append(i)
    else:
        odd.append(i)
        
print("Even numbers from the list:\n",even)
print("Odd numbers from the list:\n",odd)


