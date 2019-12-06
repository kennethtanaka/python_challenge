import os
import csv

count = 0
number_votes = 0
vote = [0,0,0,0]
names = []
greatest = 0

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

        # first time candidate is not in list. then append list of candidates
        # candidates will be in names
        # loop through looking for each candidate and add 1 to vote
        if candidate not in names:
            names.append(candidate)
        if candidate == "Khan":
            vote[0] = vote[0] + 1
        elif candidate == "Correy":
            vote[1] = vote[1] + 1
        elif candidate == "Li":
            vote[2] = vote[2] + 1
        elif candidate == "O'Tooley":
            vote[3] = vote[3] + 1    

    # combine two lists - names and votes into one
    # this will create one list called zip_list with the candidate and number of votes received
    zip_list = list(zip(names,vote))

# find the most votes and the corresponding winner from zip_list    
for x in zip_list:
  if x[1] > greatest:
    greatest = x[1]
    winner = x[0]

#To terminal
print('Election Results')
print('----------------')
print(f'Total Votes: {count}')
print('----------------')
print(f'Khan : {round(vote[0]/count*100,2)}% ({vote[0]})')
print(f'Correy : {round(vote[1]/count*100,2)}% ({vote[1]})')
print(f'Li : {round(vote[2]/count*100,2)}% ({vote[2]})')
print(f"O'Tooley : {round(vote[3]/count*100,2)}% ({vote[3]})")
print('----------------')
print(f'Winner: {winner.upper()}')
print('----------------')

#output txt file
output_file = os.path.join("pypoll_output.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write('Election Results\n')
    datafile.write('----------------\n')
    datafile.write(f'Total Votes: {count}\n')
    datafile.write('----------------\n')
    datafile.write(f'Khan : {round(vote[0]/count*100,2)}% ({vote[0]})\n')
    datafile.write(f'Correy : {round(vote[1]/count*100,2)}% ({vote[1]})\n')
    datafile.write(f'Li : {round(vote[2]/count*100,2)}% ({vote[2]})\n')
    datafile.write(f"O'Tooley : {round(vote[3]/count*100,2)}% ({vote[3]})\n")
    datafile.write('----------------\n')    
    datafile.write(f'Winner: {winner.upper()}\n')
    datafile.write('----------------\n')

    #Close file
    datafile.close()