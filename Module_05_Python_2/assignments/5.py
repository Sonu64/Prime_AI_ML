n = int(input("Enter a number: "))
t = n
sum = 0
while (n != 0):
    d = n%10;
    n = n // 10
    sum += d
    
print(f"Sum of digits in {t} is {sum}.")
    