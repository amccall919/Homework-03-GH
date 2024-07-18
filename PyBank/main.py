import os
import csv



# Path to collect data from the Resources folder
budget_data = os.path.join("Resources", "budget_data.csv")



#Read in the CSV file
with open(budget_data, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    # Initialize variables
    total_months = 0
    total_sum = 0
    previous_profit_loss = None
    changes = []
    months = []

    # Read through each row of data after the header
    for row in csvreader:
        total_months += 1
        total_sum += int(row[1])

        # Calculate the changes in "Profit/Losses" over the entire period
        current_profit_loss = int(row[1])
        if previous_profit_loss is not None:
            change = current_profit_loss - previous_profit_loss
            changes.append(change)
            months.append(row[0])

        previous_profit_loss = current_profit_loss

    # Calculate the analysis results
    if changes:
        average_change = sum(changes) / len(changes)
        greatest_increase = max(changes)
        greatest_decrease = min(changes)
        greatest_increase_month = months[changes.index(greatest_increase)]
        greatest_decrease_month = months[changes.index(greatest_decrease)]

        # Specify the full output file path
        output_path = os.path.join("Analysis", "financial_analysis.txt")

        # Export the analysis results to the specified text file path
        with open(output_path, "w") as text_file:
            text_file.write("Financial Analysis\n")
            text_file.write("----------------------------\n")
            text_file.write(f"Total Months: {total_months}\n")
            text_file.write(f"Total: ${total_sum}\n")
            text_file.write(f"Average Change: ${average_change:.2f}\n")
            text_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
            text_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

            # Print the analysis results to the terminal
            print("Financial Analysis")
            print("----------------------------")
            print(f"Total Months: {total_months}")
            print(f"Total: ${total_sum}")
            print(f"Average Change: ${average_change:.2f}")
            print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
            print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

        print(f"Financial analysis results have been written to '{output_path}'")
    else:
        print("No data found")