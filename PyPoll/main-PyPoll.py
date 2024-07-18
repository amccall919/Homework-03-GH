import os
import csv

# Path to collect data from the Resources folder
pypoll_data = ("Resources/election_data.csv")

# Create a set to store the unique candidate names
candidates_set = set()

# Read the csv file and store the data in a list
rows = []

# Open the csv file
with open(pypoll_data, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Read the csv file and store the data in a list
    for row in csvreader:
        rows.append(row)

    # Calculate the total number of votes cast
    total_votes = len(rows)

    # Extract candidate names and count the votes for each candidate
    candidate_votes = {}
    for line in rows:
        candidate = line[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

    # Determine the winner based on popular vote
    winner = max(candidate_votes, key=candidate_votes.get)
       

# Print Election Results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
    
# Print the results for each candidate in the terminal
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


output_path = os.path.join ("Analysis", "PyPoll_Analysis.txt")

# Write the results to a text file and print to the terminal
with open(output_path, "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")

    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        #print(f"{candidate}: {percentage:.3f}% ({votes})")
        
        
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

        
        
        