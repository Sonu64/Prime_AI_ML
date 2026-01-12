l1 = []
l2 = []
l3 = []

num1 = None
num2 = None

while (num1 != 0 and num2 != 0):
    while num1 != 0:
        num1 = int(input("Enter a Number in 1st List: [0 to quit entering]: "))
        if num1 != 0:
            l1.append(num1)
        
    while num2 != 0:
        num2 = int(input("Enter a Number in 2nd List: [0 to quit entering]: "))
        if num2 != 0:
            l2.append(num2)
        
l3 = (l1 + l2)
l3.sort()


if len(l1)==0 and len(l2)==0:
    print("Both Lists are Empty, Combined Sorted List is Empty as well !")
elif len(l1)==0:
    print(f"1st List is Empty\n2nd List = {l2}\nCombined Sorted List is {l3}.")
elif len(l2)==0:
    print(f"1st List = {l1}\n2nd List is Empty\nCombined Sorted List is {l3}.")
else:
    print(f"1st List = {l1}\n2nd List = {l2}\nCombined Sorted List is {l3}.")