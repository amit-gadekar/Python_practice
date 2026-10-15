from game_data import data
from art import logo,vs,gameover
import random

choiceA  = " "
choiceB = " "
user_score = 0
userGuess = True

#Retrieve data from list
def getData():
    return random.choice(data)

#Compare user choice and validate
def displayResults(choiceA, choiceB, userChoice):
    global user_score,userGuess
    if userChoice == 'a' :
        if choiceA['follower_count'] > choiceB['follower_count']:
            userGuess = True
            return userGuess
        else :
            userGuess = False
            return userGuess
           
    else:
        if choiceB['follower_count'] > choiceA['follower_count']:
            userGuess = True
            return userGuess
        else :
            userGuess = False
            return userGuess

def gameOver(user_score: int):
    print(gameover)
    print(f"Sorry..!!That's wrong.Game Over. Your Final Score is: {user_score}")

def main():
    global choiceA, choiceB,user_score,userGuess
    print(logo)
    if user_score == 0:
        choiceA = getData()
    if user_score > 0:
        print(f"Your guess is correct..!! Your Current Score is: {user_score}")

    print(f"Compare A:=> {choiceA['name']}, {choiceA['description']}, from {choiceA['country']}")
    print(vs)
    choiceB = getData()
    print(f"Against B:=>{choiceB['name']}, {choiceB['description']}, from {choiceB['country']}")
    userChoice = input("\nWho do you think has more followers on Instagram account? Type 'A' or 'B':").lower()

    if userChoice == 'a' or userChoice == 'b':
        result = displayResults(choiceA, choiceB, userChoice)
        if result == True :
           user_score += 1
           print(result, user_score)
           choiceA = choiceB
        else:
           gameOver(user_score)

    else:
        gameOver(user_score)





while userGuess == True :
    main()