#Rock Paper Scissors Game but using Fire Grass Water
#Best out of 3 wins

import random

#Take in user input:
numRounds = 1
userWins = 0
computerWins = 0

#Determine round:
while numRounds != 4:
    print(f"Round {numRounds}")
    userChoice = input("Enter your choice of Fire, Grass or Water:  ")
    if userChoice == "Fire" or userChoice == "Grass" or userChoice == "Water":
        # Make a list the random will take from & make the choice:
        elementList = ["Fire", "Grass", "Water"]
        randomChoice = random.choice(elementList)

        # Print choices
        print(f"You chose: {userChoice}")
        print(f"Opponent chose: {randomChoice}")

        # Using if statements to choose winner:
        if userChoice == randomChoice:
            print("Tie.")
        #User chose Fire
        elif userChoice == "Fire":
            if randomChoice == "Grass":
                print("You win!")
                userWins += 1
            elif randomChoice == "Water":
                print("You lose!")
                computerWins += 1
        #User chose Water
        elif userChoice == "Water":
            if randomChoice == "Fire":
                print("You win!")
                userWins += 1
            elif randomChoice == "Grass":
                print("You lose!")
                computerWins += 1
        #User chose Grass
        elif userChoice == "Grass":
            if randomChoice == "Water":
                print("You win!")
                userWins += 1
            elif randomChoice == "Fire":
                print("You lose!")
                computerWins += 1

    else:
        print("Invalid input. Try again.")
        exit()

    numRounds += 1

if userWins > computerWins:
    print("You won the set!")
elif userWins < computerWins:
    print("You lost the set!")
elif userWins == computerWins:
    print("Tied set!")

