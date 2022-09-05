arrayToBeFlatten = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]


def MyFonction(dilist=[]):

    for x2 in dilist:
        if type(x2) != list:
            print(x2)
        else:
            MyFonction(x2)


for x1 in arrayToBeFlatten:

    if type(x1) == list:
        MyFonction(x1)
    else:
        print(x1)
