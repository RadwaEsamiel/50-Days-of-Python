Day 29 : Password Manager :
In this project, I developed a Password Manager application using Python's Tkinter library. The purpose of the project was to create a user-friendly interface where users can generate, store, and manage passwords securely. The password manager allows users to input a website, their email/username, and a generated password, which can be stored in a local file.

Learning Objectives and Key Concepts:
Password Generation: A random password generator was implemented, using a combination of letters, numbers, and special symbols. The random module was utilized to create strong passwords with customizable length and character composition. This feature ensures security by generating unpredictable passwords.

GUI Development with Tkinter: Tkinter was used extensively to build a graphical user interface (GUI) that interacts with the user. Widgets such as Label, Entry, and Button were utilized to create a clean and functional interface. Through this, I gained experience in handling layout and configuring UI elements to make the application user-friendly.

Entry Validation: Input validation was included to ensure the fields (website, email/username, and password) are correctly filled before saving. Appropriate error handling was implemented using message boxes (messagebox.showwarning) to prompt the user to fill all required fields or to notify them of inputs that are too short.

Clipboard Functionality: The generated password is automatically copied to the clipboard using the pyperclip library. This eliminates the need for users to manually copy passwords, enhancing convenience.

File Handling: The user data, including the website, email/username, and password, is saved into a local CSV file (passwords_dict.csv). This ensures that the password records can be stored and retrieved later. File operations such as opening, appending, and writing data were managed efficiently using Python’s file handling mechanisms.

Confirmation Dialogs: Before saving any data, the application displays a confirmation dialog (messagebox.askokcancel) to ensure that the entered information is correct. This adds a layer of security, allowing users to double-check their inputs before storing them permanently.






