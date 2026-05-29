#Problemsolving  1st of day 6
num = [1,2,3,5,6]
for i in num:
    if i + 1 not in num:
        print(f"Missing numbers in the list:\n{i + 1}")

#Problem 2 
sentence = "data science is fun and data is powerful".split()

freq = {}

for word in sentence:

    if word in freq:
        freq[word] += 1

    else:
        freq[word] = 1

print(freq)