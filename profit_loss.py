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

        for row in csv_reader:
            
            day = int(row[0])

            net_profit = int(row[4])

            if net_profit < prev_day_net_profit and prev_day_net_profit != 0:

                net_profit_deficit = prev_day_net_profit - net_profit

                net_profit_deficit_details = [day, net_profit_deficit]

                net_profit_deficit_days.append(net_profit_deficit_details)

            elif net_profit > prev_day_net_profit and prev_day_net_profit != 0:

                net_profit_surplus = net_profit - prev_day_net_profit

                if net_profit_surplus > net_profit_highest_surplus:

                    net_profit_highest_surplus = net_profit_surplus

                    net_profit_highest_surplus_day = row[0]

            prev_day_net_profit = net_profit