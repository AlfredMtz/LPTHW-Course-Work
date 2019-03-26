# Import argv function from sys package
from sys import argv

# The 'exists' function returns as 'True' or 'False'
# if a file exist.
from os.path import exists

script, from_file, to_file = argv

# we could do these two on one line, how?
indata = open(from_file).read()

out_file = open(to_file, 'w').write(indata)
