from random import randint

def clear():
    print("\033[H\033[J", end="")

player1 = 0
player2 = 0

def run(player, num):
    movement = randint(1, 6)
    player += movement
    
    if player % 10 == 0:
        print("Player {} landed on a snake and moved back to the start".format(num))
        player = 0
    elif player % 5 == 0:
        player += 9
        print("Player {} landed on a ladder and landed on space {}".format(num, 100 if player > 100 else player))
    else:
        print("Player {} landed on space {}".format(num, 100 if player > 100 else player))
    if player >= 100:
        print("Player {} wins!".format(num))
        return "end"
    return player

clear()
while True:
    player1 = run(player1, 1)
    if player1 == "end":
        break
    input("Press enter")
    clear()
    player1 = run(player2, 2)
    if player2 == "end":
        break
    input("Press enter")
    clear()