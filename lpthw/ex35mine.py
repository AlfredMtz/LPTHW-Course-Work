from sys import exit

#1 start() -->> Introduces the game
def start():
    print("You are in a dark room.")
    print("There are four different doors: 1,2,3,4.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "1":
        bear_room()
    elif choice == "2":
        cthulhu_room()
    elif choice == "3":
        chupacabra_room()
    elif choice == "4":
        sales_rep_room()
    else:
        dead("You stumble around the room until you starve.")

#2 bear_room() -->> Function is call if users chooses to go through the 'left' door, when asked in the start() function
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    # saves 'False' estatement for upcoming while loop
    bear_moved = False

    # As long as the upcoming boolens give a 'True' output, rerun the loop all over again, if boolens estatement outputs
    # 'False' than stop running the loop.
    while True:
        choice = input("> ")

        # if boolen estatement equals true, than run the dead() function which prints you a message and 
        # exists the entire script through the .exit(0) extension, consequently if script is exited, the while loop
        # obviously stops.
        if choice == "take honey":
            dead("The bear look at you then slaps your face off.")
        # if  boolen estatements equals true, than print the estated code, and save bear_moved variable as True.
        # and rerun the while loop again.
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        # if the user retypes 'taunt bear' again and bear_moved equals ' False' than call the dead() function which
        # prints your string message and makes the script to exit and end the game.   
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        # Now the while loop was rerun and the user is asked to give a new input, if 'open door' is chosen and bear_moved
        # equals 'False' than call the function 'gold_room()'.
        elif choice == "open door" and bear_moved:
            gold_room()
        # Else, if anything else is type than call the print() given message, and rerun the while loop and keep
        # asking the user to give a valid answer.
        else:
            print("I got no idea what that means.")

#3 gold_room() -->> This function is call after the user request 'open door' in the 'bear_room()'
# function.
# I fixed this function to work better with the numbers
def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input('> ')

    how_much = int(choice)

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)

    elif how_much > 50:
        dead("You greedy bastard!, Not a")
    else:
        dead("Man, learn to type a number.")



#4 Function runs if users chooses to go through the right door!
def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

#5 Function makes the program to abort.
def dead(why):
    print(why, "Good job!")
    exit(0)


def chupacabra_room():
    print("Hi I am the legendary chupacabra")
    print("Are you scared, Yes or No?")

    choice = input("> ")

    if "Yes" in choice:
        print("You better be!")
    elif "No" in choice:
        dead("Nothing should scared you")
    else:
        print("I need a straight answer")

def sales_rep_room():
    print("Hi, Good Morning!")
    print("What brings you in today?")
    tables = False


    while True:
        choice = input("> ")

        if choice == "Sofas":
            print("Wonderfull, we have a big selection!")
        elif choice == "Tables" and not tables:
            print("Sorry, we have no tables")
            print("Do you need anything else today?")
            # It changes the variable tables to true. So if the user
            # asks again, the next time it would takes the next statement
            tables = True
        elif choice == "Tables" and tables:
            print("What kind of tables")
        else:
            print("Give me a valid statement")



#1 Run the function that starts the game
start()


 