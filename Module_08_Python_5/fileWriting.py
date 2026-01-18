file = open("writingTest.txt", "w") # Creates file if doesn't exist, No Error if File Already Exists.
file.write("New content written in write mode. Old contents over-written here...")
file.close()