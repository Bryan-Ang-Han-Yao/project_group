import overheads, cash_on_hand, profit_loss
from pathlib import Path

# Declaring variables to store the modularized functions
overheads_value = overheads.overheads_identifier()
cash_on_hand_value = cash_on_hand.COH_identifier()
net_profit_value = profit_loss.Profit_and_Loss_identifier()

# Declaring a variable to represent the full path to the "summary_report.txt" file in the current working directory
wp = Path.cwd()/"summary_report.txt"