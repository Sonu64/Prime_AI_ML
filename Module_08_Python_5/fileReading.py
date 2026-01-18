file = open("sample.txt", "r") # File object
# print(file)
data = file.read()

# Reading entire data at once
print("Printing Entire File content at once....")
print(data)

print("\n")
print("Printing 1st 2 Lines... Will get nothing as pointer earlier reached EOF while .read() was called !")
line1 = file.readline() # Nothing, as file pointer already reached EOF while .read() called
line2 = file.readline() # Nothing, as file pointer already reached EOF while .read() called
print(line1)
print(line2)
file.close()

# Have to Open Again for Line by Line printing to Reset File Pointer Location....

file = open("sample.txt", "r")
print("\n")
print("Printing 1st 2 Lines... This time we will get the lines as Pointer was reset by closing and opening file again :)")
line1 = file.readline() # 1st Line
line2 = file.readline() # 2nd Line
print(line1)
print(line2)
file.close()
