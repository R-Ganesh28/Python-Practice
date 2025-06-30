import csv
with open("peoples.csv", 'r')as f:
    reader = csv.reader(f)
    for row in reader:
        print("csv rows: ", row)

