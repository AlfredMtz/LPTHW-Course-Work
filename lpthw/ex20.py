# imports module argv from sys package
from sys import argv

# sets variable for argv
script, input_file = argv

# defines function to read the passed file
def print_all(f):
    print(f.read())

# defines function to start reading given file at byte 0
# or postion 0, meaning at the beggining of the file.
def rewind(f):
    f.seek(0)

# defines function to read _____ and only first line of text file
def print_a_line(line_count, f):
    print(line_count, f.readline(), end= "")

# Opens and saves given file to defined variable
current_file = open(input_file)

print("First let's print the whole file:\n")

# Uses previously defined 'print_all' function and
# passes current_file variable with file inside
print_all(current_file)

print("\nNow let's rewind, kind of like a tape.")

# moves the read/write location to the begining 
# of the file.
rewind(current_file)

print("Let's print three lines:")

# variable set to 1
current_line = 1
print_a_line(current_line, current_file)

# variable becomes 2, since it has a value of 1 already
# and we added 1 more.
current_line += 1
print_a_line(current_line, current_file)

# variable becomes 3, since it has a value of 2 now and we
# added 1 more.
current_line += 1
print_a_line(current_line, current_file)