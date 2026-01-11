n = int(input("Enter a number: "))
t = n
digits = list()
while (n != 0):
    d = n%10;
    n = n // 10
    digits.append(d)
    
digits = digits[::-1]

print(f"Digits of {t} are", end = " ")
for i in range (len(digits)):
    if i == len(digits)-1:
        print(f"and {digits[i]}", end = ".")
    else:
        if i == len(digits)-2:
            print(f"{digits[i]}", end = " ")
        else:
            print(f"{digits[i]}", end = ", ") 