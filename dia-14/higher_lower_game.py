from ascii_art import logo, vs
from game_data import data
import os, random, copy

def gameplay(data, restart):
    def guess(a_choice, b_choice):
        print(logo)
        print(f"Compare A: {data[a_choice]['name']}, {data[a_choice]['description']}, from {data[a_choice]['country']}")
        print(f"{vs}\n")
        print(f"Against B: {data[b_choice]['name']}, {data[b_choice]['description']}, from {data[b_choice]['country']}")
        
        player_guess = input("Wich one has more followers? [A/B]\n").lower()

        while player_guess != "a" and player_guess != "b":
            os.system('cls')    
            print(logo)
            print(f"Compare A: {data[a_choice]['name']}, {data[a_choice]['description']}, from {data[a_choice]['country']}")
            print(f"{vs}\n")
            print(f"Against B: {data[b_choice]['name']}, {data[b_choice]['description']}, from {data[b_choice]['country']}")
            
            player_guess = input("Type a valid answer!!\n\nWich one has more followers? [A/B]\n").lower()

        if player_guess == "a":
            return "a"
        else:
            return "b"
        
    def compare_guess(a_choice, b_choice, player_guess):
        if data[a_choice]["follower_count"] > data[b_choice]["follower_count"]:
            if player_guess == "a":
                return True
            else:
                return False
        else:
            if player_guess == "b":
                return True
            else:
                return False
            
    os.system('cls')
    data.clear()
    data = copy.deepcopy(restart)
    print(logo)
    new_game = input("\nStart a new game? [y/n]\n").lower()
    
    os.system('cls')
    
    while new_game != "y" and new_game != "n":
        os.system('cls')
        new_game = input(f"{logo}\n\nType a valid answer!!\n\nStart a new game? [y/n]\n").lower()

    if new_game == "y":
        score = 0
        a_choice = random.randint(0, len(data) - 1)
        
        while score < len(data) - 1:
            os.system('cls')
            b_choice = random.randint(0, len(data) - 1)
            while data[b_choice]["name"] == data[a_choice]["name"] or data[b_choice]["name"] == "OUT":
                if score < len(data) - 1:
                    b_choice = random.randint(0,len(data) - 1)
                else:
                    break

            player_guess = guess(a_choice, b_choice)

            if compare_guess(a_choice, b_choice, player_guess) == False:
                input(f"Wrong answer!\nYour score was {score}\n\nPress any key to continue.")
                data.clear()
                data = copy.deepcopy(restart)
                gameplay(data, restart)
                return
            else:
                score += 1

                if player_guess == "b":
                    data[a_choice]["name"] = "OUT"
                    a_choice = b_choice
                else:
                    data[b_choice]["name"] = "OUT"
                    b_choice = a_choice
        
        input("Congratulations! You've reached the end of the game!!\n\nPress any key to continue.")
        data.clear()
        data = copy.deepcopy(restart)
        gameplay(data, restart)
    else:
        return


restart = []

restart = copy.deepcopy(data)

gameplay(data, restart)