#DAY 7 first problem solving question 
string1 = "programming"
for ch in string1:
    if string1.count(ch)==1:
        print(f"First non repeating character is :\n",ch)
        break