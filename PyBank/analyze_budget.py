import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

print(csvpath)

counter = -1   

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        mydate = (row[0])
        counter = counter + 1
print ("Total Months: " + str(counter))
     
totalnetvalue = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        myp_l = (row[1])
        totalnetvalue = totalnetvalue + int(row[1])
print("Total: " + str(totalnetvalue))

previousvalue = 0 
plchange = 0
rownum = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader: 
        currentvalue = int(row[1])
        if (rownum ==0):
            previousvalue = currentvalue
        else:
            #print("my values :" + str(plchange) + " " + str(rownum) + " " + str(previousmonth))
            diff = currentvalue - previousvalue
            plchange = plchange + diff
            previousvalue = currentvalue
        rownum += 1
#print(plchange)
#Avergae Change = total change between months diveded by number of changes
print("Average Change: " + str(plchange/(rownum - 1)))
#print (str(rownum))


     

#The total number of months included in the dataset

#The total net amount of "Profit/Losses" over the entire period

#The average change in "Profit/Losses" between months over the entire period

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period