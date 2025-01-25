# # new_list = [new_item for item in list if test]
# #
# # names = ["radwa","ahemd","ali", "esmaiel"]
# #
# # upper_name = [name.upper() for name in names if len(name) > 5]
# # print(upper_name)
# #
# #
# # numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # squared_numbers = [num*num for num in numbers]
# # print(squared_numbers)
# #
# # list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# # numbers = [int(num) for num in list_of_strings]
# # result = [num for num in numbers if num%2 == 0]
# # print(numbers)
# # print(result)
#
# import random
# names = ["Alice", "Bob", "Charlie", "David", "Emma", "Fiona", "George", "Hannah", "Ivy", "Jack"]
#
# students_scores = {student_name:random.randint(10,100) for student_name in names }
#
# print(students_scores)
#
# passed_students = {name:score for name,score in students_scores.items() if score > 50}
#
# print(passed_students)

#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# words = sentence.split()
# result = {word:len(word) for word in words }
# print(result)


weather_c = {"Monday": 12, "Tuesday": 14,
             "Wednesday": 15, "Thursday": 14, "Friday": 21,
             "Saturday": 22, "Sunday": 24}

# (temp_c * 9/5) + 32 = temp_f

weather_f = {key:(val * 9 /5)+32 for key,val in weather_c.items() }

print(weather_f)

import pandas as pd

df_testing = pd.DataFrame([weather_c,weather_f])
print(df_testing)

for (index,row) in df_testing.iterrows() :
    print(row)


