#Imports

import csv
import os

#Path Connection

csv_path = os.path.join("/Users/jennyposso/Downloads/module 3/PyBank/Resources/budget_data.csv")

with open(csv_path) as csvfile:
    csvread = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvread)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
    print(row)

# Total months
with open(csv_path, 'r') as fp:
lines = sum(1 for line in fp) - 1

# Total Profit/Losses
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
netchange_list = []

with open(csv_path, 'r') as fp:
    csvfile = csv.reader(fp)
    header_row = next(csvfile)
    first_row = next(csvfile)
    first_r = int(first_row[1])
    aveChange = int(first_row[1])

    for row in csvfile:
        first_r += int(row[1])
        netchange = (int(row[1]) - aveChange) 
        aveChange = int(row[1])
        netchange_list += [netchange]
        sum(netchange_list)
        Sum_List = sum(netchange_list) / (len(netchange_list))  
# Greatest increase and decrease
if netchange > greatest_increase[1]:
    greatest_increase[0] = row[0]
    greatest_increase[1] = netchange
if netchange < greatest_decrease[1]:
    greatest_decrease[0] = row[0]
    greatest_decrease[1] = netchange

print("Total: $" + str(first_r))  
print("Average Change: $" + str(round(Sum_List, 2)))  
print(greatest_decrease)  

# Create the target directory if it doesn't exist
output_directory = os.path.join("/Users/jennyposso/Downloads/module 3/")
os.makedirs(output_directory, exist_ok=True)

# Create a text file and write the financial analysis results
output_file_path = os.path.join(output_directory, "Finance.txt")

with open(output_file_path, 'w') as txt_file:
    txt_file.write("Finance\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Months: {lines}\n")
    txt_file.write(f"Total: ${first_r}\n")
    txt_file.write(f"Average Change: ${Sum_List:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the file path where the results are saved
print(f"Financial analysis results have been saved to '{output_file_path}'")
