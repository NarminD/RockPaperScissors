import random


def play():
    
    options = ["rock", "paper", "scissors"]
    while True: 

        user_choice = input("Enter one of the following - rock, paper or scissors: \nYou: ").lower() #making user's input lower case to match options 

        if user_choice not in options:
            print("Invalid choice.")
            continue 
        #"continue" will end current iteration, and restart the function. To exit function we would put "return" instead of "continue". If nothing entered, it will enter computer's choice and a result without the user's input   
  
        computer_choice = random.choice(options)

        print("Computer's choice: " + computer_choice)

        #below: new if statement   
        if user_choice == computer_choice:
            print("You tied!")
        elif (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "rock" and computer_choice == "scissors"): 
            print("You win!")
        else:
            print("You lose! Better luck next time.")

        continue_game = input("Do you want to continue the game? [yes or no]: ")
        if continue_game.lower() != "yes":
            break  
      
      
print("Let the game begin!")
play()



