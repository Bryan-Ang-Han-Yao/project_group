import overheads, cash_on_hand, profit_loss
from pathlib import Path

# Declaring variables to store the modularized functions
overheads_value = overheads.overheads_identifier()
cash_on_hand_value = cash_on_hand.COH_identifier()
net_profit_value = profit_loss.Profit_and_Loss_identifier()

# Declaring a variable to represent the full path to the "summary_report.txt" file in the current working directory
wp = Path.cwd()/"summary_report.txt"

# Opening the file in write mode ("w") and specifying "UTF-8" as the character encoding for the file
with wp.open(mode = "w", encoding = "UTF-8") as file:

    # Write final output from the modularized functions to the "summary_report.txt" file
    file.write(overheads_value)
    file.write(cash_on_hand_value)
    file.write(net_profit_value)

    # Closing the file to to ensure that it is properly saved
    file.close()
    