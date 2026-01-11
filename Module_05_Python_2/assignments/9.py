import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        # the factors just repeat in reverse order after sqrt{n}. By stopping at sqrt{n}, you drastically reduce the number of iterations.
        if n%i == 0:
            # print(i)
            return False
    return True

n = int(input("\nEnter number to check for Prime: "))
output = f"\n{n} is Prime !" if isPrime(n) else f"\n{n} is not Prime."
print(output)