
#First task of day 13 count words in a string
sentence = "data science is fun and data science is powerful".split()
count = 0

for ch in sentence:
    count+=1
print(count)


#Second task of day 13 to find the unique word in a string
sentence = "data science is fun and data science is powerful".split()
for ch in sentence:
   if sentence.count(ch) == 1:
        print(ch)
    
    

