#Problemsolving  1st of day 6
num = [1,2,3,5,6]
for i in num:
    if i + 1 not in num:
        print(f"Missing numbers in the list:\n{i + 1}")
