list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8, 10, 4, 2, 3]

set1 = set(list1)
set2 = set(list2)

if len(set1.intersection(set2)) == 0:
    print("No Common Elements !")
else:
    print(set1.intersection(set2))