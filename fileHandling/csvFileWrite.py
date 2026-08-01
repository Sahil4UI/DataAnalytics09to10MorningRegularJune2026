data = [{"id":101,"name":"keshav","marks":100},
        {"id":102,"name":"aman","marks":60},
        {"id":103,"name":"ram","marks":90},
        {"id":104,"name":"amit","marks":10},
        {"id":105,"name":"shubham","marks":100}]

import csv
# comma separated values - excel file
'''
with open("a.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["id","name","marks"])
    for row in data:
        writer.writerow([row["id"],row["name"],row["marks"]])
'''

with open("a.csv","w") as file:
    writer = csv.DictWriter(file,fieldnames=["id","name","marks"])
    writer.writeheader()
    writer.writerows(data)
