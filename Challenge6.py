from math import floor

def inverseRound(number):
    decimal = number - floor(number)
    if decimal < 0.5:
        number = floor(number) + 1
    else:
        number = floor(number)
    return number

print(inverseRound(9.4))
print(inverseRound(9.6))