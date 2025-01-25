import pandas as pd

sqi_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colors = sqi_data["Primary Fur Color"].dropna().unique().tolist()

count_fur = sqi_data["Primary Fur Color"].value_counts().tolist()

data_dict = {"Fur Colors" : fur_colors,
             "Count of Squirrel" : count_fur}
print(fur_colors)
print(count_fur)
print(data_dict)
Squirrel_count = pd.DataFrame(data_dict)
Squirrel_count.to_csv("Squirrel_count.csv")