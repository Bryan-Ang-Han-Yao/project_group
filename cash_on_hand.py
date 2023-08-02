from pathlib import Path
import csv

# Creates a path to csv file
file_path = Path.cwd()/"csv_reports"/"Cash_on_Hand.csv"

def COH_identifier():
    """
    - Identifies the day(s) with cash on hand deficit or day with highest cash on hand surplus
    - No parameter is required
    """

    # Opens and reads the csv file
    with file_path.open(mode = 'r', encoding="UTF-8", newline="") as csv_file:
        csv_reader = csv.reader(csv_file)

        # Skips the header
        next(csv_reader)

        # Create an empty lists to store days with cash on hand deficit
        COH_deficit_days = []

        # Create a variable to store the previous day cash on hand
        prev_day_cash = 0

        # Create a variable to store the highest surplus in cash on hand
        COH_highest_surplus = 0

        # To iterate through the CSV file
        for row in csv_reader:
            day = int(row[0])
            cash_on_hand = int(row[1])
            if cash_on_hand < prev_day_cash:
                COH_deficit = prev_day_cash - cash_on_hand
                COH_deficit_details = [day, COH_deficit]
                COH_deficit_days.append(COH_deficit_details)
            elif cash_on_hand > prev_day_cash and prev_day_cash != 0:
                COH_surplus = cash_on_hand - prev_day_cash
                if COH_surplus > COH_highest_surplus:
                    COH_highest_surplus = COH_surplus
                    COH_highest_surplus_day = row[0]
                    
            prev_day_cash = cash_on_hand
            
        if len(COH_deficit_days) == 0:
            return f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n[HIGHEST CASH SURPLUS] DAY: {COH_highest_surplus_day}, AMOUNT: USD{COH_highest_surplus}\n"
        else:
            output = ""
            for day in COH_deficit_days:
                output += f"[CASH DEFICIT] DAY: {day[0]}, AMOUNT: USD{day[1]}\n"
            return output