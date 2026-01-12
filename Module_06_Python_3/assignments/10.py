s = input("Enter a String: ")
allChars = []
for w in s:
    if w != " ":
        allChars.append(w)
uniqueChars = list(set(allChars))
lengthUniqueChars = len(uniqueChars)

print(f"All Unique Characters -> {uniqueChars}\nNumber of Unique Characters is {lengthUniqueChars}.")