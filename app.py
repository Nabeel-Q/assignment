# prompts the player to start the game or not

print("Hello wizard.")
print("I have sent you this talking letter as a formal invitation to join the wizarding school of hogwarts.")

count = True 

while count:
    start = input("Do you want to join hogwarts yes or no? ")
    start = start.upper()
    if start == "YES":
        print("The sorting hat has unfortunately gone missing, you will have to choose your own house this year.")
        house = input("What house will you join (Gryffindor, Slytherin, Ravenclaw, Hufflepuff)? ")
        house = house.upper()
        count = False
    elif start == "NO":
        print("Well then, that was not what I expected from you but no means no.")
        print("Good day to you.")
        print("*talking letter vanishes out of thin air*")
        exit()
    else:
        print("That does not make sense you either answer with yes or no.")

roll = input("Do you want to roll the dice to learn expelliamus? ")
roll = roll.upper()

quiddich = input(f"the {house} quidditch team needs a catcher do you wanna join? ")
quddich = quiddich.upper()

ready = input("Enter yes or no to continue: ")
ready = ready.upper()