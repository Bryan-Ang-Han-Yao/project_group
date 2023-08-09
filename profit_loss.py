from pathlib import Path
import csv

# Creates a path to csv file
file_path = Path.cwd()/"csv_reports"/"Profits_and_Loss.csv"

def Profit_and_Loss_identifier():
    """
    - Identifies the day(s) with Net Profit deficit or day with highest Net Profit surplus
    - No parameter is required
    """

    # Opens and reads the csv file
    with file_path.open(mode = 'r', encoding="UTF-8", newline="") as csv_file:
        csv_reader = csv.reader(csv_file)

        # Skips the header
        next(csv_reader)

        # Create an empty lists to store days with Net Profit deficit
        net_profit_deficit_days = []

        # Create a variable to store the previous day Net Profit
        prev_day_net_profit = 0

        # Create a variable to store the highest surplus in Net Profit
        net_profit_highest_surplus = 0

        # To iterate through the CSV file
        for row in csv_reader:
            
            # To retrive day number and convert it into an integer
            day = int(row[0])

            # To retrive net profit amount and convert it into an integer
            net_profit = int(row[4])

            # Checks if the current day net profit is less than previous day net profit, exlcuding the first day
            if net_profit < prev_day_net_profit and prev_day_net_profit != 0:

                # To calculate the deficit between two days
                net_profit_deficit = prev_day_net_profit - net_profit

                # To store the the details of the deficit net profit by, "day", "net_profit_deficit"
                net_profit_deficit_details = [day, net_profit_deficit]

                # Appends the net profits deficits into a list
                net_profit_deficit_days.append(net_profit_deficit_details)

            # Checks if the current day net profit is more than previous day net profit, exlcuding the first day
            elif net_profit > prev_day_net_profit and prev_day_net_profit != 0:

                # To calculate the surplus between two days
                net_profit_surplus = net_profit - prev_day_net_profit

                # Checks if surplus is more than current highest surplus
                if net_profit_surplus > net_profit_highest_surplus:

                    # Set the new highest surplus
                    net_profit_highest_surplus = net_profit_surplus

                    # Retrive the day of the highest surplus
                    net_profit_highest_surplus_day = row[0]

            # Set new previous day
            prev_day_net_profit = net_profit

        # Checks if "net_profit_deficit_days" list is empty
        if len(net_profit_deficit_days) == 0:

            # Return the formatted the final output using 'f' string
            return f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n[HIGHEST NET PROFIT SURPLUS] DAY: {net_profit_highest_surplus_day}, AMOUNT: USD{net_profit_highest_surplus}"
        
        else:

            # Declares the variable to format the output
            output = ""

            # To iterate through each days where net profit deficit can be found
            for day in net_profit_deficit_days:

                # Adds each deficit days to the output.
                output += f"[PROFIT DEFICIT] DAY: {day[0]}, AMOUNT: USD{day[1]}\n"

            # Returns the formatted output
            return output