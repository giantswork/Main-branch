# Rock, Paper, Scissors
import random
import math

def rnd():
    opt = ["Rock", "Paper", "Scissors"]
    prompt = """
    [0] Rock
    [1] Paper
    [2] Scissors
    
    Choose your weapon: \n"""

    inp = -1
    while not (0 <= inp <= 2):
        try:
            inp = int(input(prompt))
            if inp < 0 or inp > 2:
                raise TypeError("Invalid input")
        except TypeError:
            print("Invalid input, try again\n")
        except ValueError:
            print("Invalid input, try again\n")

    comp = math.ceil(random.random() * len(opt)) - 1

    if inp == 0 and comp == 2:
        score = 1
    elif inp == 1 and comp == 0:
        score = 1
    elif inp == 2 and comp == 1:
        score = 1
    elif inp == comp:
        score = 0
    else:
        score = -1
    print("You chose " + opt[inp] + " and the computer chose " + opt[comp] + "\n")
    return score


def scoreFunction():
    player = input("Type in your name: \n")
    prompt = "Choose the number of rounds to play (value must be uneven): \n"
    inp = 0
    while inp % 2 == 0:
        try:
            inp = int(input(prompt))
            if inp % 2 == 0:
                raise TypeError("Invalid input")
        except TypeError:
            print("Invalid input, try again\n")
        except ValueError:
            print("Invalid input, try again\n")
    winScore = inp / 2 + 0.5
    yourScore = 0
    compScore = 0
    while yourScore < winScore and compScore < winScore:
        roundScore = rnd()
        if roundScore == 1:
            print("You have won this round\n")
            yourScore += 1
        elif roundScore == -1:
            print("The computer has won this round\n")
            compScore += 1
        else:
            print("Neither has won this round\n")
        print("Current score is " + player + ": " + str(yourScore) + " - Computer: " + str(compScore) + " (best of " + str(inp) + ")\n")
    if yourScore == winScore:
        print("You have WON the game\n")
    else:
        print("You have LOST the game\n")
    newGame = input("Press [Y] to start a new game, press any key to close the screen\n")
    if newGame.lower() == "y":
        scoreFunction()


scoreFunction()