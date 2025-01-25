import pandas as ps

data = ps.read_csv("weather_data.csv")
print(data[data.condition == "Sunny"])



print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]

print(monday.temp)