myList = [67, 23, 23, 34, 40, 45, 67, 40, 90, 90, 10, 10]
myListUnique = list(set(myList))

myList.sort()
myListUnique.sort()

elementsMoreThanOnce = list()

for uniqueNum in myListUnique:
    count = 0
    for num in myList:
        if uniqueNum == num and count==0:
            count += 1
        elif uniqueNum == num and count>0:
            elementsMoreThanOnce.append(uniqueNum)
            count += 1
            break


# elementsMoreThanOnce = myList - myListUnique

print(f"Elements occuring more than once are - {elementsMoreThanOnce}.")
