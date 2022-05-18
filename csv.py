#import csv
#with open('biostats.csv', mode='r') as file:
#   csv_read = csv.reader(file, delimiter="-")
#   for lines in csv_read:
#        print(lines)

# write a csv
import csv

fieldnames = ['Name', 'Sex', 'Age', 'Height', 'Weight']
rows =[
    ['John','Male', 27, 5.6,120],
    ['Mary', 'Female', 25, 5.2, 110]
]
with open('new_file.csv', 'w') as file:
    csv_write = csv.writer(file)
    csv_write.writerow(fieldnames)
    csv_write.writerows(rows)

