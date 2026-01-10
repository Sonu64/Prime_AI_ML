p = float(input("Enter Principal Amount: "))
r = float(input("Enter % Rate of Interest: "))
t = float(input("Enter time (in years): "))
si = (p*r*t)/100
print(f"Simple Interest is Rs.{si}, Final Amount = Rs.{si+p}")