#Question 1
nums = [1,2,3,2,4,5,4]
nums_value = []
for i in nums:
   if  nums.count(i)>1:
       if i not in nums_value:
           nums_value.append(i)
print(f"Duplicate values in the list:\n{nums_value}")
