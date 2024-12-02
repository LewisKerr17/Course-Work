import math

displayNum = []
hexNums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

userNum = int(input('\nDecimal Number: '))
userConversionChoice = input('Converting to Binary or Hex? (Binary / Hex): ')
userConversionChoice.lower()

def binaryConversion():
    global userNum
    while userNum >= 1:
        displayNum.append(userNum % 2)
        print(f'{userNum} ÷ 2 = {math.floor(userNum / 2)}, remainder {userNum % 2}')
        userNum = math.floor(userNum / 2)
    print(displayNum[::-1])


def hexConversion():
    global userNum
    while userNum >= 1:
        displayNum.append(hexNums[userNum % 16])
        print(f'{userNum} ÷ 16 = {math.floor(userNum / 16)}, remainder {userNum % 16}')
        userNum = math.floor(userNum / 16)
    print(displayNum[::-1])

def userChoice():
    if userConversionChoice == 'binary':
        binaryConversion()
    if userConversionChoice == 'hex':
        hexConversion()

userChoice()


