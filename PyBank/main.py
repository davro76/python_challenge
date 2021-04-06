# import required library
import os
import csv

# data path
Pybank = os.path.join("/Users/rodneydavermann/Desktop/python_challenge/PyBank/Ressources/pybank.csv")


# Open and read the pybank.csv
with open(Pybank) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # initialize variables 
    count_row = 0
    total_amount_lossprofit = 0
    net_change = 0

    # create an empty list to hold the loss/profit column
    list_loss_profit = []

    # Read through each row of data after the header
    for row in csv_reader:
        count_row += 1
        loss_profit = row[1]

        # append the lost/profit column to the list empty list and convert the elements from stringer to integer
        list_loss_profit.append(int(loss_profit))

        # total of loss/profit column
        sum_loss_profit = sum(list_loss_profit)
        total_amount_lossprofit = sum_loss_profit
#print (total_amount_lossprofit)

        # net change: list_loss_profit minus previous change
        previous_change = list_loss_profit[0]
print(previous_change)

        #for i in list_loss_profit:
            #list_loss_profit[i] = list_loss_profit - previous_change
        #print(list_loss_profit)
        
#print(previous_change)

        #total_loss_profit = loss_profit.
#print(list_loss_profit)
#size = len(list_loss_profit)
#print(size)
      
#print(count_row)