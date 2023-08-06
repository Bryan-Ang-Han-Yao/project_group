from pathlib import Path
import csv

file_path = Path.cwd()/"csv_reports"/"Profits_and_Loss.csv"

def Profit_and_Loss_identifier():
    with file_path.open(mode = 'r', encoding="UTF-8", newline="") as csv_file:

        csv_reader = csv.reader(csv_file)

        net_profit_deficit_days = []

        prev_day_net_profit = 0

        net_profit_highest_surplus = 0

        for row in csv_reader:
            
            day = int(row[0])

            net_profit = int(row[4])

            if net_profit < prev_day_net_profit and prev_day_net_profit != 0:

                net_profit_deficit = prev_day_net_profit - net_profit