from sys import exit

def intro():
    print("This game consist of an agent which walks you") 
    print("through the process of purchasing furniture, Do")
    print("you want to play?", '\n')
    print('Yes/No?')

    while True:
        answer = input("> ")

        if answer == 'Yes':
            yes()
        elif answer == 'No':
            no()
        else:
            print("I need a answer weather you want to play or not")



def yes():
    print("Great, Let me introduce yo to Waldo")
    print("Hello there, my name is Waldo")
    print("What is your name?")
    name = input("> ")
    print(f"A pleasure to meet you, {name}")
    print("So what bring you in today?")
    print("Are you looking for sofas, tables, or beds?")

    while True:
        furn_item = input("> ")

        if furn_item == 'sofas':
            end('Great')
        elif furn_item == 'tables':
            end('Great!')
        elif furn_item == 'beds':
            print(f"Great {name}, What size?")
        elif furn_item == 'twin':
            print("We don't have that size")
            print("I apologize, is there any other size")
            print("that you might need?")
        else:
            print('Sorry, I need an answer for the three top')
            print('Options, that is all we have rightnow')

def no():
    print("Than why did you even enter this script")
    print("You didn't know it was a gaming scriptt?")

    answer = input("> ")

    if answer == 'No':
        end("Oh!, Ok, ")
    elif answer == 'Yes':
        reason()
    else:
        end("I don't have time for this!")

def reason():
    print("What do you want from this script?")
# The for-loop is running one if-statement at a time, so once it arrives at the
# booleen comparasion statement for the numbers it throws an error because it is trying
# to convert the empty "> " statement into a number, which is not possiable. So the loop throws an 
# error before it can reach the else statement.
    while True:
        need = input("> ")

        if need == "values":
            print("What values are you looking for?")
        elif need == "nothing":
            end('Ok, We are aborting now than')
        elif float(need) > 150:
            print("This value holds an item")
        elif float(need) <= 150:
            print("There is not a value less than or equal to 150")
            print("Go ahead and give me a different value:")
        else:
            pass

def end(x):
    print(x, "We are done, Bye!")
    exit(0)


intro()