from math import floor

def decimalOrInt(num1, num2):
    if num2 > num1:
        return "decimal"
    ans = num1 / num2
    if ans == floor(ans):
        return "integer"
    else:
        return "decimal"

print(decimalOrInt(8, 3))
print(decimalOrInt(8, 4))