Day 8: Caesar Cipher Project
In this project, you've implemented a Caesar Cipher, an ancient encryption technique where each letter in the input text is shifted by a specified number of positions in the alphabet. The project allows both encryption (shifting letters forward) and decryption (shifting letters backward).

Key Components:

External Module:
The logo is imported from art.py and displayed when the program starts.

Caesar Cipher Functionality:
Encryption: Takes the user input, shifts each letter forward by the specified number (shift), and outputs the encrypted text.
Decryption: Reverses the process by shifting each letter backward by the specified number, revealing the original text.

Input Validation:
The program ensures that only alphabetic characters are processed. If the user enters a number, symbol, or space, a message informs them that only alphabet letters are valid for encoding/decoding.

Program Flow:
The user is prompted to choose between encrypting or decryption a message.
After processing, the user is asked if they'd like to run the cipher again. The program repeats based on their response (yes to continue, no to exit).