# -*- coding: utf-8 -*-
import os
import csv

tot_mo = 0
total = 0
x=0
election_data_csv_path = os.path.join("..", "Resources", "election_data.csv")

# Lists to store data
#Monthly_change = []
Profit_Losses = []

# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(election_data_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")

#    mylist = []
#    mydate = []
#    diff = []
    # Read through each row of data after the header
    for row in csv_reader:
        print(row[0] + " " + row[1] + " " + row[2])
#        tot_mo = tot_mo +1
#        total += int(row[1])
#        mylist.append(row[1])
#        mydate.append(row[0])
#        print("value appended to mylist " + row[1])
#        print(f" ")
#
#        print(str(tot_mo))
#
#    x=0
#    diff_total = 0
#    while x < (tot_mo-1):
#        change = (int(mylist[x+1]))-(int(mylist[x]))
#        print(str(change))
#        print(str(x))
#        diff.append(change)
#        diff_total = int(diff[x]) + diff_total
#        x=x+1
#
#    avg_chg = 0.00
#    avg_chg = diff_total/(tot_mo-1)
#
#
#    print("max & min diff")
#    max_diff = max(diff)
#    print(str(max_diff))
#    min_diff = min(diff)
#    print(str(min_diff))
#
#   
#print(diff[0])
#print(diff[84])
#print(mydate[84])
##print(str(diff_total))
#
#print(f" ")
#print(f"Financial Analysis")
#print(f"_______________________________")
#print(f" ")
#
#print("Total Months: " + str(tot_mo) )
#print("Total: " + str(total) )
#print("Average Change: " + str("%.2f" % avg_chg) )
#print("Greatest Increase in Profits: " + "$" + str(max_diff))
#print("Greatest Decrease in Profits: " + "$" + str(min_diff))
#
##delete following when debugged
#print(f" ")
#print(mylist[85])
