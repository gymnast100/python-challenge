# importing the needed modules
import os
import csv

# creatig an object out of csv file
budgetdataCSV = os.path.join("..","Resources" ,"budget_data.csv")

# opening and reading the csv file
with open(budgetdataCSV, "r") as csvfile:

    # using a reader and split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #reading the header row
    header = next(csvreader)

    # a counter for total months starts at 0
    line_count = 0 
    # total of profit/loss column values starts at 0
    total = 0 
    # initial change in profit/loss starts at 0
    initialpl = 0
    # an empty list to capture change in profit/loss
    profit_Loss=[]
    #an empty list to capture date 
    date=[]
    
    # reading the first row 
    row = next(csvreader)
    total = total + int(row[1]) 
    line_count=line_count+1
    initialpl=int(row[1])

    # after header row and first row , going through data row by row 
    for row in csvreader:
        
        # tracking dates
        date.append(row[0])
        
        # counting the total number of months
        line_count=line_count+1

        # Toatl Value of profit/loss (adding current row of profit/loss value to the previous row value )
        total = total + int(row[1])
        
        # calculating change in profit/loss , storing in a list and resetting initial value
        change_profit_loss =int(row[1])- initialpl
        profit_Loss.append(change_profit_loss)
        initialpl=int(row[1])
        
        # greatest increase in profit , getting its index to get corresponding date 
        greatest_increase_profit = max(profit_Loss)
        profit_index = profit_Loss.index(greatest_increase_profit)
        greatest_date = date[profit_index]
        
        # greatest decrease in profit , getting its index to get corresponding date 
        greatest_decrease_profit = min(profit_Loss)
        loss_index = profit_Loss.index(greatest_decrease_profit)
        lowest_date = date[loss_index]

    # calculating average chaange in profit/loss  
    average = sum(profit_Loss)/len(profit_Loss)

    # displaying results
    print(f"Financial Analysis") 
    print(f"--------------------")
    print(f"Total Months:{line_count}")
    print(f"Total:${total}")
    print(f"Average Change: ${(round(average,2))}")
    print(f"Greatest Increase in Profits:{greatest_date} (${greatest_increase_profit})")
    print(f"Greatest Decrease in Profits:{lowest_date} (${greatest_decrease_profit})")
    
    # creating a text file , writing into it and exporting it
    output = open("output1.text", "w")

    line1 = (f"Financial Analysis") 
    line2 = (f"--------------------")
    line3 = (f"Total Months:{line_count}")
    line4 = (f"Total:${total}")
    line5 = (f"Average Change: ${(round(average,2))}")
    line6 = (f"Greatest Increase in Profits:{greatest_date} (${greatest_increase_profit})")
    line7 = (f"Greatest Decrease in Profits:{lowest_date} (${greatest_decrease_profit})")
    
    output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6, line7))