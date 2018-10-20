import csv

def read_Data():
    data = []
    return data

def write_Data(users):
    with open('users.csv','a', newline='') as file:
        writer = csv.writer(file)

        for row in users:
            writer.writerow(row.values())
