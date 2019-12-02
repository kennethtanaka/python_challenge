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
    print(list)
    # Read each row of data after the header
    total = 0
    count = 0
    sum1 = 0
    sum2 = 0
    delta = 0
    totaldelta = 0
   
       
                
    print (f"Total months: {count}")    
    print (f"Total: ${total}")
    print (f"Total delta: {totaldelta}") 
    print (f"sum1: {sum1}") 
    print (f"sum2: {sum2}") 