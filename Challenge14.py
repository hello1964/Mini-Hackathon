def sumOfEven(*nums):
    return sum([i for i in nums if i % 2 == 0])

print(sumOfEven(67, 7, 8, 4))