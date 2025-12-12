# Edgar C Terrones
# 11/28/25
# Final Project
# Penalty Shootout

import random
import time
import sys

# Options for shooting and saving (Top Left, Bottom Left, Middle, Top Right, Bottom Right)
OPTIONS = ['TL', 'BL', 'M', 'TR', 'BR']

def display_goal_area():
    #Prints an image of the goal area to the console.
    print("Goal Area:")
    print(" _______[TL]____[M]____[TR]_______ ")
    print("|                                |")
    print("|                                |")
    print("|_______[BL]____[M]____[BR]_______|")

def shootout_game():
    #Main function to run the penalty shootout game.
    player_score = 0
    computer_score = 0
    rounds = 5

    print("--- Welcome to Edgar's Penalty Shootout! ---")
    print(f"You will have {rounds} shots against the computer goalie.")
    time.sleep(1)

    for i in range(1, rounds + 1):
        print(f"\n--- Round {i} ---")
        display_goal_area()

        # Player's turn to shoot
        while True:
            player_shot = input(f"Choose where to shoot ({', '.join(OPTIONS)}) or enter exit:").upper()
            if player_shot == 'EXIT':
                print("Exiting game...")
                sys.exit()  #calls exit if user wishes to exit
            if player_shot in OPTIONS:
                break
            else:
                print("Invalid choice. Please use one of the options above.")

        computer_save = random.choice(OPTIONS)
        print(f"You shoot towards the {player_shot}...")
        time.sleep(1.5)
        print(f"The computer goalie dives to the {computer_save}!")
        time.sleep(1.5)

        if player_shot == computer_save:
            print("Oh no! The goalie saved it.")
        else:
            print("GOOOOAAAL!")
            player_score += 1
        
        # Computer's turn to shoot (player acts as goalie)
        print("\n--- Computer's Shot ---")
        while True:
            player_save = input(f"Choose where to dive ({', '.join(OPTIONS)}): ").upper()
            if player_save in OPTIONS:
                break
            else:
                print("Invalid choice. Please use one of the options above.")
        
        computer_shot = random.choice(OPTIONS)
        print(f"The computer shoots towards the {computer_shot}...")
        time.sleep(1.5)
        print(f"You dive to the {player_save}...")
        time.sleep(1.5)

        if computer_shot == player_save:
            print("Great save!")
        else:
            print("Goal for the computer!")
            computer_score += 1

        print(f"\nCurrent Score: You {player_score} - {computer_score} Computer")
        time.sleep(1)

    # Final Result
    print("\n--- Final Whistle! ---")
    print(f"Final Score: You {player_score} - {computer_score} Computer")

    if player_score > computer_score:
        print("🎉 Congratulations! You win the shootout! 🎉")
    elif computer_score > player_score:
        print("😞 Unlucky! The computer wins this time. 😞")
    else:
        print("🤝 It's a draw! 🤝")

if __name__ == "__main__":
    shootout_game()