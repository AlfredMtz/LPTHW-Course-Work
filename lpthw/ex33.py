''' This function checks whether a given number is'''

def check_condition(number, increment):
    # variable i has a starting value of 0, and variable 'number' is an empty list
    i = 0
    numbers = []

    # run the while loop block of code has long as the boolen statement '<' is true, once the boolen
    # statement becomes false, go ahead and stop running the while loop block of code.
    while i < number:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment
        print("The numbers: ", numbers)
        print(f"At the bottom i is {i}")

    # Before running this lines of code, the while loop block on top needs to finish running entirely, than python will move
    # to the next lines of codes.
    print("The numbers: ")

    # The variable 'numbers' became a list full on numbers captured by the while loop above.
    for num in numbers:
        print(num)