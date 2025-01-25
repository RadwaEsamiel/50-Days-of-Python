file = open("testing.txt")
content = file.read()
print(content)
file.close()

with open("testing.txt", mode="a") as file2 :
    file2.write("hello radwa!")


with open("testing.txt") as newfile :
    newcontent = newfile.read()
    print(newcontent)


with open("../Day 23/ReadMe.txt") as readme_file :
    file_content = readme_file.read()
    print(file_content)


with open(r"D:\iti\Interviews Preparation\Python\Day 23\ReadMe.txt") as readme_file:
    file_content = readme_file.read()
    print(file_content)


with open("D:\\iti\\Interviews Preparation\\Python\\Day 23\\ReadMe.txt") as readme_file:
    file_content = readme_file.read()
    print(file_content)
