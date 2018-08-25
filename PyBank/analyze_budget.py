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

currentvalue = 0
previousvalue =  0
maxvalue = 0 
rownum = 0
maxvaluemonth = ""

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        currentvalue = int(row[1])
        if (rownum ==0):
            previousvalue = currentvalue
        else:
            diff = currentvalue - previousvalue
            previousvalue = currentvalue

            if (diff > 0):
                if (maxvalue == 0) :
                    maxvalue = diff 
                    maxvaluemonth = (row[0])
                else:
                    if (diff > maxvalue):
                        maxvalue = diff
                        maxvaluemonth = (row[0])

        rownum += 1
print("Greatest Increase: " + (maxvaluemonth) + " ($" + str(maxvalue) + ")")
        
currentvalue = 0
previousvalue =  0
minvalue = 0 
rownum = 0
minvaluemonth = ""

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        currentvalue = int(row[1])
        if (rownum ==0):
            previousvalue = currentvalue
        else:
            diff = currentvalue - previousvalue
            previousvalue = currentvalue

            if (diff < 0):
                if (minvalue == 0) :
                    minvalue = diff 
                    minvaluemonth = (row[0])
                else:
                    if (diff < minvalue):
                        minvalue = diff
                        minvaluemonth = (row[0])

        rownum += 1
print("Greatest Decrease: " + (minvaluemonth) + " ($" + str(minvalue) + ")")    

print("Financial Analysis: ")
print("---------------------")
print ("Total Months: " + str(counter))
print("Total: " + str(totalnetvalue))
print("Average Change: " + str(plchange/(rownum - 1)))
print("Greatest Increase: " + (maxvaluemonth) + " ($" + str(maxvalue) + ")")
print("Greatest Decrease: " + (minvaluemonth) + " ($" + str(minvalue) + ")")

