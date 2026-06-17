#Problem solving of day9
nums = [1, 2, 3, 5, 6]#finding missing number in the list 
for i in nums:
    if (i + 1 ) not in nums:
        print(f"The missing vaules in the sorted list:\n{i+1}")