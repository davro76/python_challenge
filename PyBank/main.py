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

    # initialize variables 
    count_row = 0
    total_amount_lossprofit = 0
    net_change = 0
    first_loss_profit_value = 0


    # create empty lists to hold the loss/profit column and net change
    list_loss_profit = []
    list_net_change = []
    
    # Read through each row of data after the header
    for row in csv_reader:
        count_row += 1
        loss_profit = row[1]
        
        # append the lost/profit column to the list empty list and convert the elements from stringer to integer
        list_loss_profit.append(int(loss_profit))

        # total of loss/profit column
        sum_loss_profit = sum(list_loss_profit)
        total_amount_lossprofit = sum_loss_profit


        # net change: list_loss_profit minus previous change
        previousvalue = list_loss_profit[0]
        net_change = int(row[1]) - previousvalue
        list_net_change.append(net_change)
#print(list_net_change)
#size = max(list_net_change)
#print(list_net_change)
print(min(list_net_change))
        # average net change
        #average_net_change = net_change / count_row


        
      
#print calculated variables 
#print(count_row)
#print (total_amount_lossprofit)
#print(net_change)
#print(average_net_change)