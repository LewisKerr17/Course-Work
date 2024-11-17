import random
import csv

userScore = 0
userName = input('Name: ')

with open('Python\scores.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

print("I'm thinking of a number between 1 and 10, guess it")

while True:

    numberToGuess = random.randint(1,10)
    playCount = 0

    
    while playCount < 3:
        try:
            userGuess = int(input(f"Guess #{playCount + 1}: "))
            playCount += 1

            if (userGuess == numberToGuess):
                print("Well done, you got it")

                if (playCount == 1):        
                    userScore += 10
                elif (playCount == 2):
                    userScore += 5
                else:
                    userScore += 3
                break
            
            elif (userGuess < numberToGuess):
                print("Too low")
            else:
                print("Too high")
        except ValueError:
            print("Please enter a valid number")

    if (playCount >= 3 and userGuess != numberToGuess):
        print("You've ran out of guesses, the number was: " + str(numberToGuess))

        userReplay = (input("Play again? (Y/N): "))
        if (userReplay.upper() != "Y"):
            print("End of Game") 
            break 

    if (userGuess == numberToGuess):
        with open('Python\scores.csv', 'a') as csvfile:
            csvfile.write('\n' + userName + ', ' + str(userScore))
        break