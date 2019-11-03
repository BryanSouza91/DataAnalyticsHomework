import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join("Resources", "budget_data.csv")

# Read the CSV file
with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    # Define variables
    total_months = 0
    net_total = 0
    avg_chg = 0
    chg = []
    month = []
    PL = []
    increase = 0
    decrease = 0
    inc_mon = ""
    dec_mon = ""

    for row in csvreader:
        month.append(row[0])
        PL.append(float(row[1]))
        # Count of months in data
        total_months += 1
        # Find net total over time
        net_total += float(row[1])
       
    for i in range(1,len(month)):
        chg.append(PL[i]-PL[i-1])
        avg_chg = round(sum(chg)/len(chg),2)
        increase = max(chg)
        inc_mon = str(month[chg.index(increase)])
        decrease = min(chg)
        dec_mon = str(month[chg.index(decrease)])
                
# Print report to terminal and .txt
print("Financial Analysis")
print("-----"*12)
print(f"Total Months:                           {total_months}")
print(f"Total:                                  ${net_total}")
print(f"Average Change:                         ${avg_chg}")
print(f"Greatest Increase in Profits:           {inc_mon} ${increase}")
print(f"Greatest Decrease in Profits:           {dec_mon} ${decrease}")

with open("pybank.txt", "w") as text_file:
    print("Financial Analysis", file=text_file)
    print("-----"*12, file=text_file)
    print(f"Total Months:                           {total_months}", file=text_file)
    print(f"Total:                                  ${net_total}", file=text_file)
    print(f"Average Change:                         ${avg_chg}", file=text_file)
    print(f"Greatest Increase in Profits:           {inc_mon} ${increase}", file=text_file)
    print(f"Greatest Decrease in Profits:           {dec_mon} ${decrease}", file=text_file)