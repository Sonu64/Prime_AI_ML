def operation(operator, a, b):
    match operator:
        case '+':
            return a+b
        case '-':
            return a-b
        case '*':
            return a*b
        case '/':
            return a/b
        case '//':
            return a//b
        case '%':
            return a%b
        case _:
            return "Invalid Operator!"

a = int(input("\nEnter 1st number: "))
b = int(input("Enter 2nd number: "))

operator = input("Enter Operator: ")

result = operation(operator, a, b)

# print(type(result)) 
# for true division it is float, for integer division it is int.

if result != "Invalid Operator!":
    print(f"\n{a} {operator} {b} = {result}")
else:
    print(f"\n{result}")
            