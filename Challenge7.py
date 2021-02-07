import sys

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

def choices(textBefore: str, choices: list, endText: bool = False):

    def cmd(string: str):
        sys.stdout.write(string)

    def clearAmount(number: int, thisLine: bool = True):
        if thisLine:
            cmd("\033[K")
        for i in range(0, number):
            cmd("\033[F")
            cmd("\033[K")    

    choice = 0
    firstTime = True
    while choice < 1 or choice > len(choices):
        if not(firstTime):
            clearAmount(4 + len(choices))
        print(textBefore + (" What do you do?" if endText else ""))
        print("")
        for p, i in enumerate(choices):
            print("   [{}]{}".format(p + 1, i))
        print("")
        choice = input("Choice?")
        choice = int(choice) if isInt(choice) else 0
        firstTime = False
    clear()
    return choice - 1

def createInput(startText, inputText, func = lambda e: True, effect = lambda e: e):
    while True:
        print(startText)
        val = input(inputText)
        clear()
        if func(val):
            return effect(val)

def inputIsInt(e):
    return isInt(e)

def onlyLetters(e):
    for i in e:
        if i.lower() not in "abcdefghijklmnopqrstuvwxyz":
            return False
    return True

clear()
info = []
info.append(createInput("What is your first name?", "", func=onlyLetters))
info.append(createInput("What is your last name?", "", func=onlyLetters))
info.append(createInput("How old are you?", "", func=inputIsInt, effect=int))
info.append(True if choices("Are you married?", ["Yes", "No"]) == 0 else False)
info.append("m" if choices("What is your gender?", ["Male", "Female"]) == 0 else "f")

title = ""
if info[2] <= 18:
    title = "Ms" if info[4] == "f" else "Master"
elif info[4] == "f":
    if info[3]:
        title = "Mrs"
    else:
        title = "Miss"
else:
    title = "Mr"

msg = "Dear {} {} {}".format(title, info[0].title(), info[1].title())

print(msg)