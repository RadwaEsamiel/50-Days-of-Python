import pandas

data = pandas.read_csv("weather_data.csv")
# temp = data["temp"]
# print(temp)


# temp_list = data["temp"].to_list()
# avg_temp = sum(temp_list) / len(temp_list)
# print(round(avg_temp,3))


temp_avg = data["temp"].mean()
print(round(temp_avg,3))

temp_max = data["temp"].max()
print(temp_max)

print(data.condition)