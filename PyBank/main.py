import os
import csv

bank_csv = os.path.join('..','Week 3 - Python_Homework_PyBank_Resources_budget_data.csv')

months_number = 0
total_amount = 0
ProfitsLosses = []
months = []
monthly_change = []


with open(bank_csv, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	header = next(csvreader)  

	for row in csvreader:
		months_number +=1
		total_amount += float(row[1])
		ProfitsLosses.append(row[1])
		months.append(row[0])
	print(f'Total of Months: {months_number}')
	print(f'Total Amount: {total_amount}')
	print(f'Months: {months}')
	print(f'Profits and Losses: {ProfitsLosses}')

ProfitsLosses_previo = int(ProfitsLosses[0])

for i in range(1, len(ProfitsLosses)):
	monthly_change.append(int(ProfitsLosses[i]) - ProfitsLosses_previo)
	ProfitsLosses_previo = int(ProfitsLosses[i])
	i += 1

AverageChange = float(sum(monthly_change) / len(monthly_change))

print(f'Average Monthly Change: {AverageChange}')

MaxIncrease = max(monthly_change)
MaxDecrease = min(monthly_change)

for i in range(len(monthly_change)):
	if monthly_change[i] == MaxIncrease:
		maxMonth = (i -1)
	elif monthly_change[i] == MaxDecrease:
		minMonth = (i-1)
	else:
		i+=1

MaxIncrease_Month = months[maxMonth]
MaxDecrease_Month = months[minMonth]

print(f"Greatest Increase in Profits: {MaxIncrease_Month}: ${MaxIncrease}")
print(f"Greatest Decrease in Profits: {MaxDecrease_Month}: ${MaxDecrease}")

output_path = os.path.join("bank_results.txt")
	
with open(output_path, "w") as text:
	text.write("Financial Analysis\n")
	text.write("--------------------------------\n")
	text.write(f"Total of Months: {months_number}\n")
	text.write(f"Total Amount: {total_amount}\n")
	text.write(f"Average Change: ${AverageChange}\n")
	text.write(f"Greatest Increse in Profits: {MaxIncrease_Month} ${MaxIncrease}\n")
	text.write(f"Greatest Decrease in Profits: {MaxDecrease_Month} ${MaxDecrease}\n")