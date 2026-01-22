try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError as e:
    print("File Doesn't exist !")
    print(e)