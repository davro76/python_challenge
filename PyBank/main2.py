# import required libraries
import csv
import os
 
# file location
pybank = os.path.join ("/Users/rodneydavermann/Desktop/python_challenge/PyBank/Ressources/pybank.csv")
 
# new list
list_changes = []
period = []
total_amount_lossprofit = []
 
with open (pybank) as csvfile:
    csv_read = csv.reader(csvfile, delimiter = ",")
 
    csv_header = next(csvfile)
     
    # put the data into lists
    for row in csv_read:
        period.append(row[0])
        total_amount_lossprofit.append(int(row[1]))
         
    # number of period
    period_count = len(period)
     
    # variables for loops
    current_value = 1
    previuos = 0
     
    # first monthly change 
    first_change = (total_amount_lossprofit[1]- total_amount_lossprofit[0])
     
     
    # loop through the data set to calculate the average change
    for month in range(period_count-1):
        first_change = (total_amount_lossprofit[current_value] - total_amount_lossprofit[previuos])
        list_changes.append(int(first_change))
        current_value+=1
        previuos+=1
         
     
    # monthly average   
    average_change = round(sum(list_changes)/(period_count -1),2)
 
    # maximum and minimum changes over the period
    minimum_change = min(list_changes)
    maximum_change = max(list_changes)
 
    # list index 
    minimum_index = list_changes.index(minimum_change)
    maximum_index = list_changes.index(maximum_change)
     
    # months for max and min from list of changes
    month_minimum_change = period[minimum_index + 1]
    month_maximum_change = period[maximum_index + 1]
   
 
# display results in terminal
 
print("PyBank Data Financial Analysis")
print("----------------------------")
print(f"Months: {len(period)}")
print(f"Total: ${sum(total_amount_lossprofit)}")
print(f"Average Monthly Change: {average_change}")
print(f"Greatest Increase in Profits: {month_maximum_change} (${maximum_change})")
print(f"Greatest Decrease in Profits: {month_minimum_change} (${minimum_change})")
 
# analysis file to export
result = open("PyBank_Results.txt","w")
 
result.write(" PyBank Data Financial Analysis\n")
result.write("----------------------------\n")
result.write(f"Months: {len(period)}\n")
result.write(f"Total: ${sum(total_amount_lossprofit)}\n")
result.write(f"Average Monthly Change: {average_change}\n")
result.write(f"Greatest Increase in Profits: {month_maximum_change} (${maximum_change})\n")
result.write(f"Greatest Decrease in Profits: {month_minimum_change} (${minimum_change})\n")
 
  
result.close()