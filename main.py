import random
import csv

print('Im thinking of a number between 1 and 10 - try and guess it.')

while True:

    numberToGuess = random.randint(1, 10)

    playCount = 0
    userScore = 0
    userGuess = prompt(f'Guess #{playCount + 1}: ')

    if userGuess == numberToGuess:
        print('You got it!')
        score += 10
        playCount += 1
    
    elif userGuess < numberToGuess:
        print('Too low')
        playCount += 1

    elif userGuess > numberToGuess:
        print('Too high')
        playCount+= 1
    

    if playCount >= 3:
        print(f'Ran out of guesses! The number was {numberToGuess}!')
    
