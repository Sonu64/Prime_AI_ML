word = input("Enter word to search in File: ")
temp = word
word = word.lower()
lineNumbers = list()
try:
    with open("words.txt", "r") as f:
        lines = f.readlines()  
        for i in range(0, len(lines)):
            if word in lines[i].lower(): # Can directly convert a line to lowercase like this
                lineNumbers.append(i+1)
except FileNotFoundError as e:
    print("File to search does not exist !")
    print(e)
else:
    if len(lineNumbers) > 0:
        print(f"{temp} occur in Lines ", end="")
        print(*lineNumbers, sep=', ') # Astersik (*) is the Unpacking Operator, Seperated by commas.
    else:
        print(f"{temp} is not found in the File !")
finally:
    print("Program over !")
    