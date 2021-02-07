from random import randint

cards = ["a", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k"]
cards = [card for card in cards for i in range(0,4)]

def clear():
    print("\033[H\033[J", end="")

def deal():
    newCards = cards
    hands = [[], []]
    for _ in range(int(len(newCards) / 2 - 1)):
        hands[0].append(newCards.pop(randint(0, len(newCards) - 1)))
        hands[1].append(newCards.pop(randint(0, len(newCards) - 1)))
    return hands

players = deal()

def testInput(player):
    player = 0 if player < 0 else 1 if player > 1 else player
    def test(e):
        return e in players[player]
    return test

def createInput(startText, inputText, func = lambda e: True):
    while True:
        print(startText)
        val = input(inputText)
        clear()
        if func(val):
            return val

def sortList(e):
    key = {"a": 1, "1": 2, "2": 3, "3": 4, "4": 5, "5": 6, "6": 7, "7": 8, "8": 9, "9": 10,
    "10": 11, "j": 12, "q": 13, "k": 14}
    return key[e]

clear()
while True:
    players[0].sort(key=sortList)
    players[1].sort(key=sortList)

    playerOneChoice = createInput("Player 1. This is your deck {}".format(players[0]), "Please pick a card: ", func=testInput(0))
    playerTwoChoice = createInput("Player 2. This is your deck {}".format(players[1]), "Please pick a card: ", func=testInput(1))

    if playerOneChoice == playerTwoChoice:
        print("Snap!")
        break

    players[0].remove(playerOneChoice)
    players[1].remove(playerTwoChoice)