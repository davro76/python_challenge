# import packages
import csv
import os

# data path
PyPoll = os.path.join("/Users/rodneydavermann/Desktop/python_challenge/PyPoll/Ressources/pypoll.csv")
 
 # list_all_candidate
unique_candidate_list = []
candidates = []

# initialize variables 
count_row = 0
Khan_number_votes = 0
Correy_number_votes = 0
Li_number_votes = 0
OTooley_number_votes = 0

# Open and read the pypoll.csv
with open(PyPoll) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Read the header row first 
    csv_header = next(csv_file)

 # Read through each row of data after the header
    for row in csv_reader:
        count_row += 1

        
    

        # use the set property to get unique items from candidates list
        #candidates_set = set(candidates)
        #unique_candidate_list =(list(candidates_set))
        #print(unique_candidate_list) 
        

        # all candidates list    
#print(candidates)
print(count_row)
 # assign values from column 3 to a list
candidates.append(row[2])
for i in candidates:
    if i not in unique_candidate_list:
        unique_candidate_list.append(i)
print(unique_candidate_list)
    






