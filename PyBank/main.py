# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# assign path to where the csv file is held
csvpath = os.path.join('.', 'resources', 'budget_data.csv')


# Read CSV file as a series of lists
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # assign placeholder values to all variables
    count = 0
    runtot = 0
    prevmonth = 0
    diff = 0
    rundiff = 0
    prevmonthdiff = 0
    diffmax = 0
    diffmin = 0
    # Read each row of data after the header
    for row in csvreader:
        #create a running total of the profit/loss values
        runtot = int(row[1])+ runtot
        #increase the count by one for each row
        count = count + 1
        #for the first row of data
        if count == 1:
            diff = 0
            #assign a new value for prevmonth profit/loss
            prevmonth = int(row[1])
        #for all other rows
        else:    
            #calculate the difference between this row profit/loss and the previous row's profit/loss (prevmonth)
            diff = int(row[1])-prevmonth
            #change the value of prevmonth to the value of the current row's profit/loss
            prevmonth = int(row[1])
            #change the value of rundiff to the sum of the current diff and the previous value of rundiff
            rundiff = diff + rundiff
            #change value of the prevmonthdiff to the current value of diff
            prevmonthdiff = diff
            #if the current diff is greater than the previously found maxium diff
            #then capture the value and the date
            if diff > diffmax:
                diffmax = diff
                maxdate = row[0]
            #if the current diff is less than the previously found minimum diff
            #then capture the value and the date
            if diff < diffmin:
                diffmin = diff
                mindate = row[0]
#Calculate average change and round to two places
avchange = round((rundiff / (count - 1)),2)
#Terminal output
print("\n")
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(count))
print("Total: $" + str(runtot))
print("Average Change : $" + str(avchange))
print("Greatest Increase in Profits: " + maxdate + " ($" + str(diffmax) + ")")
print("Greatest Decrease in Profits: " + mindate + " ($" + str(diffmin) + ")")

#create path to output folder
output_path = os.path.join(".", "output", "banking_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, "w", newline="") as results:
    #Linux/Unix line endings
    results.writelines("\n")
    results.writelines("Financial Analysis\n")
    results.writelines("----------------------------\n")
    results.writelines("Total Months: " + str(count) + "\n")
    results.writelines("Total: $" + str(runtot) + "\n")
    results.writelines("Average Change : $" + str(avchange) + "\n")
    results.writelines("Greatest Increase in Profits: " + maxdate + " ($" + str(diffmax) + ")\n")
    results.writelines("Greatest Decrease in Profits: " + mindate + " ($" + str(diffmin) + ")\n")
    


    
