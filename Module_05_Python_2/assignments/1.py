salary = float(input("Enter Base Salary: "))
if salary <= 0:
    print("Invalid Salary !")
    exit(1)
elif salary > 0 and salary < 30000:
    tax = 0.05 * salary
elif salary >= 30000 and salary < 70000:
    tax = 0.15 * salary
elif salary >= 70000:
    tax = 0.25 * salary

print(f"Tax for Salary of Rs.{salary} is Rs.{tax}.")