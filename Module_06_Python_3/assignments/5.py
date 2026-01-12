studData = dict()
choice = None
while choice != 'E' and choice != "EXIT":
    print("\n\n")
    print(f"[A] Add Student with Marks\n[B] Update Student Marks\n[C] Search for a Student\n[D] Display all Data.\n[E]/[Exit] Exit Application.")
    choice = input("Enter choice: ").upper()
    while choice not in ["A", "B", "C", "D", "E", "EXIT"]:
        choice = input("Please Enter Valid choice: ").upper()
    if choice == "A":
        print("________ Add Student with Marks _______")
        name = input("Enter Student Name (Case Sensitive !): ")
        marks = float(input("Enter Student Marks: "))
        while marks not in range(1, 101):
            marks = float(input("Enter Valid Marks please: "))
        studData[name] = marks
        print(f"Successfully Added Data for {name} !")
    
    elif choice == "B":
        print("________ Update Student Marks _______")
        name = input("Enter Student name to Update Marks (Case Sensitive !): ")
        if name not in studData.keys():
            print(f"No Data found for {name} !")
        else:
            marks = float(input(f"Enter updated Marks for {name}: "))
            while marks not in range(1, 101):
                marks = float(input("Enter Valid Marks please: "))
            studData[name] = marks
            print(f"Successfully Updated Marks for 1st Student with name {name}!")
            
    elif choice == "C":
        print("_________ Search for a Student ________")
        name = input("Enter Student name to Search (Case Sensitive !): ")
        if name not in studData.keys():
            print(f"No Data found for {name}!")
        else:
            print(f"Student Name: {name}\tStudent Marks: {studData[name]}.")
            
    elif choice == "D":
        print("_________ Displaying All Student Data _________")
        print("Name\t\t\t\tMarks")
        for name, marks in studData.items():
            print(f"{name}\t\t\t\t{marks}")
            