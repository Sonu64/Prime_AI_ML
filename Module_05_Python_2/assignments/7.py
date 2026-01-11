n = input("Enter a number: [or 'Q' or 'Quit'] to exit: ")
while(True):
    try:
        result = "Positive" if int(n)>0 else "Negative"
        print(result)
        n = input("Enter a number: [or 'Q' or 'Quit'] to exit: ")
    except:
        n = n.lower()
        if n!='q' and n!='quit':
            n = input("Please Enter Valid values for n : [or 'Q' or 'Quit'] to exit: ")
        else:
            break
        
    