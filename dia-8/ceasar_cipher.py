alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, change_qnt, codify_decodify):
  
  end_text = ""

  if codify_decodify == "decodify":
    change_qnt *= -1

  for char in text:
    if char in alphabet:
      position = alphabet.index(char)
      new_pos = position + change_qnt
      end_text += alphabet[new_pos]
    else:
      end_text += char

  print(f"Here's the {codify_decodify}d result: {end_text}")

finish = False

while not finish:

  direction = input("Type 'codify' or 'decodify' to choose what to do:\n")
  shift = int(input("Type the shift qantity:\n"))
  text = input("Type your text:\n").lower()
  
  shift = shift % 26

  caesar(text=text, change_qnt=shift, codify_decodify=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    finish = True

    print("Goodbye")
    


