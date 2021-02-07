def clear():
    print("\033[H\033[2J", end="")

def isInt(string: str):
    if "." in string:
        return False
    try:
        int(string)
    except:
        return False
    else:
        return True

def createInput(startText, inputText, func = lambda e: True, effect = lambda e: e):
    while True:
        print(startText)
        val = input(inputText)
        clear()
        if func(val):
            return effect(val)

def checkNumber(e):
    if isInt(e):
        return 10 >= int(e) >= 0
    return False

clear()
secretNumber = createInput("Player 2, please type a secret number between 0-10 for player 1 to guess", "", func=checkNumber, effect=int)

while True:
    if createInput("Player 1, guess the number", "", func=checkNumber, effect=int) == secretNumber:
        print("YOU WIN!")
        break