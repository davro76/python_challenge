# Import dependencies
import os
import csv
from collections import Counter

# Define PyPoll's variables
candidates_list = []
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
        candidates_list.append(row[2])
        

    # candidates list by ascending order
    sorted_list = sorted(candidates_list)
    arrange_list = sorted_list

    # number of votes for each candidate
    count_candidate = Counter (arrange_list) 
    votes_per_candidate.append(count_candidate.most_common())

    # percentage 
    for item in votes_per_candidate:
       
        candidate_index_0 = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        candidate_index_1 = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        candidate_index_2 = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
        candidate_index_3 = format((item[3][1])*100/(sum(count_candidate.values())),'.3f')
          
    
    
# display results in terminal
print("Election Results")
print("-------------------------")
print (f"Total Votes:  {len(total_voters)}") 
print("-------------------------")
print(f"{votes_per_candidate[0][0][0]}: {candidate_index_0}% ({votes_per_candidate[0][0][1]})")
print(f"{votes_per_candidate[0][1][0]}: {candidate_index_1}% ({votes_per_candidate[0][1][1]})")
print(f"{votes_per_candidate[0][2][0]}: {candidate_index_2}% ({votes_per_candidate[0][2][1]})")
print(f"{votes_per_candidate[0][3][0]}: {candidate_index_3}% ({votes_per_candidate[0][3][1]})")
print("-------------------------")
print(f"Winner:  {votes_per_candidate[0][0][0]}")
print("-------------------------")


# analysis file to export
results = open("PyPoll_Results.txt","w")
results.write("Election Results\n")
results.write("-------------------------\n")
results.write(f"Total Votes:  {len(total_voters)}\n")
results.write("-------------------------\n")
results.write(f"{votes_per_candidate[0][0][0]}: {candidate_index_0}% ({votes_per_candidate[0][0][1]})\n")
results.write(f"{votes_per_candidate[0][1][0]}: {candidate_index_1}% ({votes_per_candidate[0][1][1]})\n")
results.write(f"{votes_per_candidate[0][2][0]}: {candidate_index_2}% ({votes_per_candidate[0][2][1]})\n")
results.write(f"{votes_per_candidate[0][3][0]}: {candidate_index_3}% ({votes_per_candidate[0][3][1]})\n")
results.write("-------------------------\n")
results.write(f"Winner:  {votes_per_candidate[0][0][0]}\n")
results.write("-------------------------\n")  
  
results.close()