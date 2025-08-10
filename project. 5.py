import pandas as pd

# sample nested json data
data = {
    "students": [
        {"name": "Alice", "age": 20, "marks": {"math": 85, "science": 90}},
        {"name": "Bob", "age": 22, "marks": {"math": 78, "science": 88}},
        {"name": "Charlie", "age": 21, "marks": {"math": 92, "science": 95}}
    ]
}

# normalize the nested json into a flat table
df = pd.json_normalize(data["students"])

print(df)
