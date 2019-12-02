import os
import csv

# Path to collect data from the Resources folder
bank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Read in the CSV file


with open(bank_csv, 'r') as f:

    csvReader = csv.reader(f)
    max_increase_row = max(csvReader, key=lambda row: int(row[1]))
    best_date = max_increase_row[0]
    print(f"Greatest Increase in Profits:  + {best_date} {max_increase_row}")

for row in csvReader:
    Revenue.append(row[1])
max_profit = max(Revenue, key=int)        

################################################
avg=[]
    for row in csvreader:
        num1 = int(row[1])  
        num2 = int(row[1])
        difference = (num2 - num1) 
        avg.append(difference)
    totalavg = mean(avg)

####################################################
    revenue.append(int(row[1]))
        max_profit = max(revenue)