import csv
cars = {}

import csv
with open('2.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)