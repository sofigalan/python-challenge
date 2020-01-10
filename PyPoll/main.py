import csv
import os

poll_csv = os.path.join("..", "Week 3 - Python_Homework_PyPoll_Resources_election_data.csv")

count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

with open(poll_csv, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	header = next(csvreader)
    
	for row in csvreader:
		count += 1
		candidatelist.append(row[2])
	print(f"Total Votes: {count}")

	for x in set(candidatelist):
		unique_candidate.append(x)
		y = candidatelist.count(x)
		vote_count.append(y)
		z = (y/count)*100
		vote_percent.append(z)

	winning_vote_count = max(vote_count)
	winner = unique_candidate[vote_count.index(winning_vote_count)]

for i in range(len(unique_candidate)):
            print(f"{unique_candidate[i]}: {vote_percent[i]}% ({vote_count[i]})")

print(f"The winner is: {winner}")

output_path = os.path.join("poll_results.txt")	
with open(output_path, "w") as text:
	text.write("Poll Results\n")
	text.write("--------------------------------\n")
	text.write(f"Total Votes: {count}\n")
	for i in range(len(unique_candidate)):
            text.write(f"{unique_candidate[i]}: {vote_percent[i]}% ({vote_count[i]})\n")
	text.write(f"The winner is: {winner}\n")