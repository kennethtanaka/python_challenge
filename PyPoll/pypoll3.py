import os
import csv

count = 0
number_votes = 0
vote = []
names = []

# Path to collect data from the Resources folder
poll_csv = os.path.join('..', 'Resources', 'election_data.csv')

# Read in the CSV file
with open(poll_csv, 'r') as csvfile:
   
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # Read the header row first 
    header = next(csvreader)
    
    for row in csvreader:
        # total votes  
        count = count + 1 
        #read in the candidate from column 3
        candidate = (row[2])

        if candidate in names:
        # Returns the index of the first object with a matching candidate name
            names_index = names.index(candidate)
            vote[names_index] = vote[names_index] + 1
        else:
        # first time candidate is not in list. then append list of candidates 
        # and add 1 to vote list
            names.append(candidate)
            vote.append(1)
               
pct = []
max_votes = vote[0]
max_index = 0

# Returns the number of candiates from list names
for x in range(len(names)):
    #calculation to get the percentage
    vote_pct = round(vote[x]/count*100, 2)
    pct.append(vote_pct)
    
    if vote[x] > max_votes:
        max_votes = vote[x]
        max_index = x

election_winner = names[max_index] 

#To terminal
print('Election Results')
print('----------------')
print(f'Total Votes: {count}')
print('----------------')
for x in range(len(names)):
    print(f'{names[x]} : {pct[x]}% ({vote[x]})')
print('----------------')
print(f'Winner: {election_winner.upper()}')
print('----------------')


#output txt file
output_file = os.path.join("pypoll_output.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write('Election Results\n')
    datafile.write('----------------\n')
    datafile.write(f'Total Votes: {count}\n')
    datafile.write('----------------\n')
    for x in range(len(names)):
        datafile.write(f'{names[x]} : {pct[x]}% ({vote[x]})\n')
    datafile.write('----------------\n')    
    datafile.write(f'Winner: {election_winner.upper()}\n')
    datafile.write('----------------\n')

    # Close file
    datafile.close()