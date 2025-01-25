import pandas as ps

data_dict = {
    "name": "Alice",
    "age": 28,
    "is_student": False,
    "grades": [88, 92, 75, 85],
    "courses": {
        "math": "A",
        "science": "B+",
        "history": "A-"
    }
}
data = ps.DataFrame([data_dict])
data.to_csv("new_data.csv")