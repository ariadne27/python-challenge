#This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
import re

#add dictionary (may update with an import version of the dictionary)
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Create output file
output_path = os.path.join(".", "output", "employee_data_rev.csv")
with open(output_path, "w", newline="") as reformat:
    newformat = csv.writer(reformat, delimiter=',')
    newformat.writerow(["Emp ID", "First Name","Last Name","DOB","SSN","State"])

    # open file to be read
    csvpath = os.path.join('.', 'resources', 'employee_data.csv')
    with open(csvpath, newline='') as csvfile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        # Read the header row first (skip this step if there is now header)
        csv_header = next(csvreader)
    
        # Read each row of data after the header
        for row in csvreader:
            #save row elements to variables
            fullname = row[1]
            dob = row[2]
            ssn = row[3]
            statef = row[4]
            #split the name variables
            namesplit = re.split(" ", fullname)
            firstname = namesplit[0]
            lastname = namesplit[1]
            #split the date variables
            datesplit = re.split("-", dob)
            year = datesplit[0]
            month = datesplit[1]
            day = datesplit[2]
            #split the SSN variable
            ssnsplit = re.split("-", ssn)
            last4 = ssnsplit[2]
            
            #pulling state abbrev from dictionary
            #adding to end of row
            stateabbv = us_state_abbrev[statef]

            #write over existing elements with new variables
            #append additional element to the end of the list
            row[1] = firstname
            row[2] = lastname
            row[3] = month + "/" + day + "/" + year
            row[4] = "***-**-" + last4
            row.append(stateabbv)
            #write to output row
            newformat.writerow(row)

 