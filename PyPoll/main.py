# Modules
import csv
import os

# Relative path to our csv file
csvpath = "PyPoll\Resources\election_data.csv"

# Initialize Counter Variables
Stockham_Votes = 0
DeGette_Votes = 0
Doane_Votes = 0

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)
 
    # loop the CSV
    for row in csvreader:
        #Find the candidate that was voted for in current row
        candidate = str(row[2])

        # Compare candidate value against known list of values
        # Add 1 to appropriate counter depending on vote
        if (candidate == "Charles Casper Stockham"):
            Stockham_Votes += 1
        elif (candidate == "Diana DeGette"):
            DeGette_Votes += 1
        elif (candidate == "Raymon Anthony Doane"):
            Doane_Votes += 1

# Calculate Total and Candidate Percentages
total_votes = Stockham_Votes + DeGette_Votes + Doane_Votes
stockham_percent = (Stockham_Votes / total_votes) * 100
degette_percent = (DeGette_Votes / total_votes) * 100
doane_percent = (Doane_Votes / total_votes) * 100

# Calculate winner based on total votes received
if Stockham_Votes > DeGette_Votes and Stockham_Votes > Doane_Votes:
    winner = "Charles Casper Stockham"
elif DeGette_Votes > Stockham_Votes and DeGette_Votes > Doane_Votes:
    winner = "Diana DeGette"
elif Doane_Votes > Stockham_Votes and Doane_Votes > DeGette_Votes:
    winner = ""

# Output final results to Terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Charles Casper Stockham: {round(stockham_percent,3)}% ({Stockham_Votes})")
print(f"Diana DeGette: {round(degette_percent,3)}% ({DeGette_Votes})")
print(f"Raymon Anthony Doane: {round(doane_percent,3)}% ({Doane_Votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Specify file path for our final text file
file_path = "PyPoll/analysis/"
analysis_file_path = os.path.join(file_path, "analysis.txt")

# Output final results to text file
with open(analysis_file_path,"w") as f:
    print("Election Results", file=f)
    print("-------------------------", file=f)
    print(f"Total Votes: {total_votes}", file=f)
    print("-------------------------", file=f)
    print(f"Charles Casper Stockham: {round(stockham_percent,3)}% ({Stockham_Votes})", file=f)
    print(f"Diana DeGette: {round(degette_percent,3)}% ({DeGette_Votes})", file=f)
    print(f"Raymon Anthony Doane: {round(doane_percent,3)}% ({Doane_Votes})", file=f)
    print("-------------------------", file=f)
    print(f"Winner: {winner}", file=f)
    print("-------------------------", file=f)