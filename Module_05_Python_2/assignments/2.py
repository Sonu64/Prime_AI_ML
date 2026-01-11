a = int(input("Enter a: "))
b = int(input("Enter b: "))

for i in range(a, b+1):
    if i%2 == 0:
        print(f"{i}\t")