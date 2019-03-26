from sys import argv

# Uses argv to get a filename
script, filename = argv

# Ask the user what it wants to do with the given file
print(f"We're going to earase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# Ask the user to type its choice on what to do with the file
input("?")

# Tells the user the file is being open
print("Opening the file...")
# ('w') is just a string saying "open this file in 'write' mode"
target = open(filename, 'w')

# .truncate() Empties the file. Watch out if you care about the file
print("Truncating the file. Goodbye!")
target.truncate()

# Asks the user to input 3 lines
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Writes those three previous lines to the file
print("I'm going to write these to the file.")

# write() -- writes "stuff" to the file
target.write(f"{line1}\n{line2}\n{line3}\n")
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

# closes the file
print("And finally, we close it.")
target.close()