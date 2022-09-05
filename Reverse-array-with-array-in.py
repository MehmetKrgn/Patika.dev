arrayToBeReversed = [[1, 2], [3, 4], [5, 6, 7]]

# do not use reverse() method

def myReverseFonc(myList = []):

    for x1 in range(0, len(myList) + 1, 1):
            
            myList.insert(x1, myList[-1])
            myList.pop()
    
    for x2 in myList:
        if type(x2) == list: myReverseFonc(x2)
    
    return myList


print(myReverseFonc(arrayToBeReversed))
