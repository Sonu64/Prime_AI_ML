n = int(input("Enter a number: "))
t = n
count = 0
while (n != 0):
    d = n%10;
    n = n // 10
    count += 1
    
print(f"Number of digits in {t} is {count}.")
    