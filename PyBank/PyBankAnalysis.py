#import modules
import os
import csv

#set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

#set the output of the text file
text_path = "Final_Analysis.txt"
outfile = os.path.join('analysis', text_path)
#Set variables
totalmonths = []
profits = []
pc = []

# Method 2 using CVS Module
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile) #, delimiter=',')
   

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        totalmonths.append(row[0])
        profits.append(int(row[1]))

for i in range(len(profits) - 1):
        pc.append(profits[i+1] - profits[i])



total_months = len(totalmonths)
sum_profits = sum(profits)
avg_change = (sum(pc) / len(pc))
greatest_increase = ((totalmonths[pc.index(max(pc))+1]))
greatest_decrease = ((totalmonths[pc.index(min(pc))+1]))
g_increase = max(pc)
g_decrease = min(pc)


output =(
        f"Financial Analysis\n"
        f"---------------------\n"
        f'Total MOnths: {total_months}\n'
        
        f'Total Profits: {sum_profits}\n'
        f'Average Revenue Change : {avg_change}\n'
        f'Greatest Increase in Profits: {greatest_increase} {g_increase}\n'
        f'Greatest Decrease in Profits: {greatest_decrease} {g_decrease}\n'
)
print(output)




  
# write changes to csv
with open(outfile, 'w') as file:
        file.write(output)
       



