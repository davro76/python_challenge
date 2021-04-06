
import os
import csv

Pybank = os.path.join("/Users/rodneydavermann/Desktop/PyBank/Ressources/pybank_.csv")


# Open and read csv
with open(Pybank) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csv_reader:
        print(row)



    