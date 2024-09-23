# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
net_changes = [] # my idea is to create a list that put all the net changes inside this list

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)   # it just to read for the row after header
    first_row = next(reader)  #read the first data row
    total_months += 1  #count the first month

    # Extract first row to avoid appending to net_change_list
    print(f"Header: {header}")
    previous_price = int(first_row[1]) #this is to get the first Profit/loss
    total_net += previous_price #add the first month's value to the total net
    greatest_increase = ["", 0] #set the format of [month, amount]
    lowest_increase = ["", 0] #set the format of [month, amount]
    # Track the total and net change
    # Process each row of data
    for row in reader:
        # Track the total
        total_months += 1 #increase the month by counting 1
        current_price = int(row[1]) #get the current month's profit/loss
        total_net += current_price #add to the total net

        # Track the net change
        net_change = int(row[1]) - previous_price #formula
        previous_price = current_price #previous price equal to current price
        net_changes.append(net_change) #put all the new net changes into list


        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase[1]:
            greatest_increase = [row[0], net_change] # if this condition is true, in greatest_increase list, it will find the greatest value

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < lowest_increase[1]:
            lowest_increase = [row[0], net_change] # if this condition is true, in lowest_increase list, it will find the lowest value


# # Calculate the average net change across the months

    # avg = sum(of the net change) / len(net change list) 

    avg_net_change = sum(net_changes) / len(net_changes) 

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${avg_net_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {lowest_increase[0]} (${lowest_increase[1]})"
)

# Print the output
print(output)

# # Write the results to a text file
with open(file_to_output, "w") as txt_file:
     txt_file.write(output)
