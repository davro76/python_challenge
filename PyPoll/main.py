# import packages
import csv
import os

# data path
PyPoll = os.path.join("/Users/rodneydavermann/Desktop/python_challenge/PyPoll/Ressources/pypoll.csv")


# Open and read the pypoll.csv
with open(PyPoll) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    

    # Read the header row first 
    csv_header = next(csv_file)

    # initialize variables 
    count_row = 0

    # Read through each row of data after the header
    for row in csv_reader:
        count_row += 1
print(count_row)



