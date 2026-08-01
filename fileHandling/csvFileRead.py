import csv

with open("a.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# with open("a.csv","r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)
