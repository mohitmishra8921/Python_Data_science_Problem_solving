#Problem solving for the day 5
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
common_list = []
for i in list1:
    if i in list2:
        common_list.append(i)
print(common_list)

#Problem 2 of dayt 5
string1 = "numpy"

freq = {}

for ch in string1:

    if ch in freq:
        freq[ch] += 1

    else:
        freq[ch] = 1

print(freq)