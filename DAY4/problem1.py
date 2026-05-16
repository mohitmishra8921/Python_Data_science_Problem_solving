# list1 = [1,2,3,4,5,6,7,8]
# even_num = []
# for i in list1:
#     if i %2==0:
#         even_num.append(i)
# print("The even numbers from the list are :",even_num)

string1 = "data science"

vowels_count = {}

for ch in string1:
    if ch in "aeiou":

        if ch in vowels_count:
            vowels_count[ch] += 1

        else:
            vowels_count[ch] = 1

print(vowels_count)