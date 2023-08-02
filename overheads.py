# Assigned to Natalee

from pathlib import Path
import csv

file_path = Path.cwd()/"csv_reports"/"Overheads.csv"

def overheads_identifier():
    with file_path.open(mode="r", encoding="UTF-8", newline="") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        overheadsRecords = [] 
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