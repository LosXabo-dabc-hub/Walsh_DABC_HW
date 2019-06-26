# -*- coding: utf-8 -*-
import os
import csv

#import pandas
#df = pandas.read_csv('hrdata.csv')
#print(df)


#tot_mo = 0
total = 0
x=0
budget_data_csv_path = os.path.join("..", "Resources", "budget_data.csv")

# Lists to store data
#Monthly_change = []
Profit_Losses = []

# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(budget_data_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")

    mylist = []
    mydate = []
    diff = []
    # Read through each row of data after the header
    all_row_values = []
    for row in csv_reader:
        date = row[0]
        value = row[1]
        row_values = [date, value]
        all_row_values.append(row_values)
    
    all_row_values[0]    
    print(all_row_values[2][0])    
        
    #print(row[0] + " " + row[1])
    #tot_mo = tot_mo +1
    #total += int(row[1])
    #mylist.append(row[1])
    #mydate.append(row[0])
    #print("value appended to mylist " + row[1])
    #print(f" ")

    print(str(tot_mo))

    x=0
    diff_total = 0
    while x < (tot_mo-1):
        change = (int(mylist[x+1]))-(int(mylist[x]))
        print(str(change))
        print(str(x))
        diff.append(change)
        diff_total = int(diff[x]) + diff_total
        x=x+1

    avg_chg = 0.00
    avg_chg = diff_total/(tot_mo-1)


    print("max & min diff")
    #max_diff = max(diff)
    print(str(max_diff))
    #min_diff = min(diff)
    print(str(min_diff))

   
print(diff[0])
print(diff[84])
print(mydate[84])
#print(str(diff_total))

print(f" ")
print(f"Financial Analysis")
print(f"_______________________________")
print(f" ")

print("Total Months: " + str(tot_mo) )
print("Total: " + str(total) )
print("Average Change: " + str("%.2f" % avg_chg) )
print("Greatest Increase in Profits: " + "$" + str(max_diff))
print("Greatest Decrease in Profits: " + "$" + str(min_diff))

#delete following when debugged
print(f" ")
print(mylist[85])





#
#file1 = open(file.csv, 'rb')
#reader = csv.reader(file1)
#new_rows_list = []
#for row in reader:
#   if row[2] == 'Test':
#      new_row = [row[0], row[1], 'Somevalue']
#      new_rows_list.append(new_row)
#file1.close()   # <---IMPORTANT
#
## Do the writing
#file2 = open(file.csv, 'wb')
#writer = csv.writer(file2)
#writer.writerows(new_rows_list)
#file2.close()
#


#*******
#********
#
#import os
#import csv
#
## use self-explanatory names for variables
#cereal_csv_path = os.path.join("..", "Resources", "cereal.csv")
#
## Open and read csv
#with open(cereal_csv_path, newline="") as csvfile:
#    csv_reader = csv.reader(csvfile, delimiter=",")
#
#    # Read the header row first (skip this part if there is no header)
#    csv_header = next(csv_reader)
#    print(f"Header: {csv_header}")
#
#    # Read through each row of data after the header
#    for row in csv_reader:
#
#        # Convert row to float and compare to grams of fiber
#        if float(row[7]) >= 5:
#            print(row[0]+" has "+row[7])
#
#
#cereal_csv_path = os.path.join("..", "Resources", "cereal_out.csv")
#
#
#        # Add title
#        Date.append(row[1])
#
#        # Add price
#        Profit_Losses.append(row[2])
#
#
#my_info = {
#	"name": "Marie",
#	"occupation": "Developer",
#	"age": 39,
#	"hobbies": ["Track & field", "Basketball", "Listening to music"],
#	"wake-up": {
#		"Monday": "6:00",
#		"Tuesday": "6:00",
#		"Thursday": "6:00",
#		"Saturday": "6:00"}
#}
#
#print(f'My name is {my_info["name"]}')
#print(f'I have {len(my_info["hobbies"])} hobbies')
#print(f'On Mondays, I get up at {my_info["wake-up"]["Monday"]}')
#
#
#import os
#import csv
#
## Prompt user for video lookup
#video = input("What show or movie are you looking for? ")
#
## Set path for file
#csvpath = os.path.join("..", "Resources", "netflix_ratings.csv")
#
## Bonus
## ------------------------------------------
## Set variable to check if we found the video
#found = False
#
## Open the CSV
#with open(csvpath, newline="") as csvfile:
#    csvreader = csv.reader(csvfile, delimiter=",")
#
#    # Loop through looking for the video
#    for row in csvreader:
#        if row[0] == video:
#            print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])
#
#            # BONUS: Set variable to confirm we have found the video
#            found = True
#
#            # BONUS: Stop at first results to avoid duplicates
#            break
#
#    # If the video is never found, alert the user
#    if found is False:
#        print("Sorry about this, we don't seem to have what you are looking for!")
#
#
#
#
#import os
#import csv
#
#udemy_csv = os.path.join("..", "Resources", "web_starter.csv")
#
## Lists to store data
#title = []
#price = []
#subscribers = []
#reviews = []
#review_percent = []
#length = []
#
## with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
#with open(udemy_csv, newline="") as csvfile:
#    csvreader = csv.reader(csvfile, delimiter=",")
#    for row in csvreader:
#        # Add title
#        title.append(row[1])
#
#        # Add price
#        price.append(row[4])
#
#        # Add number of subscribers
#        subscribers.append(row[5])
#
#        # Add amount of reviews
#        reviews.append(row[6])
#
#        # Determine percent of review left to 2 decimal places
#        percent = round(int(row[6]) / int(row[5]), 2)
#        review_percent.append(percent)
#
#        # Get length of the course to just a number
#        new_length = row[9].split(" ")
#        length.append(float(new_length[0]))
#
## Zip lists together
#cleaned_csv = zip(title, price, subscribers, reviews, review_percent, length)
#
## Set variable for output file
#output_file = os.path.join("web_final.csv")
#
##  Open the output file
#with open(output_file, "w", newline="") as datafile:
#    writer = csv.writer(datafile)
#
#    # Write the header row
#    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
#                     "Percent of Reviews", "Length of Course"])
#
#    # Write in zipped rows
#    writer.writerows(cleaned_csv)