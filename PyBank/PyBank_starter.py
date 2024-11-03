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
previous_profit_loss = 0
net_change_list = []
dates = []
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_profit_loss = int(first_row[1])
    dates.append(first_row[0])

    # Track the total and net change


    # Process each row of data
    for row in reader:
        total_months += 1
        total_net += int(row[1])
        # Track the total


        # Track the net change
        profit_loss = int(row[1])
        net_change = profit_loss - previous_profit_loss
        net_change_list.append(net_change)
        previous_profit_loss = profit_loss
        dates.append(row[0])

        # Calculate the greatest increase in profits (month and amount)
        average_net_change = sum(net_change_list) / len(net_change_list) if net_change_list else 0


        # Calculate the greatest decrease in losses (month and amount)
greatest_increase = max(net_change_list) if net_change_list else 0
greatest_increase_month = dates[net_change_list.index(greatest_increase) + 1] if greatest_increase else ""


# Calculate the average net change across the months
greatest_decrease = min(net_change_list) if net_change_list else 0
greatest_decrease_month = dates[net_change_list.index(greatest_decrease) + 1] if greatest_decrease else ""

# Generate the output summary


# Print the output
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${average_net_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
