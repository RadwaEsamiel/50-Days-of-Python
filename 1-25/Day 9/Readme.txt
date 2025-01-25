Day 9: Secret Auction Program

This project implements a secret auction program where multiple bidders can submit their bids. The bids are stored in a dictionary, and once all participants have entered their bids, the program determines and announces the winner with the highest bid.

Key Components:
Logo Display:
The program begins by displaying the logo imported from the art.py file.

Bid Collection:
The user is prompted to enter their name and bid amount.
The input validation ensures that the bid is numeric.
The bids are stored in a dictionary with the name as the key and the bid as the value.

Handling Multiple Bidders:
After each bid, the program asks if there are more bidders. If the user answers "yes," it clears the screen and waits for the next bidder. If "no," it proceeds to find the winner.

Winner Determination:
The program identifies the highest bid and prints the name of the winning bidder along with their bid amount.