import random
choice = 'Y'
correct = random.randint(1, 100)

print(correct)
ans = int(input("\nGuess the number [1-100]: "))

while (choice == 'Y' or choice == 'YES'):
    print(correct)
    if (ans > correct):
        print("You Guessed High !\n")
        ans = int(input("Guess again : "))
    elif (ans < correct):
        print("You Guessed Low !\n")
        ans = int(input("Guess again : "))
    else:
        print(f"Correct Guess ! {correct} is the number I was thinking of :) ")
        choice = input("Do you want to Play again ? [Y/N]: ").upper()
        while choice not in ['Y', 'YES', 'N', 'NO']:
            choice = input("Please Enter Valid Choice ! [Y/N]: ").upper()
        if choice == 'Y' or choice == 'YES': 
            correct = random.randint(1, 100)
            print(correct)
            ans = int(input("\n\n\nGuess the number [1-100]: "))
