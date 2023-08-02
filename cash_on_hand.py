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

            # To retrive day number and convert it into an integer
            day = int(row[0])

            # To retrive cash on hand amount and convert it into an integer
            cash_on_hand = int(row[1])

            # Checks if the current day cash on hand is less than previous day cash on hand
            if cash_on_hand < prev_day_cash:

                # To calculate the deficit between two days
                COH_deficit = prev_day_cash - cash_on_hand

                # To store the the details of the deficit cash on hand by, "day", "COH_deficit"
                COH_deficit_details = [day, COH_deficit]

                # Appends the cash on hand deficits into a list
                COH_deficit_days.append(COH_deficit_details)

            # Checks if the current day cash on hand is more than previous day cash on hand, exlcuding the first day
            elif cash_on_hand > prev_day_cash and prev_day_cash != 0:
                
                # To calculate the surplus between two days
                COH_surplus = cash_on_hand - prev_day_cash

                # Checks if surplus is more than current highest surplus
                if COH_surplus > COH_highest_surplus:

                    # Set the new highest surplus
                    COH_highest_surplus = COH_surplus

                    # Retrive the day of the highest surplus
                    COH_highest_surplus_day = row[0]

            # Set new previous day        
            prev_day_cash = cash_on_hand

        # Checks if "COH_deficit_days" list is empty    
        if len(COH_deficit_days) == 0:

            # Return the formatted the final output using 'f' string
            return f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n[HIGHEST CASH SURPLUS] DAY: {COH_highest_surplus_day}, AMOUNT: USD{COH_highest_surplus}\n"
        
        else:

            # Declares the variable to format the output
            output = ""

            # To iterate through each days where cash on hand deficit can be found
            for day in COH_deficit_days:

                # Adds each deficit days to the output
                output += f"[CASH DEFICIT] DAY: {day[0]}, AMOUNT: USD{day[1]}\n"

            # Returns the formatted output
            return output