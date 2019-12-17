import os
import csv

bank_csv = os.path.join('..', '..', 'Homework_Resources', 'Week 3 - Python_Homework_PyBank_Resources_budget_data.csv')

with open(bank_csv, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	
	header = next(csvreader)
	number_months = 0    

	for row in csvreader:
		number_months +=1
	number_months
	print(f'Total of Months: {number_months}')

with open(bank_csv, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	
	header = next(csvreader)
	total_amount = 0

	for row in csvreader:
		total_amount += float(row[1])
	total_amount
	print(f'Total Amount: {total_amount}')

output_path = os.path.join("bank_results.txt")
	
with open(output_path, "w", newline="") as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(["Financial Analysis"])
	csvwriter.writerow(["--------------------------------"])
	csvwriter.writerow(["Total of Months: ", number_months])
	csvwriter.writerow(["Total Amount: ", total_amount])
	csvwriter.writerow(["Average Change: "])
	csvwriter.writerow(["Greatest Increse in Profits: "])
	csvwriter.writerow(["Greatest Decrease in Profits: "])


 
	
