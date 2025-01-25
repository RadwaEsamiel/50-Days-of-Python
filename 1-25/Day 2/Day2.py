print("Hello"[4])

print("Radwa"[-1])


print(type("Radwa"))

print(type(123))

print(type(123.456))

print(type(True))



username = input("Please Enter your name :\n")
name_length = len(username)

print(type(username))
print(type(name_length))
print(type("Your name length is : "))
print("Your name length is : " + str(name_length))


print(5+6)
print(6-2)
print(5*2)
print(6/3)
print(type(6/3)) <class 'float'>
print(6//3)
print(type(6//3)) <class 'int'>

print(6**3)<power> 
bmi = 84 / 1.65 ** 2 <square>


PEMDAS
Parentheses, Exponents, Multiplication/Division, Addition/Subtraction




bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi))
print(round(bmi,2))



x =2

x += 2
x *= 2
x -= 2
x /= 2
print(x)



score = 12
height = 1.6
flag = True

print(f"your score is {score} and your height is : {height} which means your winning is {flag}")