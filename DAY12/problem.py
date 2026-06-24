nums = [5, 10, 15, 20]
num = []
for i in nums :
    num.append(i*2)
print(num)


words = ["apple", "banana", "apple", "orange", "banana", "apple"]

dicti = {}
for ch in words :
    
    if ch in dicti:
        dicti[ch]+=1
    else:
        dicti[ch] = 1
for key,values in dicti.items():
    print("Frequency of items in the list:\n",key,values)

