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
            overhead_category = row[0].strip()
            overhead_percentage = float(row[1])
            overheadsRecords.append([overhead_category, overhead_percentage])
        highest_overhead = max(overheadsRecords, key=overheadCol)
        highest_category = highest_overhead[0]   
        highest_percentage = highest_overhead[1]
        return f"[HIGHEST OVERHEAD] {highest_category}: {highest_percentage}%\n"
    
def overheadCol(overheadRow):
    return overheadRow[1]