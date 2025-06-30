import csv
rows = [
    ["Name", "age", 'city'],
    ['Alice', 20, 'Goa'],
    ['Bob', 19, 'China']
]
with open('peoples.csv', 'w', newline = '')as file:
    writer = csv.writer(file)
    writer.writerows(rows)
