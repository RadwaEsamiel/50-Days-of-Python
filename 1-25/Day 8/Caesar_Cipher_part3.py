# TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(direction_value) :

    def decrypt(original_text, shift_amount) :
        decrypted_text = ""
        for letter in original_text :
                if letter not in alphabet:
                    print("invalid Text only alphabet letters will be decoded!")
                    break
                else:
                    shifted_position = alphabet.index(letter) - shift_amount
                    shifted_position %= len(alphabet)
                    decrypted_text += alphabet[shifted_position]
        print(f"Here is your decrypted result: {decrypted_text}")


    def encrypt(original_text, shift_amount):
        cipher_text = ""
        for letter in original_text:
            if letter not in alphabet:
                print("invalid Text only alphabet letters will be encoded!")
                break
            else:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
        print(f"Here is the encoded result: {cipher_text}")


    if direction_value == "decode" :
                decrypt(text,shift)
    elif direction_value == "encode" :
                encrypt(text,shift)
    else :
        print("Invalid Reqeust")


# TODO-3: Can you figure out a way to restart the cipher program?
flag = False

while not flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction.lower())

    answer = input("Type 'yes' if you want to go again. Otherwise, type 'no'.")

    if answer == "yes" :
        caesar(direction.lower())
    elif answer == "no" :
        flag = True
    else :
        print("Invalid Answer!")
        flag = True

