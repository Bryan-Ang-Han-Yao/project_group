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

                net_profit_deficit_details = [day, net_profit_deficit]

                net_profit_deficit_days.append(net_profit_deficit_details)

            elif net_profit > prev_day_net_profit and prev_day_net_profit != 0:

                net_profit_surplus = net_profit - prev_day_net_profit

                if net_profit_surplus > net_profit_highest_surplus:

                    net_profit_highest_surplus = net_profit_surplus

                    net_profit_highest_surplus_day = row[0]

            prev_day_net_profit = net_profit

        if len(net_profit_deficit_days) == 0:

            return f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n[HIGHEST NET PROFIT SURPLUS] DAY: {net_profit_highest_surplus_day}, AMOUNT: USD{net_profit_highest_surplus}"
        
        else:

            output = ""

            for day in net_profit_deficit_days:

                output += f"[PROFIT DEFICIT] DAY: {day[0]}, AMOUNT: USD{day[1]}\n"

                return output