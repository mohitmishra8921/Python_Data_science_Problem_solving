#DAY 7 first problem solving question
# Question 1 
string1 = "programming"
for ch in string1:
    if string1.count(ch)==1:
        print(f"First non repeating character is :\n",ch)
        break

#Question 2
# list1 = [10, 5, 20, 8, 15]
# largest = 0 
# for i in list1:
#     if i > largest:
#         largest = i
# print(f"Largest element in the unsorted list:\n{largest}")
#Question 3 
#Is it same before just one chng that we have to find secodn lrgest in th elist without using sorting 


list1 = [10, 5, 20, 8, 15]

largest = 0
second_largest = 0

for i in list1:

    if i > largest:
        second_largest = largest
        largest = i

    elif i > second_largest:
        second_largest = i

print("Largest:", largest)
print("Second Largest:", second_largest)