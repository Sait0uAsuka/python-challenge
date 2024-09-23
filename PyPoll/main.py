# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os


# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
# candidate_names = []  # make a list of candidate name, but now its empty
dictionary = {} # make a dictionary, in the future, it can combine the name and the vote count and %
# Winning Candidate and Winning Count Tracker
win = ''
winvote= 0   # Track the win vote

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader) #skip the head, read from row 2

    # Loop through each row of the dataset and process it
    for row in reader:
        
        # Print a loading indicator (for large datasets)
        # print(". ", end="")  

        # Increment the total vote count for each row
        total_votes += 1 #keep adding the votes
        # Get the candidate's name from the row
        candidate = str(row[2]) #identify the column 3 from row 2 is the name of candidate

        # If the candidate is not already in the candidate list, add them
        if candidate not in dictionary:  # in dictionary, its blank, if candidate is NOT in the dictionary, add it
            dictionary[candidate] = 1    # and add 1 for vote
        # Add a vote to the candidate's count
        else:                           # if candidate is INSIDE the dictionary
            dictionary[candidate] += 1  # candidate will plus 1 vote

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    # Write the total vote count to the text file
    output = (
        f"Election Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"------------------------\n"
    )


    # Loop through the candidates to determine vote percentages and identify the winner

    for candidate_name in dictionary: #iterating over the keys of dictionary 
                                      #now inside the dictionary is [candidate_name:  xxxxx(value)]
                                                                        #             dictionary[candiate_name]
        # Get the vote count and calculate the percentage
        vote = dictionary[candidate_name]  # values = dictionary[keys] 
        percentage = (vote / total_votes)*100  #formula of percentage
        

        # Update the winning candidate if this one has more votes
        if vote >= winvote:  #if vote count is bigger thatn winvote which is zero now
            win = candidate_name                   # win is = to candidate_name
            winvote = vote
        
        # Print and save each candidate's vote count and percentage
        output += f"{candidate_name}: ${percentage:.3f}% ({vote}) \n" 
        #            Diana DeGette:     73.812%           (272892)

    # Generate and print the winning candidate summary
    output += (
    f"------------------------\n"
    f"Winner: {win}"
    )


print(output)
    # Save the winning candidate summary to the text file
with open(file_to_output, "w") as txt_file:
     txt_file.write(output)
