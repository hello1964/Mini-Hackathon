def convertTimeToStandard(time):
    timeList = time.split(":")
    timeList = list(map(int, timeList))
    pm = False

    if timeList[0] > 12:
        timeList[0] -= 12
        pm = True
    return "{}:{} {}".format(timeList[0], timeList[1], "PM" if pm else "AM")

print(convertTimeToStandard("13:59"))
print(convertTimeToStandard("6:47"))