import csv

data = [
    "FirstName,LastName".split(","),
    ["Virat","Kohli"],
    ["Sachin","Tendulkar"],
    ["MS","Dhoni"],
    ["Yuvraj","Singh"],
    ["Ishant","Sharma"]
]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for row in data:
        writer.writerow(row)