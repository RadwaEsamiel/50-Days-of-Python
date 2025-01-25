#TODO: Create a letter using starting_letter.txt

with open(r".\Input\Letters\starting_letter.txt") as letter_file:
    letter = letter_file.read()
    print(letter)


#for each name in invited_names.txt
with open(r".\Input\Names\invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

#Replace the [name] placeholder with the actual name.
for name in names :
    new_name = name.strip()
    new_letter = letter.replace("[name]", new_name)

    #Save the letters in the folder "ReadyToSend".
    with open(fr".\Output\ReadyToSend\letter_for_{new_name}.txt", mode="w") as write_file :
        write_file.write(new_letter)


