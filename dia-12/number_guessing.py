from ascii_art import logo
import random
import os

def gameplay():
    def game_range():
        number_range = int(input("Choose a size for the challenge. [100/500/1000]\n"))

        while number_range != 100 and number_range != 500 and number_range != 1000:
            number_range = int(input("\nType a valid answer!!\n\nChoose a size for the challenge. [100/500/1000]\n"))
        return number_range  


    def lives():
        difficulty = (input("Choose the game's difficulty. [easy/hard]")).lower()

        while difficulty != "easy" and difficulty != "hard":
            difficulty = (input("Type a valid answer!!\n\nChoose the game's difficulty. [easy/hard]\n")).lower()
        if difficulty == "easy":
            return 10
        else:
            return 5

    print(f"{logo}\n---------------------------------------------------\n\nWelcome!\nIn this game you have to guess the mysterious number!\n")

    max_num = game_range()
    lives = lives()
    answer = random.randint(1, max_num)
    lost = False

    def guess():
        player_guess = int(input(f"{lives} lives left!\nMake your guess:\n"))

        while player_guess < 1 and player_guess > max_num:
            player_guess = int(input(f"{lives} lives left!\nMake your guess:\n"))
        
        return player_guess
    
    player_guess = guess()
    
    while player_guess != answer:
        if lives < 1:
            lost = True
            break

        if player_guess > answer:
            lives -= 1
            print("\nThe answer is lower!")
            player_guess = guess()
        elif player_guess < answer:
            lives -= 1
            print("\nThe answer is higher!")
            player_guess = guess()
    if not lost:    
        again = input(f"\nGreat, you did it with {lives} lives left!\nPlay again? [y/n]\n")

        while again != "y" and again != "n":
            again = input(f"\nType a valid anser!!\n\nGreat, you did it with {lives} lives left!\nPlay again? [y/n]\n")
        if again == "y":
            os.system('cls')
            gameplay()
        else:
            return
    else:    
        again = input(f"\nOh no, you have no lives left!\nPlay again? [y/n]\n")

        while again != "y" and again != "n":
            again = input(f"\nType a valid anser!!\n\nOh no, you have lives left!\nPlay again? [y/n]\n")
        if again == "y":
            os.system('cls')
            gameplay()
        else:
            return

gameplay()