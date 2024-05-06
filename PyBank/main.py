# Modules
import csv
import os

# Relative path to our csv file
csvpath = "PyBank/Resources/budget_data.csv"

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)

    # Initializing the first row of the dataset as a variable so that we can call its values for variables below
    # This means our for loop will not be reading the first row's data, so we initialize all our variables with this data to account for that
    first_row = next(csvreader)

    # Initialize our first variables
    months = 1
    total_amount = int(first_row[1])
    profit_changes = [] # Track changes in a list to calculate average at the end (sum of list / len of list)
    
    # We need to track the previous value to iterate properly for change tracking
    previous_amount = int(first_row[1])
    increase =  int(first_row[1])
    increase_date = str(first_row[0])
    decrease =  int(first_row[1])
    decrease_date = str(first_row[0])

    # loop the CSV
    for row in csvreader:
        # add each row amount to our total amount
        total_amount += int(row[1])
        # Expected result is amount of rows in dataset without header, so add 1 per loop
        months += 1

        profit_amount = int(row[1]) # Current amount value for change tracking

        change = profit_amount - previous_amount
        profit_changes.append(change) # Add this change to our running list, will be used in averaging later

        if change > increase:
            increase = change
            increase_date = str(row[0])
        elif change < decrease:
            decrease = change
            decrease_date = str(row[0])

        previous_amount = profit_amount

# Calculate Average Change over dataset
avg_change = sum(profit_changes) / len(profit_changes)

# Output final results to Terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${round(avg_change,2)}")
print(f"Greatest Increase in Profits: {increase_date} (${increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${decrease})")

# Specify file path for our final text file
file_path = "PyBank/analysis/"
analysis_file_path = os.path.join(file_path, "analysis.txt")

# Output final results to text file
with open(analysis_file_path,"w") as f:
    print("Financial Analysis", file=f)
    print("----------------------------", file=f)
    print(f"Total Months: {months}", file=f)
    print(f"Total: ${total_amount}", file=f)
    print(f"Average Change: ${round(avg_change,2)}", file=f)
    print(f"Greatest Increase in Profits: {increase_date} (${increase})", file=f)
    print(f"Greatest Decrease in Profits: {decrease_date} (${decrease})", file=f)