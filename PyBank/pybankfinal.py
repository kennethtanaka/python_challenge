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
    
    
    # Read each row of data after the header
    
    total = 0
    count = 0
    num1 = 0
    num2 = 0
    total = 0
    delta = 0
    difference = 0
    maxdelta = 0
    mindelta = 0
    maxdeltadate = 0
    mindeltadate = 0
    

    for row in csvreader:
        count = count + 1 
               
        #calculates total revenue
        total = total + (int(row[1]))
               
        #create a variable that will count the revenue change
        delta = int(row[1]) - num1
        num2 = int(row[1])
        difference = delta + difference      

        #find greatest increase/decrease profit change and date                                  
        if delta > maxdelta:
            maxdelta = delta
            maxdeltadate = row[0]
        if delta < mindelta:
            mindelta = delta
            mindeltadate = row[0]
    
    num2 = num1

    #calculate the average change in revenue
    avgdelta = round(difference/((count)-1))
    print (f"total delta :{difference}")          
    print (f"Total months: {count}")    
    print (f"Total: ${total}")
    print (f"Average Change: {avgdelta}")
    print (f"Greatest Increase in Profits: {maxdeltadate} {maxdelta}")
    print (f"Greatest Decrease in Profits: {mindeltadate} {mindelta}")

#Output final results to txt file
with open("pybank.txt","w") as txtfile:
    txtfile.write(f"Total months: {count}\n")
    txtfile.write(f"Total: ${total} \n")
    txtfile.write(f"Average Change: ${avgdelta}\n")
    txtfile.write(f"Greatest Increase in Profits: {maxdeltadate} {maxdelta}\n")
    txtfile.write(f"Greatest Decrease in Profits: {mindeltadate} {mindelta}\n")

    # Close file
    txtfile.close()
