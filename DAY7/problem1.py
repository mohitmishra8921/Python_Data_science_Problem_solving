#DAY 7 first problem solving question
# Question 1 
string1 = "programming"
for ch in string1:
    if string1.count(ch)==1:
        print(f"First non repeating character is :\n",ch)
        break

#Question 2
list1 = [10, 5, 20, 8, 15]
largest = 0 
smallest = 0
for i in list1:
    if i > largest:
        largest = i
print(f"Largest element in the unsorted list:\n{largest}")