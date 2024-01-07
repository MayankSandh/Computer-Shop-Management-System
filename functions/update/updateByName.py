import csv
from os import remove, rename
def updateCell(filePath, name):
        with open("abcd.csv", "r+", newline="") as file:
            data = [x for x in csv.reader(file)]
        remove("{}".format(filePath))
        for r in data:
            if r[0] == name:
                r[-1] == "FIRED"
        with open("{}".format(filePath), "w+", newline="") as file:
            writer = csv.writer(file, delimiter = ",")
            writer.writerows(data)
