from ascii_art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def card_draw(cards):
    return random.choice(cards)

def score_count(hand):
    count = 0

    for card in hand:
        count += card
    
    for i, card in enumerate(hand):
        if card == 11 and count > 21:
            hand[i] = 1
            count -= 10
            break
    
    return count

def blackjack(score):
    if score == 21:
        return True

def choose_winner(player_score, pc_score):
    if pc_score <= 21:
        if player_score == pc_score:
            print("It's a draw!\n")
        elif player_score > pc_score:
            print("You win!\n")
        else:
            print("You lose!\n")
    else:
        print("You win!")

def start_playing():
    answer = input("\nStart a new game of Blackjack? (y/n)\n").lower()

    if answer == "y":
        os.system('cls')
        play_cycle()
    elif answer != "n" and answer != "y":
        print("Type a valid answer!")
        start_playing()
    else:
        return

def play_cycle():
    print(logo)
    
    finish = False

    pc_hand = [random.choice(cards), random.choice(cards)]
    player_hand = [random.choice(cards), random.choice(cards)]

    player_score = score_count(player_hand)
    pc_score = score_count(pc_hand)

    if blackjack(pc_score) :
        print("PC blackjack! You lose!\n")
        start_playing()
        return
    elif blackjack(player_score):
        print("Blackjack! You win!\n")
        start_playing()
        return

    while not finish:    
        player_score = score_count(player_hand)
        pc_score = score_count(pc_hand)
        
        print(f"Your hand: {player_hand}\nYour score: {player_score}\n----------------\nPC first card: {pc_hand[0]}\n")

        if player_score > 21:
            print("You're over!")
            start_playing()
            return
        else:    
            drawing = input("Want to draw? (y/n)\n").lower()
            if drawing == "y":
                player_hand.append(random.choice(cards))
                pc_hand.append(random.choice(cards))
            elif drawing == "n":
                while pc_score < 17:
                    pc_hand.append(random.choice(cards))
                    pc_score = score_count(pc_hand)

                choose_winner(player_score, pc_score)
                print(f"Your final hand: {player_hand}\nYour final score: {player_score}\n----------------\nPC final hand: {pc_hand}\nPC final score: {pc_score}\n")
                start_playing()
                return

            else:
                print("Type a valid answer!\n")

#Program start

start_playing()