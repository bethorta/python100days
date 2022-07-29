from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, direction):
  end_text = ""
  if direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char not in alphabet:
      new_char = char
    else:
      position = alphabet.index(char)
      new_position = position + shift_amount
      if new_position > len(alphabet) - 1:
        new_position -= len(alphabet)
      elif new_position < 0:
        new_position += len(alphabet)
      new_char = alphabet[new_position]
    end_text += new_char

  print(f"Here's the {direction}d result: {end_text}")
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "yes":
    cipher_program()
  else:
    print("Goodbye")

def cipher_program():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % len(alphabet)
  caesar(text, shift, direction)

print(logo)
cipher_program()