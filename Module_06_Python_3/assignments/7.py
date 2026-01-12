sentence = input("Enter a String: ")
spacesShortHand = len(sentence.split(' '))-1
# print(sentence.split(' '))
print(f"Number of Spaces found using .split() = {spacesShortHand}")

spacesLoop = 0
for word in sentence:
    spacesLoop = (spacesLoop + 1) if word == " " else spacesLoop
print(f"Number of Spaces found using Loop = {spacesLoop}")

