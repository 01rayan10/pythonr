import random
print("Welcome to the Rock Paper Scissors game.")
print("Please choose between rock, paper and scissors:")
choices = ["rock", "paper", "scissors"]
while True:
    player = input("Your choice: ").strip().lower()
    if player not in choices:
        print(f"Incorrect choice. Please choose rock or paper or scissors. You chose: {player}")
        continue
    computer = random.choice(choices)
    print(f"The computer chose: {computer}")
    if player == computer:
        print("Draw.")
    elif player == "rock" and computer == "scissors" or\
         player == "paper" and computer == "rock" or\
         player == "scissors" and computer == "paper":
        print("YAAYY YOU WON!!!")
    else:
        print("You lost :( BUT.. You can play again and maybe win this time!)")
    pa = input("Do you want to play again? (yes/no): ")
    if pa == "no":
        print("Thank you for playing with me :)")
        break