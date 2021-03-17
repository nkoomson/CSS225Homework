#Adventure_Game_Section_3.py
#Nelson Koomson
#3/17/2021

#Third Section of my Adventure Game

from main_character import player


#Chef will then walk 20 feet to the yellow house
def start():
    print("Chef has to go to the store to purchase a gift for the friend")
    print("Chef finds a store to the right")
    print("Chef enters the store to purchase a gift")

    gift = input("Choose a gift to purcase at the store? gift card or drink or jewelry")
    while gift != "gift card" and gift != "drink" and gift != "jewelry":
        gift = input("You must select a different item")
    player.gift.append(gift)
    print(player.gift)


    print("Chef has to walk 20 feet to the yellow house")

    choice = input("Which house is the party?")
    while choice != "yellow":
        choice = input("Enter a different color")

    print("Well done, you've won")
    print("The party host really appreciated your ", player.gift[0],"!")
    exit()