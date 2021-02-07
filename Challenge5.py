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

class InputTesters:
    @staticmethod
    def isDate(e):
        try:
            e = e.split("/")
        except:
            return False
        else:
            if len(e) != 3:
                return False
            for i in e:
                if not isInt(i):
                    return False
            return True

    @staticmethod
    def toDate(e):
        return list(map(int, e.split("/")))

clear()
today = createInput("What is the date today?", "", func=InputTesters.isDate, effect=InputTesters.toDate)
birth = createInput("What date were you born?", "", func=InputTesters.isDate, effect=InputTesters.toDate)

years = today[2] - birth[2] - 1

if today[0] > birth[0]:
    years += 1
elif today[0] == birth[0]:
    if today[1] >= birth[1]:
        years += 1

print("You are {} years old".format(years))