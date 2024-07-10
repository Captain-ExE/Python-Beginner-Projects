alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]


#main caesar funtion starts
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f'The {cipher_direction}d text is "{end_text}"')


#main caesar funtion ends

print(
    "Welcome to Caesar Cypher encryption decryption program. here you can encrypt and decrypt text\n"
)
continue_p = True
while continue_p:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message.\n").lower()
    shift = int(input("Type the shift amount.\n"))
    shift = (shift % 26)

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    decision = input("If you want to continue? type yes or no.\n")
    if decision == "no":
        continue_p = False
        print("Program ended here. goodbye!")
