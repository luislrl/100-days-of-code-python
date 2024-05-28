import random

from words import word_list

hearts = 6

visualization = []

correct_word = random.choice(word_list)
length = len(correct_word)

end = False

from ascii_art import logo
print(logo)

for _ in range(length):
    visualization.append('_')

while not end:
    guess = input("Guess a letter: ").lower()

    if guess in visualization:
        print(f"You've already tried {guess}")

    for position in range(length):
        letter = correct_word[position]
        
        if letter == guess:
            visualization[position] = letter

    if guess not in correct_word:
        print(f"You tried {guess}, it's not a letter of the word. You lose a heart.")
        
        hearts -= 1
        if hearts == 0:
            end = True
            print("You lose.")

    print(f"{' '.join(visualization)}")

    if "_" not in visualization:
        end = True
        print("You win.")

    from ascii_art import lose_progress, logo
    print(lose_progress[hearts])