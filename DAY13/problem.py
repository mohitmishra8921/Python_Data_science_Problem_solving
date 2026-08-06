
#First task of day 13 count words in a string
# sentence = "data science is fun and data science is powerful".split()
# count = 0

# for ch in sentence:
#     count+=1
# print(count)


# #Second task of day 13 to find the unique word in a string
# sentence = "data science is fun and data science is powerful".split()
# for ch in sentence:
#    if sentence.count(ch) == 1:
#         print(ch)
    
    

# my_info = "Hello my name is mohit kumar mishra "

# file = open ("Basic.txt","w")
# file.write(my_info)
# file.close()


# my_info = "Hello my name is mohit kumar mishra "

students = [
    "Amit Kumar, 20, Delhi, amit@example.com",
    "Sneha Gupta, 21, Pune, sneha@example.com",
    "Rohan Singh, 22, Bangalore, rohan@example.com",
    "Anjali Mehta, 20, Chennai, anjali@example.com"
]

with open("students.txt", "w") as f:
    for student in students:
        f.write(student + "\n")

