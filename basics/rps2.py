import random
choices = ["rock", "paper", "scissors"]
print("WELCOME TO THE ROCK - PAPER - SCISSORS GAME!")
while True:
    try:
        player = input("Please choose between rock, paper and scissors: ").strip().lower()
        if player not in choices:
            print("Incorrect choice, please try again.")
        else:
            computer = random.choice(choices)
            print("The computer chose:", computer)
            if player == "rock" and computer == "scissors" or player == "paper" and computer == "rock" or player == "scissors" and computer == "paper":
                print("YAAAAAAY YOU WON!!!")
            elif player == computer:
                print("DRAW..")
            else:
                print("LOOOOSER")
            again = input("Do you want to play again? (yes/no) ").strip().lower()
            if again == "no":
                print("Thank you for playing my game. See you later!")
                break    
    except:
        print("Something went wrong.. please try again")
                
         
                
