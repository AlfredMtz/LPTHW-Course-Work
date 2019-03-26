print("Hello, How are you doing today?")
print("1. Good, 2. Ok, 3. Bad, 4. Terriable")

answer = input("> ")

if answer == "1":
    print("Great, what bring you in today?")
    print("Sofas, Tables, Beds,  or Matresses?")

    furniture = input(" ")

    if furniture == "Sofas":
        print("Are you looking for leather or fabric?")

        material = input("> ")

        if material == "leather":
            print(f"Alright!, We do have a great selection of sofas in {material}!")
        
        elif material == "fabric":
            print(f"Nice!, let's go check out the {material} gallery!")
    
    elif furniture == "Tables":
        print("I am sorry!, We don't have any tables at the moment")

    elif furniture == "Beds":
        print("Ok, What size of bed do you need?")
        print("king, queen, full, or twin?")

        size = input('> ')

        print(f"Let me show you what we have in {size} size beds?")

    elif furniture == "Matresses":
        print("You don't need Matresses, go back home and don't come back to my store!")

    else:
        print('''You need to tell me what brings you in today
        in order for me to help you!''')

elif answer in ("2", "3", "4"):
    print("You need to work on your trust issues before you walk into this store, sorry!")

else:
    print("You need to tell me how you feel, please!")

