import random
import csv

userScore = 0
userName = input('Name: ')
fieldNames = ['Name', 'Score']
highScoresWithName = []
highScoresInt = []

with open('Python/scores.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=fieldNames)
    next(reader)
    for row in reader:
        storedScore = int(row['Score'])
        storedName = row['Name']
        highScoresWithName.append((storedName, storedScore))
        highScoresInt.append(storedScore)

highScoresWithName.sort(reverse=True)
print('Top 5 scores')
print(highScoresWithName[0:5])

print("I'm thinking of a number between 1 and 10, guess it")

while True:

    numberToGuess = random.randint(1,10)
    playCount = 0

    
    while playCount < 3:
        try:
            userGuess = int(input(f'Guess #{playCount + 1}: '))
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
        with open('Python/scores.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldNames)

            if len(highScoresInt) < 5 or userScore > min(highScoresInt[0:5]):
                with open('Python/scores.csv', 'a', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
                    writer.writerow({'Name': userName, 'Score': userScore})

        break