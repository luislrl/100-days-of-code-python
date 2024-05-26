import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letters_qnt = int(input("How many letters would you like in your password?\n")) 
numbers_qnt = int(input(f"How many numbers would you like?\n"))
symbols_qnt = int(input(f"How many symbols would you like?\n"))

password = []

for char in range(1, letters_qnt + 1):
  password.append(random.choice(letters))
for char in range(1, numbers_qnt + 1):
  password += random.choice(numbers)
for char in range(1, symbols_qnt + 1):
  password += random.choice(symbols)

final_password = ""

random.shuffle(password)

for char in password:
  final_password += char

print(f"Your password is: {final_password}")