import math

num = input("Enter number: ")
num = float(num)

ip = int(math.floor(num))
dp = num-ip

print(f"Integer part is {ip}, and Decimal part is {dp}.") 
# But the above process gives Decimal Precision Errors, for better results use Decimal Module


from decimal import Decimal
num = input("Enter a Decimal Number: ")
# It is best practice to convert from a string to avoid float conversion errors first
# So keep num as str, no need to convert to float.
num = Decimal(num)

integerPart = int(num)
decimalPart = num - integerPart
print(f"Integer part is {integerPart}, and Decimal part is {decimalPart}.") 





