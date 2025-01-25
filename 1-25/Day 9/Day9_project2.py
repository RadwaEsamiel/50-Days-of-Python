# TODO-1: Ask the user for input
from math import trunc
from unicodedata import numeric

import art
print(art.logo)
print("Welcome to Secret Auction Program!")

# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
others_flag = True
bids_dict = {}

while others_flag is True:
    username = input("Please Enter your name :\n")
    bid = input("What is your bid?")

    if username in bids_dict :
        print("Name already Used. Try again with different name!")
    else :

        if bid.isnumeric() :
            bids_dict[username] = int(bid)
        else :
            print("Invalid Bid! Please Enter valid number to bid!")

    others = input("Are there any other bidders? please enter 'Yes' or 'No' ").lower()
    if others == 'no' :
        others_flag = False
    elif others == 'yes' :
        print("\n"*100)
    else :
        print("Invalid Answer")
        others_flag = False


# TODO-4: Compare bids in dictionary
def Secret_Auction(dictionary):
    winner_bid = 0
    winner_name = ""
    for key in dictionary:
        bid_amount = dictionary[key]
        if bid_amount > winner_bid :

            winner_bid = dictionary[key]
            winner_name = key
            print("\n" * 100)  # Clear the console (as an effect of secret auction)
            print(f"The Winner is {winner_name} with a Bid of ${winner_bid}")




Secret_Auction(bids_dict)







