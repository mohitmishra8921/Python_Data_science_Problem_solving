while True:
    import random 

    def game_win(user,computer):
      if user == computer:
         return None
      #Snake vs water
      if user == "s" and computer == "w":
        return True
      if user == "w" and computer == "s":
         return False
    
      #Water vs gun 
      if user == "w" and computer == "g":
          return True
      if user == "g" and computer == "w":
         return False
    
     #Gun vs Snake
      if user == "g" and computer == "s":
        return True
      if user == "s" and computer == "g":
        return False
    

    rand_no = random.randint(1,3)
                         
    print("Computer's turn: Snake(s), Water (w), Gun (g)")

    if rand_no == 1:
      computer = "s"
    elif rand_no == 2:
     computer = "w"
    else:
     computer = "g"
    try:
         user = (input("Your turn: Snake(s), Water (w), Gun (g): ")).lower()
    except Exception as e:
            print(e) 
 
    result = game_win(user, computer) # Returns True if you win, False for lose, None for draw
    print(f"\nYou chose: {user}")
    print(f"\nComputer chose: {computer}")
 
    if result is None:
        print("Its a draw!")
 
    elif(result):
        print("You win!")
    else:
        print("You lose!")
 


    
       
