fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit + " Pie")
__________________________________________________

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

total_student_scores = sum(student_scores)
print(total_student_scores)


total_student_scores_manual = 0
for score in student_scores :
    total_student_scores_manual += score

print(total_student_scores_manual)

________________________________________________________

max_student_scores = max(student_scores)
print(max_student_scores)

max_student_scores = 0
for maxx in student_scores :
    if maxx > max_student_scores :
        max_student_scores = maxx

print(max_student_scores)

_______________________________________________________

for number in range(1,10,3):
    print(number)


sum = 0
for number in range(1,101):
    sum += number

print(sum)

_______________________________________________________

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0 :
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else : 
        print(number)