def additionCarte(carte):
    carte=str(carte)
    if len(carte) == 3:
        if carte[0] == "1":
            return 10+int(carte[2])
        else:
            return 10+int(carte[0])
    else:
        return int(carte[0])+int(carte[1])


for i in range(2,10):
    a=str(i)+"10"
    print(a)
    print(additionCarte(a))
    print("---------------")