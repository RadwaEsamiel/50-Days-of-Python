# with open("testing_file.csv") as file :
#     file.read()

try :
    file = open("testing_file.csv")

except :
    file = open("testing_file.csv","w")
    file.write("this for testing")
else:
    content = file.read()
    print(content)
finally:
    file.close()