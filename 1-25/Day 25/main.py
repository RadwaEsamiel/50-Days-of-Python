# with open("weather_data.csv") as file :
#     weather = file.readlines()
#     print(weather)

import csv
with open("weather_data.csv") as file :
    weather_data = csv.reader(file)
    temperatures = []
    for row in weather_data :
        if row[1] != "temp" :
            temperatures.append(int(row[1]))
    print(temperatures)

