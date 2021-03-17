#Section_1.py
#Nelson Koomson
#3/17/2021

#First Section of my Adventure Game
from main_character import player


def start():
#This is what the player should have on his way.
    #player.money = 10
    #wounded = False
    #weapon = ["pepper_spray", "knife"]

    #Introduction
    print("This is a journey to a friends party!")

    print("I have set out of my house, ready to start the journey!")

    #Player chooses to turn right, left, or walk straight.
    #print("Which direction do you want to go?")
    #choice = input("A: Right B: Left C: Far Right").upper()


    #This function asks the player the direction he wants to go.
    def Direction():
        print("Where do you want to go?")
        choice = input("A: Right B: Left C: Far Right")
        return(choice)

    # Modified Direction() that removes option A
    def Direction2():
        print("Where do you want to go?")
        choice = input("B: Left C: Far Right")
        return(choice)

    #Modified Direction() that removes option B
    def Direction3():
        print("Where do you want to go?")
        choice = input("A:Right C: Far Right")
        return choice
    choice = Direction()


    #If the player chooses A he turns right.
    print(choice)
    while choice != "C":
        if choice == "A":
            print("Chef chooses to turn right")
            print("Chef encountered with wild animals.")
            print("Chef needs to turn to another direction")
            choice = Direction2()
            #Option A is removed
            # Runs if the player tries to pick A again.
        if choice == "A":
            choice = input("You cannot go Right again. Pick B or C.")

    #If the player chooses B he turns left.
        elif choice == "B":
            print("Chef turns left")
            print("Chef come across a lake")
            print("Chef needs to turn")
            choice = Direction3()
            #Option B is removed
            #If the player chooses any other letter, this will print invalid
        else:
            print("Invalid input")

    #If the player chooses C he turns left.
    if choice == "C":
        print("Chef chooses to turn far right")
        print("Chef have come in contact with armed robbers")
        print("Chef needs to use a weapon")
        print("Which weapon do you want to use? ", player.weapon)
        choice = input()
        print(choice)
        if choice == "knife":
            print("Player is defeated")
            exit()
        elif choice == "pepper_spray":
            print("player defeats the armed robbers and can continue the game")
            print("Is Chef wounded? ", player.wounded)
            choice = input()
            if choice == "Yes": player.wounded
            Wounded = True
            return



