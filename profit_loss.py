from pathlib import Path
import csv

file_path = Path.cwd()/"csv_reports"/"Profits_and_Loss.csv"

def Profit_and_Loss_identifier():
    with file_path.open(mode = 'r', encoding="UTF-8", newline="") as csv_file:

        csv_reader = csv.reader(csv_file)

        net_profit_deficit_days = []

        prev_day_net_profit = 0