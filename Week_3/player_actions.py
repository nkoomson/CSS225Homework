#player_actions.py
#Nelson Koomson
#2/2/21

def check_play_again(user_input):
    #This ask players of a game either to play again or quit the game
    if user_input == "Y":
        print("play again!")
    elif user_input == "N":
        print("quit the game!")
    else:
        print("Invalid input.")


check_play_again(input("Would you like to play again? Type Y for Yes or N for No: \n"))
