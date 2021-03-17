#main_game.py
#Nelson Koomson
#3/17/2021


#You have been invited to a party and you have to find means of getting to the destination
#This file will control how the game will flow

#This function imports the various section into the main game
from main_character import player

import Adventure_Game_Section_1
import Adventure_Game_Section_2
import Adventure_Game_Section_3


print("old name: ", player.name)
#prayer.name = input("Enter your name: ")
#print("new name: ", player.name)

Adventure_Game_Section_1.start()
Adventure_Game_Section_2.start()
Adventure_Game_Section_3.start()