def clear():
    print("\033[H\033[2J", end="")

clear()
name = input("What is your name? ")
clear()
location = input("Where do you live? ")
clear()
like = input("What do you like to do? ")
clear()

print("Hello, my name is {}, I live in the {}, and I like {}".format(name, location, like))