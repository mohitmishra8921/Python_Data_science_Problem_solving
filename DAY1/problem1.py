list1 = [1,2,2,3,3,3]
dict1 = {}
count = 0
for i in list1:
    if i in dict1:
       dict1[i] = dict1[i] + 1
    else:
        dict1[i] = 1
for key, value in dict1.items():
  print(key, "->", value)

       

        

    
    
        

