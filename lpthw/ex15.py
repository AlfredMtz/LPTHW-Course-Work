from sys import argv

# uses argv to get a filename
script, filename = argv  

# new command open, opens a given file
txt = open(filename)     

# string giving the name of your file
print(f"Here's your file {filename}:")

# we called a function on txt named read. 
# you give a file a command by using the . (dot or period).
# This line reads a file
# Its like saying, Hey txt! Do your read command with no parameters!.
# Parameters is what is inside the ()
print(txt.read()) 
txt.close()    
                       
# Ask the user again to input the file name again                     
print("Type the filename again:")
file_again = input("> ")

# reopens the file
txt_again = open(file_again)

# rereads and prints the file again
print(txt_again.read())
txt.close()


