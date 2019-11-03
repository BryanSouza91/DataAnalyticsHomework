import os
import csv

# Define path to csv 
csvpath = os.path.join("Resources", "election_data.csv")
# Read csv file
with open(csvpath, 'r') as csvfile:
# Split data
    csvreader = csv.reader(csvfile, delimiter=',')
    
# Define variables
    tot_votes = 0
# List to store unique candidates
    candidates = []
# Dictionaries to store 
    votes_by_cand = {}
    perc_votes = {}
# Store winner as string
    winner = ""
    
# Store csv data into List of Lists
    data = [row for row in csvreader]
# loop through the data
    for i in range(1,len(data)):
# Remove unused data 
        del data[i][1]
# Tally total votes
        tot_votes += 1
# Form list of unique candidates
        if data[i][1] not in candidates: 
            candidates.append(data[i][1])
# Form dict of votes for each candidate
    votes_by_cand = {c:[] for c in candidates}
# Loop through candidates
    for j in range(len(candidates)):
        for i in range(1,len(data)):
            if data[i][1] == candidates[j]:
                votes_by_cand[candidates[j]].append(data[i][0])
# Replace voter IDs with number of voter IDs
        votes_by_cand[candidates[j]] = len(votes_by_cand[candidates[j]])
        perc_votes[candidates[j]] = round(((votes_by_cand[candidates[j]]/tot_votes)*100),3)
# Find winner through max function
    winner = max(votes_by_cand, key=votes_by_cand.get)    
# Print report to terminal and .txt
print("Election Results")
print("-----"*8)
print(f"Total Votes:                     {tot_votes}")
print("-----"*8)
print(f"Khan:                   {perc_votes['Khan']}%    {votes_by_cand['Khan']}")
print(f"Correy:                 {perc_votes['Correy']}%    {votes_by_cand['Correy']}")
print(f"Li:                     {perc_votes['Li']}%    {votes_by_cand['Li']}")
print("O'Tooley:               "+str(perc_votes["O'Tooley"])+"%     "+str(votes_by_cand["O'Tooley"]))
print("-----"*8)
print(f"Winner:                          {winner}")
print("-----"*8)
with open("pypoll.txt", "w") as text_file:
    print("Election Results",file=text_file)
    print("-----"*8,file=text_file)
    print(f"Total Votes:                     {tot_votes}",file=text_file)
    print("-----"*8,file=text_file)
    print(f"Khan:                   {perc_votes['Khan']}%    {votes_by_cand['Khan']}",file=text_file)
    print(f"Correy:                 {perc_votes['Correy']}%    {votes_by_cand['Correy']}",file=text_file)
    print(f"Li:                     {perc_votes['Li']}%    {votes_by_cand['Li']}",file=text_file)
    print("O'Tooley:               "+str(perc_votes["O'Tooley"])+"%     "+str(votes_by_cand["O'Tooley"]),file=text_file)
    print("-----"*8,file=text_file)
    print(f"Winner:                          {winner}",file=text_file)
    print("-----"*8,file=text_file) 