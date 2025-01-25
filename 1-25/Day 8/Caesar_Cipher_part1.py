alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']





# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
def encrypt(original_text , shift_amount ) :
    indexes_list = []

    # TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

    for letter in original_text :
        if alphabet.index(letter) + shift_amount >= 26 :
            indexes_list.append((alphabet.index(letter) + shift_amount)-26)
        else :
            indexes_list.append(alphabet.index(letter) + shift_amount)

    print(indexes_list)

    encrypted_text = ""

    for inx in indexes_list :
        encrypted_text += alphabet[inx]

    print(encrypted_text)



# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

encrypt("zibra", 9)