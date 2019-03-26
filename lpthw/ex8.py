# creates a variable with a string
formatter = "{} {} {} {}"

# takes the formatter variable and calls the format
# function for four arguments, which match up with
# the four {} in the formatter variable
print(formatter.format(1, 2, 3, 4))
# takes the formatter variable and calls the format 
# function for four arguments, which mathc up with
# the four {} in the formatter variable
print(formatter.format("one", "two", "three", "four"))
# takes the formatter variable and calls the format
# function for four arguments, which match up with
# the four {} in the formatter variable
print(formatter.format(True, False, False, True))
# takes the formatter variable and calls the format
# function for four arguments, which match up with
# the four {} in the formatter variable
print(formatter.format(formatter, formatter, formatter, formatter))
# takes the formatter variable and calls the format
# function for four arguments, which match up with
# the four {} in the formatter variable

print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
)) 