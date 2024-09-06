import csv
reg,enter,exit = 0,1,2
def carflist():
    cars = []
    with open('OCR_CompSci/2.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            cars.append(row)
    return cars

def addCar(registration,entryTime):
    with open('OCR_CompSci/2.csv','a') as f:
        writer = csv.writer()

