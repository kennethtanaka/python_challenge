import os
import csv

# Path to collect data from the Resources folder
bank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Read in the CSV file
with open(bank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # Read the header row first 
    header = next(csvreader)
    print(f"CSV Header: {header}")
    
    # Read each row of data after the header
    total = 0
    count = 0
    num1 = 0
    num2 = 0
    

    for row in csvreader:
        total += int(row[1])  
        count = count + 1  
        num1 = int(row[1])
        nextrow = next(cvsreader)
        num2 = int(row[1])
        num1 = int(row[1])
       
    print (f"Total months: {count}")    
    print (f"Total: ${total}")
    
