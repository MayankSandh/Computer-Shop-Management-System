import csv
from os import remove, rename
def updateCell(filePath, r, c, new):
        with open("abcd.csv", "r+", newline="") as file:
            data = [x for x in csv.reader(file)]
        remove("{}".format(filePath))
        data[r][c] = new
        with open("{}".format(filePath), "w+", newline="") as file:
            writer = csv.writer(file, delimiter = ",")
            writer.writerows(data)
