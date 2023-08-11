# This action requires the 'csv' module
import csv

# The basic usage is to first define the rows of the csv file:
#creates a csv
row_list = [["Title", "Current Price", "Actual Price", "Description","How To","Images"],
             ]
with open('test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)



# adding on the csv
f = open('test.csv', 'a')

# create the csv writer
writer = csv.writer(f)
row = ["noodles","24","43","this is description","images links"]
# write a row to the csv file
writer.writerow(row)

# close the file
f.close()