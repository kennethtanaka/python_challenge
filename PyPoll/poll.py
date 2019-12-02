import os
import csv
import collections as ct
candidate = []
count = 0 

# Path to collect data from the Resources folder
poll_csv = os.path.join('..', 'Resources', 'election_data.csv')

# Read in the CSV file
with open(poll_csv, 'r') as csvfile:
    votes = ct.Counter()
   
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # Read the header row first 
    header = next(csvreader)
    
    for row in csvreader:
        count = count + 1 
        candidate = row[-1]
        votes[candidate] += 1
    
    Khan = int(votes.get('Khan'))
    Correy = votes.get('Correy')
    Li = votes.get('Li')
    OTooley = votes.get("O'Tooley")
    

    
    print('Election Result')
    print('---------------')
    print(f"Total Votes: {count}")
    print('---------------')
    print(f"{votes}")   

    print(Khan)
    
