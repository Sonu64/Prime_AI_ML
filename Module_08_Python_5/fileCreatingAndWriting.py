file = open("tempFile.txt", "x") # Will Throw an Error if File already Exists. X Mode is especially for creating new files and writing.

lines = ["Line-1\n", "Line-2\n", "Line-3\n"]
# writelines() is used to take an iterable and write all of its contents in the file.
# Though it seems it handles newlines at the end, but No, It doesn't. We have to manually add
# newline character at the end of each iterable-content/line as we did here.

file.writelines(lines)