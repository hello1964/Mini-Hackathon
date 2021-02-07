def swap(str1, str2):
    def lengthSortFunc(val):
        return len(val)
    strs = [str1, str2]
    strs.sort(key=lengthSortFunc)
    if len(strs[0]) < len(strs[1]):
        strs[1] = strs[1][:len(strs[0])]
    skipped = True
    newStr1 = ""
    newStr2 = ""
    for p, i in enumerate(strs[0]):
        if not skipped:
            newStr1 += strs[1][p]
            newStr2 += strs[0][p]
            skipped = True
        else:
            newStr1 += strs[0][p]
            newStr2 += strs[1][p]
            skipped = False
    return (newStr1, newStr2)
    
print(swap("12931", "fdjsa"))