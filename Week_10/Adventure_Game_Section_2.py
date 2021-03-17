#Adventure_Game_Section_2.py
#Nelson Koomson
#3/17/2021

#Second Section of my Adventure Game


from main_character import player


def check_money():
    answer = input("Do you have money to pay? ")
    while answer != "Y":
        answer = input("Type correct initial? ")
    return answer


def start():
    #Chef has to walk straight if he is able to defeat the armed robbers
    choice = input("Which direction do you want to go?")
    while choice != "Straight":
        choice = input("Choose another direction")


    #Chef comes into contact with a river which he has to pay to cross.
    #answer = "Y"

    if choice == "Straight":
        print("Chef has come into contact with a river")
        print("Chef needs to pay to be transported in a boat?")

        answer = check_money()
        #print(answer)

        print("How much do you have on you? ", player.money)
        choice = int(input())
        print(choice)

            # Runs as long as "choice" is less than the amount needed to pass (10)
        while choice < 10:
            print("Not enough money, enter a different amount.")
            choice = int(input())
        #player.money = player.money - choice
        ## Line 31 will remove the amount of money the player put in for "choice" from the player's inventory--
        ###need a while statement to make sure that "choice" isn't GREATER THAN player.money!
    print(player.money)
    print("Chef has enough to let him cross the river")
    print("Chef has cross to the other side of the river")
    print("Chef needs to walk to the friends house")
    return