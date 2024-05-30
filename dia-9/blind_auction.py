from ascii_art import logo
import os

print(logo)

offers = {}

def define_winner(offers):
    winner_value = 0

    for name in offers:
        offer = offers[name]

        if offer > winner_value:
            winner_value = offer
            winner = name
    print(f"{winner} is the winner, paying R${winner_value}")
end_program = False

while not end_program:
    name = input("Type your name:\n")
    offer = int(input("Type your offer:\n"))

    offers[name] = offer

    more_offers = input("There are more offers?(yes/no):\n")

    if more_offers == "no":
        end_program = True
        define_winner(offers)
    elif more_offers == "yes":   
        os.system('cls')

