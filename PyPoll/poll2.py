import os
import csv

# Path to collect data from the Resources folder
poll_csv = os.path.join('..', 'Resources', 'election_data.csv')

# Read in the CSV file
with open(poll_csv, 'r') as csvfile:
   
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # Read the header row first 
    header = next(csvreader)
    
    count = 0 
    counter = 0
    name = []
    vote = 0

    for row in csvreader:
        count = count + 1
        candidate = (row[2]) 
        
        #check for name of candidates: 
        if candidate not in name:
            # add to list of candidates in name
            name.append(candidate)
            # initialize vote
          
        #add vote for that canditate
        vote[candidate] = vote[candidate] + 1

        
    percent = []
    max_votes = vote[0]
    max = 0

    for x in range(len(name)):
    #calculation to get the percentage, x is the looper value
        vote_pct = round(vote[x]/count*100, 2)
        percent.append(vote_pct)
    
        if candidate_vote[x] > max_votes:
            max_votes = vote[x]
            max_index = x

    winner = candidate_name[max_index] 

  
    #To terminal
print('======================================================')
print('|                  Election Results                  |')
print('======================================================')
print(f'Total Votes: {count}')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for x in range(len(name)):
    print(f'{name[x]} : {percent[x]}% ({vote[x]})')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(f'Election winner: {winner.upper()}')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#output txt file
output_file = os.path.join("pypoll_election_results.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write('======================================================\n')
    datafile.write('|                  Election Results                  |\n')
    datafile.write('======================================================\n')
    datafile.write(f'Total Votes: {count}\n')
    datafile.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    for x in range(len(name)):
        datafile.write(f'{name[x]} : {percent[x]}% ({vote[x]})\n')
    datafile.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    datafile.write(f'Election winner: {winner.upper()}\n')
    datafile.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    datafile.write("---END OF REPORT---")


    