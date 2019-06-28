# -*- coding: utf-8 -*-
import os
import csv

# Initializing variables
tot_mo = 0
total = 0
x=0

# Setting path to budget_data.csv
budget_data_csv_path = os.path.join("..", "Resources", "budget_data.csv")

# Opening csv data
# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(budget_data_csv_path, newline="", encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_reader)
#    print(f"Header: {csv_header}")

    # Creating lists
    mylist = []
    mydate = []
    diff = []
    all_row_values = []
    
    # Read through each row of data after the header
    for row in csv_reader:
        date = row[0]
        value = row[1]
        row_values = [date, value]
        all_row_values.append(row_values)
        
#        print(row[0] + " " + row[1])
        tot_mo = tot_mo +1
        total += int(row[1])
        mylist.append(row[1])
        mydate.append(row[0])

#        print("value appended to mylist " + row[1])
#        print(f" ")
#        print(str(tot_mo))

    all_row_values[0]    
# This prints the first value in the second group 
#    print(all_row_values[2][1])  

    x=0
    diff_total = 0
    while x < (tot_mo-1):
        change = (int(mylist[x+1]))-(int(mylist[x]))
#        print(str(change))
#        print(str(x))
        diff.append(change)
        diff_total = int(diff[x]) + diff_total
        x=x+1

    avg_chg = 0.00
    avg_chg = diff_total/(tot_mo-1)

# Finding the greatest increase (max_diff) and decrease (min_diff)
#    print("max & min diff")
    max_diff = max(diff)
#    print(str(max_diff))
    min_diff = min(diff)
#    print(str(min_diff))

# Finding the rows for the min and max values
    v = 1
    row_v = 0
    while v < (tot_mo-1):
        # Finding the row for the max_diff value
        if max_diff == int(diff[v]):
            row_max = v+1
        # Finding the row for the min_diff value
        if min_diff == int(diff[v]):
            row_min = v+1
        # Incrementing counter
        v = v + 1

# Creating and opening a txt file named Analysis_Results.txt
file1 = open("Analysis_Results.txt","w") 

# Write analysis output to file 
# \n is placed to indicate EOL (End of Line) 
file1.write("Financial Analysis \n") 
file1.write("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n \n") 

file1.write("Total Months: " + str(tot_mo) + "\n") 
file1.write("Total: " + "$" + str(total) + "\n") 
file1.write("Average Change: " + str("%.2f" % avg_chg) + "\n") 
file1.write("Greatest Increase in Profits: " + (all_row_values[row_max][0]) + " " + "($" + str(max_diff) + ")" + "\n") 
file1.write("Greatest Decrease in Profits: " + (all_row_values[row_min][0]) + " " + "($" + str(min_diff) + ")" + "\n") 

# Closing Analysis_Results.txt 
file1.close() #to change file access modes 
  
  
# print("row_v is " + str(row_min))
    
# print(diff[0])
# print(diff[84])
# print(mydate[84])
# print(str(diff_total))

# Write analysis output to terminal
print(f" ")
print(f"Financial Analysis")
print(f"_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print(f" ")

print("Total Months: " + str(tot_mo) )
print("Total: " + "$" + str(total) )
print("Average Change: " + str("%.2f" % avg_chg) )
print("Greatest Increase in Profits: " + (all_row_values[row_max][0]) + " " + "($" + str(max_diff) + ")")
print("Greatest Decrease in Profits: " + (all_row_values[row_min][0]) + " " + "($" + str(min_diff) + ")")

#delete following when debugged
# print(f" ")
# print(mylist[85])


