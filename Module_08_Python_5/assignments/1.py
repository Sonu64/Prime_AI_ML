f = open("names.txt", "w")
names = [input(f"Enter Name {i+1}: ")+"\n" for i in range(5)]
f.writelines(names)
print("All names written to File.")
f.close()

print("Showing File Content - ")
f = open("names.txt", "r")
print(f.read())
f.close()

