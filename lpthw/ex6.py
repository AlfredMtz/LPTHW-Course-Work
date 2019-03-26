# builds a variable with a value of 10
types_of_people = 10
# It formats a string with a variable inside of the string
x = f"There are {types_of_people} types of people."

# Builds a variable with a string value
binary = "binary"
# Builds a variable with a string value
do_not = "don't"
# Builds a variale with a farmatted string, which has two variables within the string
y = f"Those who know {binary} and those who {do_not}."

# it prints the value of x variable
print(x)

# it prints the value of y variable
print(y)

# it prints a formatted string, which has x variable withing the string
print(f"I said: {x}")
# it prints a formatted string, which has y variable withing the string
print(f"I also said: '{y}'")

# it builds a variable with a value equal "False"
hilarious = False
# it builds a variable with a string and flexable extension for a variable
joke_evaluation = "Isn't that joke so funny?! {}"

# it prints a variable with a formatted extension for a variable
print(joke_evaluation.format(hilarious))

# it builds a variable with a string value
w = "This is the left side of..."
# it builds a variable with a string value
e = "a string with a right side."

# it prints a combination of strings from two different variables
print(w + e)