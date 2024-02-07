from pathlib import Path 
import csv
import os

# Script for CSV path
csv_path = os.path.join("/Users/jennyposso/Downloads/module 3/PyPoll/Resources/election_data.csv")

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        print(row)

total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

with open(csv_path,newline="", encoding="utf-8") as elections:
    csvreader = csv.reader(elections,delimiter=",") 

   
    header = next(csvreader)     
    for row in csvreader: 
         total_votes +=1
         if row[2] == "Khan": 
            khan_votes +=1
         elif row[2] == "Correy":
            correy_votes +=1
         elif row[2] == "Li": 
            li_votes +=1
         elif row[2] == "O'Tooley":
            otooley_votes +=1

candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)


khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")


output_directory = os.path.join("/Users/jennyposso/Downloads/module 3/")
os.makedirs(output_directory, exist_ok=True)

# Create a text file and write the financial analysis results
output_file_path = os.path.join(output_directory, "Election_Winner.txt")
with open(output_file_path, 'w') as file:
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("----------------------------\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})\n")
    file.write("----------------------------\n")
    file.write(f"Winner: {key}\n")
    file.write("----------------------------\n")

# Print the file path where the results are saved
print(f"Election results have been saved to '{output_file_path}'")
# Assign output file location and with the pathlib library