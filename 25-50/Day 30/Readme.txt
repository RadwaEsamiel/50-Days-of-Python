Day 30 : Password Manager Project 
This project is a simple Password Manager application built using Python's tkinter library for the graphical user interface (GUI). The program allows users to manage and securely store passwords for different websites. I implemented several key features that enhance both the usability and functionality of the application.

Key Features:

Password Generation:
The application includes a built-in password generator. When a user clicks the "Generate Password" button, a random password is created using an external password_generator module. The generated password is automatically inserted into the password field and copied to the clipboard for easy use.

Password Storage:
Passwords, along with the associated website and email/username, are stored in a passwords.json file. This allows for easy retrieval and reuse later. If the file doesn't exist, it is created, and new entries are appended to the existing data.

Search Functionality:
Users can search for passwords by entering the website name. The application retrieves the relevant email/username and password from the passwords.json file and displays it in a messagebox. If the website isn't found, an appropriate warning is displayed.


Form Validation:
Before adding any new entries, the application validates the input to ensure that no fields are left empty and that the website, email, and password meet a minimum length requirement. This improves both user experience and data integrity.

Data Persistence:
Passwords are saved to a JSON file, ensuring that data is persisted even after closing the application. The file is updated each time a new entry is added.

Error Handling: implemented exception handling, particularly when reading and writing to the JSON file. This ensures that the program remains robust in cases where the file may be missing or corrupted.
