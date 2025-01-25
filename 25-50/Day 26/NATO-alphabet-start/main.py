
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_alpha_dict = {row.letter:row.code for index,row in data.iterrows()}



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonatics() :
    user_input = input("Enter the Word you want to know the NATO phonetic alphabet for its letters:").upper()

    try : 
        alpha_output = [phonetic_alpha_dict[letter] for letter in user_input]
    except :
        print("Sorry Please insert letters only")
        generate_phonatics()
    else : 
        print(alpha_output)

    print(f"The phonetic alphabet is : {alpha_output}")
