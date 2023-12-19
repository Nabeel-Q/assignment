import app
'''This module is used to import the player data.'''
import Slytherin
import Gryffindor
import Ravenclaw
import Hufflepuff
'''These modules will import the attributes of each role
like health, magic points, luck, intelligence, dexterity, and strength.'''
import random
'''the random module allows you to create a random number generator.'''

if app.house == "GRYFFINDOR":
    print("ah a righteous one, you will join the Gryffindor house.")
    ST = Gryffindor.ST
    LK = Gryffindor.LK
    DX = Gryffindor.DX
    IQ = Gryffindor.IQ
    HP = Gryffindor.HP
    MP = Gryffindor.MP
    rival = "Slytherin"
elif app.house == "SLYTHERIN":
    print("ah a cunning one, you will join the Slytherin house.")
    ST = Slytherin.ST
    LK = Slytherin.LK
    DX = Slytherin.DX
    IQ = Slytherin.IQ
    HP = Slytherin.HP
    MP = Slytherin.MP
    rival = "Gryffindor"
elif app.house == "RAVENCLAW":
    print("ah an intelligent one, you will join the Ravenclaw house.")
    ST = Ravenclaw.ST
    LK = Ravenclaw.LK
    DX = Ravenclaw.DX
    IQ = Ravenclaw.IQ
    HP = Ravenclaw.HP
    MP = Ravenclaw.MP
    rival = "Hufflepuff"
elif app.house == "HUFFLEPUFF":
    print("ah a good and loyal friend, you will join the Hufflepuff house.")
    ST = Hufflepuff.ST
    LK = Hufflepuff.LK
    DX = Hufflepuff.DX
    IQ = Hufflepuff.IQ
    HP = Hufflepuff.HP
    MP = Hufflepuff.MP
    rival = "Ravenclaw"
else:
    print("That's not a house.")

if rival == "Gryffindor":
    print("ah a righteous one, you will join the Gryffindor house.")
    RST = Gryffindor.ST
    RLK = Gryffindor.LK
    RDX = Gryffindor.DX
    RIQ = Gryffindor.IQ
    RHP = Gryffindor.HP
    RMP = Gryffindor.MP
elif rival == "Slytherin":
    print("ah a cunning one, you will join the Slytherin house.")
    RST = Slytherin.ST
    RLK = Slytherin.LK
    RDX = Slytherin.DX
    RIQ = Slytherin.IQ
    RHP = Slytherin.HP
    RMP = Slytherin.MP
elif rival == "Ravenclaw":
    print("ah an intelligent one, you will join the Ravenclaw house.")
    RST = Ravenclaw.ST
    RLK = Ravenclaw.LK
    RDX = Ravenclaw.DX
    RIQ = Ravenclaw.IQ
    RHP = Ravenclaw.HP
    RMP = Ravenclaw.MP
else:
    print("ah a good and loyal friend, you will join the Hufflepuff house.")
    RST = Hufflepuff.ST
    RLK = Hufflepuff.LK
    RDX = Hufflepuff.DX
    RIQ = Hufflepuff.IQ
    RHP = Hufflepuff.HP
    RMP = Hufflepuff.MP

print("Now that you've been sorted into your house I'll see you tommorow at hogwarts.")
print("*talking letter vanishes*")
print("*24 hrs goes by your at hogwarts attending your first class*")

# challenge 1

print("Hello everyone, I am professor Gilderoy Lockhart and I will be teaching you how to cast spells today.")
print("In todays class you will be casting the spell expelliamus, which allows you to move objects with your wand.")

expelliamus = 0
dice = 0
count = True

if app.roll == "YES":
    dice = random.randrange(1, 21)
    if dice >= 15:
        expelliamus = 1
        IQ = IQ + 2
        DX = DX + 2
        print(f"critical win, you rolled a {dice} and sucessfully learnt expelliamus. (+2 IQ, +2, DX)")
        print("Alright, class is over you are now dismissed.")
    elif dice >= 10 and dice < 15:
        expelliamus = 1
        print(f"win, you rolled a {dice} and sucessfully learned expelliamus.")
        print("Alright, class is over you are now dismissed.")
    elif dice >= 5 and dice < 10:
        expelliamus = 0
        print(f"loss, you rolled a {dice} and didn't learn expelliamus.")
        print("Alright, class is over you are now dismissed.")
    else:
        expelliamus = 0
        IQ = IQ - 2
        DX = DX - 2
        print(f"critical loss, you rolled a {dice} and didn't learn expelliamus. (-2 IQ, -2 DX)")
        print("Alright, class is over you are now dismissed.")
elif app.roll == "NO":
    print("Ok, I guess another delinquent has decided to join this class very well, you will regret this later.")
    print("Alright, class is over you are now dismissed.")
else:
    print("How did you get accepted into hogwarts? Just leave my class.")


# challenge 2

print(f"*From down the hallway the quidditch coach for team {app.house} sees you*")
print("hey hey hey")

catch = 0
dice2 = random.randrange(1, 21)

if app.quiddich == "YES":
    print(f"ok, The game against {rival} is in three days be sure to train for it")
    print(f"Hello one and all, todays game is going to be played by {app.house} against {rival}")
    print(f"*the score of the game is 7-3 {rival} is winning*")
    print("the golden snitch has been thrown out")
    print("*a dice will be rolled on whether or not you catch the golden snitch*")
    if dice2 >= 15:
        catch = 1
        DX += 5
        ST += 5
        print(f"The golden snitch has been caught team {app.house} wins. (DX = +5, ST = +5)")
    elif dice2 >= 10 and dice2 < 15:
        catch = 1
        print(f"The golden snitch has been caught team {app.house} wins.")
    elif dice2 >= 5 and dice2 < 10:
        print(f"ooh, team {app.house} almost caught the snitch but team {rival} has caught it and wins the game.")
    else:
        DX -= 5
        ST -= 5
        print(f"The golden snitch has been caught team {rival} wins.")
elif app.quiddich == "NO":
    print("alright, I guess I have to find somebody more capable of playing quiddich then.")
    print("Game Over")
    exit()

# challenge 3

print("Are you ready for challenge 3?")

if app.ready == "YES":
    print(f"*The game is over and you see a player from {rival} walking to you*")
    if catch == 1:
        print("I know you cheated, I challenge you to a battle at midnight don't chicken out.")
    else:
        print("ha, I knew you were bad your not as fast as me")
        print("how about this since you lost to me in quidditch. How about we battle at midnight to see what your really worth.")
elif app.ready == "NO":
    print("Game Over")
    exit()
else:
    print("You need to input yes or no.")
    exit()

print("*it is now midnight and you show up for the battle*")
print("I thought you would chicken out, I guess your braver than I thought")

dice3 = random.randrange(1, 21)

if dice3 >= 15:
    if expelliamus == 1:
        MP -= 10
        RHP -= 50
        print("you have used expelliamus before your rival could and hit him with a rock. (-10 MP)")
    else:
        RMP -= 10
        print("Your rival used expelliamus but missed his attack")
elif dice3 >= 10 and dice3 < 15:
    if expelliamus == 1:
        MP -= 10
        RHP -= 50
        HP -= 50
        RMP -= 10
        print("you have used expelliamus and hit your rival with a rock. (-10 MP)")
        print("you were hit with a rock by your rivals expelliamus. (-50 HP)")
    else:
        HP -= 50
        RMP -= 10
        print("you were hit with a rock by your rivals expelliamus (-50 hp)")
elif dice3 >= 5 and dice3 < 10:
    if expelliamus == 1:
        MP -= 10
        RMP -= 10
        HP -= 50
        print("you use expelliamus to hit your opponent with a rock but you miss")
        print("your opponent hits you with a rock using expelliamus")
    else:
        HP -= 50
        RMP -= 10
        print("you were hit with a rock by your rivals expelliamus (-50 hp)")
else:
    if expelliamus == 1:
        MP -= 10
        RMP -= 10
        HP -= 50

print("*after using expelliamus you start fist fighting each other*")
print("your strength and dexterity will be the deciding factor in this fight")

if DX > RDX and ST > RST:
    RHP -= 50
elif DX < RDX and ST < RST:
    HP -= 50
elif DX < RDX and ST > RST:
    RHP -= 25
    HP -= 25
elif DX > RDX and ST < RST:
    RHP -= 25
    HP -= 25
else:
    RHP -= 100
    HP -= 100

if HP > RHP:
    print("You win")
elif HP < RHP:
    print("You lose")
else:
    print("The fight has ended in a draw")