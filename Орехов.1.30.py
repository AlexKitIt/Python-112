
import csv

with open("data2.csv") as r_file:
    file_reader = csv.reader(r_file, delimiter=";")
    count = 0
    for row in file_reader:
        print(row)
print("_______________________________________________________________________")

