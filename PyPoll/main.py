import csv
import os

poll_csv = os.path.join("..", "..", "Homework_Resources", "Week 3 - Python_Homework_PyPoll_Resources_election_data.csv")

with open(poll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimeter=",")
    
    header = next(csvreader)
    
    