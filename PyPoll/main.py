# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#direct to the folder struction ('.' = current folder, '..' = up a folder)
csvpath = os.path.join(".", "Resources", "election_data.csv")


# Read CSV file as a series of lists

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)
    

    #create placeholder values for counts
    count = 0
    runtot = 0
    kcount = 0
    ccount = 0
    lcount = 0
    ocount = 0 

    # Read each row of data after the header
    for row in csvreader:
        #add one to the count(vote count) for each row
        count = count + 1
        #add one to the count for each candiate if their name appears in the 3rd element of each row
        if row[2] == "Khan":
            kcount = kcount + 1
        if row[2] == "Correy":
            ccount = ccount + 1
        if row[2] == "Li":
            lcount = lcount + 1
        if row[2] == "O'Tooley":
            ocount = ocount + 1
#this is a clunky approach, but compares vote count and declares winner 
if kcount > ccount and kcount > lcount and kcount > ocount:
    winner = "Khan"
if ccount > kcount and ccount > lcount and ccount > ocount:
    winner = "Correy"
if lcount > kcount and lcount > ccount and lcount > ocount:
    winner = "Li"
if ocount > kcount and ocount > ccount and ocount > lcount:
    winner = "O'Tooley"

#print results
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(count))
print("-------------------------")
print("Khan: " + str(round((kcount/count)*100, 4)) + "% (" + str(kcount) +")")
print("Correy: " + str(round((ccount/count)*100, 4)) + "% (" + str(ccount) +")")
print("Li: " + str(round((lcount/count)*100, 4)) + "% (" + str(lcount) +")")
print("O'Tooley: " + str(round((ocount/count)*100, 4)) + "% (" + str(ocount) +")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

#create path to output folder
output_path = os.path.join(".", "output", "election_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, "w", newline="") as results:
    #Linux/Unix line endings
    results.writelines("Election Results\n")
    results.writelines("-------------------------\n")
    results.writelines("Total Votes: " + str(count) + "\n")
    results.writelines("-------------------------")
    results.writelines("Khan: " + str(round((kcount/count)*100, 4)) + "% (" + str(kcount) +")\n")
    results.writelines("Correy: " + str(round((ccount/count)*100, 4)) + "% (" + str(ccount) +")\n")
    results.writelines("Li: " + str(round((lcount/count)*100, 4)) + "% (" + str(lcount) +")\n")
    results.writelines("O'Tooley: " + str(round((ocount/count)*100, 4)) + "% (" + str(ocount) +")\n")
    results.writelines("-------------------------\n")
    results.writelines("Winner: " + winner + "\n")
    results.writelines("-------------------------\n")
    