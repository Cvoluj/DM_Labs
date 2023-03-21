import random
def Atitudes(firstDict, secondDict, women, men, MotherAndSon):


    for name, gender in firstDict.items():
        if gender == "w":
            women.add(name)
    for name, gender in secondDict.items():
        if gender == "w":
            women.add(name)
        else:
            men.add(name)

    NumOfmothers = random.randint(1, round(len([*men]) / 2))
    mothers = set(random.sample([*women], NumOfmothers))
    sons = set(random.sample([*men], round(len([*men]) / 2)))
    print(mothers)
    print(women)
    for k, (i, j) in enumerate(zip(mothers, sons)):
        if k == len(mothers) or k == len(sons):
            pass
        elif i not in MotherAndSon and j not in MotherAndSon:
            MotherAndSon.add((i, j))

    wifes = set(random.sample([*women], NumOfmothers))
    husbands = set(random.sample([*men], len([*men])))

    WifeHusband = set()
    for k, (i, j) in enumerate(zip(wifes, husbands)):
        if k == len(mothers) or k == len(sons):
            pass
        if i not in MotherAndSon and j not in MotherAndSon:
            WifeHusband.add((i, j))

    MotherInlaw = set()
    for (i, j), (l, f) in zip(MotherAndSon, WifeHusband):
        if j == f:
            MotherInlaw.add((i, l))
    # print(MotherAndSon)
    print("!!!Wife and husband\n", WifeHusband)
    print("!!!Mother in law\n", MotherInlaw)
    return WifeHusband, MotherInlaw