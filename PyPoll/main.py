# importing the needed modules 
import os
import csv

# creating an object out of csv file
election_dataCsv= os.path.join("..", "Resources", "election_data.csv")

# opening and reading the csv file
with open(election_dataCsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #reading the header row 
    header = next(csvreader)
    
    # a counter with start value of 0 for counting total number of votes cast by voters
    totalCount_votes = 0 

    # an empty list to capture names of candidates
    candidates = []
    # an empty list to capture total votes received by each candidate
    totalVotes_candidate =[]
    # an empty list to capture percentage of total votes for each candidate
    percentVotes_candidate =[]

    # going through row by row after header 
    for row in csvreader:
        # adding to counter will get total number of votes
        totalCount_votes += 1

        '''
        If candidates name is not in empty "candidates" list , then add name to list , make note of index 
         & add a vote in the empty "totalVotes_cadidate" list for the same index.
        If cadidate name is already in the list, then make note of the index  and add a vote in the 
        "totalVotes_cadidate" list at the same index.
        '''
        
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            totalVotes_candidate.append(1)  
        else:
            index = candidates.index(row[2])
            totalVotes_candidate[index] += 1

    # calculating percentage votes & adding to the "percentVotes_candidate " list
    for votes in totalVotes_candidate:
        percentage = (votes / totalCount_votes) * 100
        percentage = round(percentage)
        percentage = "% .3f%%"  % percentage
        percentVotes_candidate.append(percentage)

    # getting the winner candidate 
    # max votes belongs to winner
    winner = max(totalVotes_candidate) 
    # finds the index of the highest votes
    index = totalVotes_candidate.index(winner) 
    # uses above index to find name of winning candidate with highest votes
    winning_candidate = candidates[index] 
    
# displaying the results
print("Election Results") 
print("----------------------------")   
print(f"Total Votes : {(totalCount_votes)}")  
print("----------------------------")
for i in range (len(candidates)):
    print(f"{candidates[i]}: {(percentVotes_candidate[i])}  ({totalVotes_candidate[i]})")
print("----------------------------")
print(f"Winner : {winning_candidate}")
print("----------------------------")

# creating an output text file , writing into it and exporting it
output = open("output2.txt", "w")

line1 = "Election Results"
line2 = "----------------------------"
line3 = (f"Total Votes : {(totalCount_votes)}")
line4 = "----------------------------"
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range (len(candidates)):
    line = (f"{candidates[i]}: {(percentVotes_candidate[i])}  ({totalVotes_candidate[i]})")
    output.write('{}\n'.format(line))

line6 = ("----------------------------")
line7 = (f"Winner : {winning_candidate}")
line8 = ("----------------------------")

output.write('{}\n{}\n{}\n'.format(line6, line7, line8))
