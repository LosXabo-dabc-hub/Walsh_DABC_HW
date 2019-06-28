# -*- coding: utf-8 -*-
import os
import csv

# Initializing variables
total_votes_cast = 0
TRUE = 1
# Setting path to election_data.csv
election_data_csv_path = os.path.join("..", "Resources", "election_data.csv")

# Opening election_data.csv
# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(election_data_csv_path, newline="", encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_reader)
#    print(f"Header: {csv_header}")

    # Declaring lists
    all_row_values = []
    sorted_all_row_values = []
    voter_ids = []
    counties = []
    candidates = []

    # Counting the total number of votes
    for row in csv_reader:
        # Counting total votes cast
        total_votes_cast = total_votes_cast + 1
        voter_id = row[0]
        county = row[1]
        candidate = row[2]
        row_values = [voter_id, county, candidate]
        all_row_values.append(row_values)

#        sorted_all_row_values = all_row_values

        # The following code creates lists for each column item
        candidates.append(candidate)
        counties.append(county)
        voter_ids.append(voter_id)

    # the function set() finds unique values in a list

    c_name = []
    c_percent = []
    c_votes = []
    c_results = []
    
    candidate_list = set(candidates)
    for x_candidate in candidate_list:
        candidate_percent = round((((candidates.count(x_candidate))/total_votes_cast)*100),3)
        candidate_votes = candidates.count(x_candidate)
#        print((x_candidate) + " " + str("%.3f" % candidate_percent) + " " + str(candidates.count(x_candidate)))
        c_name = x_candidate
        c_percent = float(candidate_percent)
        c_votes = int(candidate_votes)
        c_values = [c_name, c_percent, c_votes]
        c_results.append(c_values)

#        print(c_name)
#        print(str(c_percent))
#        print(str(c_votes))
#       print(x_candidate)
#       print(candidates.count(x_candidate))


#print(c_results[0][0])
#print(str(total_votes_cast))

def sortSecond(val):
    return val[1]

c_results.sort(key = sortSecond, reverse = True)
#print(c_results)


# can access multidimensional list using 
# square brackets 
  
          

print(f" ")
print(f"Election Results")
print(f"_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print(f" ")
print("Total Votes: " + str(total_votes_cast))
print(f"_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print(f" ")

for i in range(len(c_results)) :  
#    for j in range(len(c_results[i])) :  
#        print(c_results[i][j], end=" ") 
    print(c_results[i][0] + ": " + str("%.3f" % c_results[i][1]) + "% (" + str(c_results[i][2]) + ")")     
print(f"_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print(f" ")


# Creating and opening a txt file named Analysis_Results.txt
file2 = open("Election_Results.txt","w") 

# Write analysis output to file 
# \n is placed to indicate EOL (End of Line) 
file2.write(f"Election Results \n")
file2.write(f"_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n \n")
file2.write("Total Votes: " + str(total_votes_cast) + "\n")
file2.write(f"_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n \n")

for i in range(len(c_results)) :  
#    for j in range(len(c_results[i])) :  
#        print(c_results[i][j], end=" ") 
    file2.write(c_results[i][0] + ": " + str("%.3f" % c_results[i][1]) + "% (" + str(c_results[i][2]) + ")" + "\n")     
file2.write(f"_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n \n")
file2.write(f" ")

# Closing Analysis_Results.txt 
file2.close() #to change file access modes 
  


#for i in range(len(c_results)) :  
#    for j in range(len(c_results[i])) :  
#        print(c_results[i][j], end=" ") 
#    print() 

    




    