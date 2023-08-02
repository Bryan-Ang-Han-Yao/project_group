from pathlib import Path
import csv

# Create a path to csv file
file_path = Path.cwd()/"csv_reports"/"Overheads.csv"

def overheads_identifier():
    """
    - Identifies the highest expense category and its overhead percentage
    - No parameters required
    """

    # Opens and reads the csv file
    with file_path.open(mode="r", encoding="UTF-8", newline="") as csv_file:
        csv_reader = csv.reader(csv_file)

        # Skips the header
        next(csv_reader)

        # Create an empty lists to store overheads records
        overheadsRecords = [] 

        # Iterates through the rows in the "Overheads.csv" file
        for row in csv_reader:

            # Retrieve the overhead category for each record
            overhead_category = row[0].strip()

            # Retrieve the overheard percentage for each record and converting it to a float
            overhead_percentage = float(row[1])

            # Appends the overhead category and overheard percentage to the "overheadsRecords" list
            overheadsRecords.append([overhead_category, overhead_percentage])

        # Finds the row with the highest value in the overheads column
        highest_overhead = max(overheadsRecords, key=overheadCol)

        # Retrieves the highest overhead category name
        highest_category = highest_overhead[0]   

        # Retrieves the highest overhead value
        highest_percentage = highest_overhead[1]

        # Returns the formatted output of the highest overhead using the 'f' string
        return f"[HIGHEST OVERHEAD] {highest_category}: {highest_percentage}%\n"
    
def overheadCol(overheadRow):
    """
    - Function to obtain the second item in each row of the CSV file
    - "overheadRow" is a parameter that takes in each row in the "Overheads.csv" file
    """

    # Retrieves the second item of each row in the "Overheads.csv" file (Overhead value)
    return overheadRow[1]