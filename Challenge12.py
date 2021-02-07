def alphaIndex(string):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    listOfIndexes = []
    string.lower()

    for i in string:
        if i in alpha:
            listOfIndexes.append(alpha.index(i) + 1)
    
    listOfIndexes = list(map(str, listOfIndexes))

    return " ".join(listOfIndexes).strip()

print(alphaIndex("abcxyz"))