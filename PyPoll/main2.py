# Import dependencies
import os
import csv
import collections
from collections import Counter

# Define PyPoll's variables
voters_candidates = []
votes_per_candidate = []
total_voters = []


# file location
pypoll_csv = os.path.join("/Users/rodneydavermann/Desktop/python_challenge/PyPoll/Ressources_1/pypoll.csv")

# Open and read the csv file
with open(pypoll_csv) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    print(f"Header: {csv_header}")
    
    # Read through each row of data after the header
    for row in csv_reader:
        
        # append row[0] to total_voters
        total_voters.append(row[0])
        voters_candidates.append(row[2])
        

    # Sort the list by default ascending order
    sorted_list = sorted(voters_candidates)
    
    # Arrange the sorted list by most common outcomes
    arrange_list = sorted_list

    #count votes per candidate in most common outcome order and append to a list
    count_candidate = Counter (arrange_list) 
    votes_per_candidate.append(count_candidate.most_common())

    # percentage votes per candicate 
    for item in votes_per_candidate:
       
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
        fourth = format((item[3][1])*100/(sum(count_candidate.values())),'.3f')
          
    
    
# display results in terminal
print("Election Results")
print("-------------------------")
print (f"Total Votes:  {len(total_voters)}") 
print("-------------------------")
print(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})")
print(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})")
print(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})")
print(f"{votes_per_candidate[0][3][0]}: {fourth}% ({votes_per_candidate[0][3][1]})")
print("-------------------------")
print(f"Winner:  {votes_per_candidate[0][0][0]}")
print("-------------------------")


# analysis file to export
results = open("PyPoll_Results.txt","w")
results.write("Election Results\n")
results.write("-------------------------\n")
results.write(f"Total Votes:  {len(total_voters)}\n")
results.write("-------------------------\n")
results.write(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})\n")
results.write(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})\n")
results.write(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})\n")
results.write(f"{votes_per_candidate[0][3][0]}: {fourth}% ({votes_per_candidate[0][3][1]})\n")
results.write("-------------------------\n")
results.write(f"Winner:  {votes_per_candidate[0][0][0]}\n")
results.write("-------------------------\n")  

 
  
results.close()