student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

grade = ""

for name in student_scores :
    if 100 >= student_scores[name] >= 91 :
        grade = "Outstanding"
    elif  90 >= student_scores[name] >= 81 :
        grade = "Exceeds Expectations"
    elif  80 >= student_scores[name] >= 71 :
        grade = "Acceptable"
    elif student_scores[name] <= 70 :
        grade = "Fail"
    else :
        grade = "Unknown"

    student_grades[name] = grade


print(student_grades)


_________________________________________________________________________


travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2])
