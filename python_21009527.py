# Ashwin Vigneswaran (21009527)

from random import choice # generates randomized values

from collections import Counter

# Defining the checkup function that is used to check the placement of the fruits and notify the user
def checkup(first_check, second_check):
    first_checkup = "The correct fruits that are in the correct place are: " + str(first_check)
    second_checkup = "The correct fruits that are in the wrong place are: " + str(second_check)
    return print(first_checkup + "\n" + second_checkup + "\n")


EstimationCounter = 1 # EstimationCounter set to 1 (used to count attempts user takes to get final correct answer)
Start = "YES"
Fruits = ["strawberry", "mango", "watermelon", "avocado"] # List to store the fruits used in the game

# Prints the welcome message and the rules for Ashwin's Mastermind Game
print("Greetings!")
print("Welcome To Ashwin's Mastermind Game!")
print()
print("The rules are simple:")
print()
print("1) 4 choices of fruit will be picked randomly.")
print("2) You must correctly guess the order of these 4 fruits.")
print("3) The fruits can repeat more than once!")
print("4) The fruits are: strawberry, mango, watermelon, and avocado.")
print("5) You have to submit a guess once each time, until the 4th try.")
print("6) You will be notified on the correct and wrong placements after the 4th try, then you can retry.")
print("7) Good luck and have fun guessing!")

# This is what will happen when the game starts (code is run)
while Start == "YES":
    print()

    Answer = [] # Creates an empty list for Answer
    for i in range(4):
        Answer.append(choice(Fruits)) # Computer generates four random fruits from the list

    # print(str(Answer)) Use this is if you want the answer straight away for testing purposes

    Win = False # Win is set to false
    while True: # (while) All is set to 0 and no register yet until the user starts guessing
        Assessment = False
        Correct = 0
        Wrong = 0
        while not Assessment:
            Assessment = True

            Estimate = [] # This list is used to store the user's input each time
            for i in range(0, 4):
                Estimate.append(str(input("Please enter your guess: ")).lower().strip()) # User enters their fruit guess
                if len(Estimate) != 0: # If length is not 0, it will show the user's guess of fruit
                    print("Your estimation(s):" + str(Estimate) + "\n")
                if Estimate[i] not in Fruits: # validation check to see if fruits are in the list or not
                    print("That is not in the list! Do not leave empty spaces, and please enter a fruit from the list. Try again.", "\n")
                    Assessment = False
                    break

        Correct = sum(1 for x,y in zip(Answer, Estimate) if x == y) # Used to check correct placements with the random list x (up and down)
        Wrong = sum((Counter(Answer) & Counter(Estimate)).values()) - Correct # Calculates the wrong placements

        if Correct == 4: # If all correct, win is set to true
            Win = True
            break
        else: # If wrong, user is notified on checkup (placements) and counter is increased
            EstimationCounter += 1
            checkup(Correct, Wrong)

    print()

    # When user wins, they are told the answer and that they win
    if Win:
        print("Congratulations! The answer is " + str(Answer) + "." + " You got it right, you win! :)")

    # Displays how many attempts it took
    print("This is how many attempts it took for you to get the answer: " + str(EstimationCounter))

    # Prompts user if they wanna play again, and converts 'yes' or 'no' to uppercase.
    Start = input("That was fun! Should we play again? (Enter 'Yes' or 'No'):" + " ").upper()

    while Start != "YES" and Start != "NO": # validation check for appropriate words
        print("You are only allowed to answer with a 'Yes' or 'No'")
        Start = input("That was fun! Should we play again? (Enter 'Yes' or 'No'):" + " ").upper()

    if Start == "NO": # If user enters 'no', game stops
        print()
        print("Thank you for playing Ashwin's Mastermind Game!")

    if Start == "YES": # If user enters 'yes', game restarts
        print()
        print("Welcome To Ashwin's Mastermind Game!")
        print()
        print("The rules are easy:")
        print()
        print("1) 4 choices of fruit will be picked randomly.")
        print("2) You must correctly guess the order of these 4 fruits.")
        print("3) The fruits can repeat more than once!")
        print("4) The fruits are: strawberry, mango, watermelon, and avocado.")
        print("5) You have to submit a guess once each time, until the 4th try.")
        print("6) You will be notified on the correct and wrong placements after the 4th try, then you can retry.")
        print("7) Good luck and have fun guessing!")
        print()
        print("Here we go again!")

# The End!