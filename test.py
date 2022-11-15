import csv
from datetime import datetime
source = 'khoubza.csv'  # khoubza.csv is the path of the source file with unformatted dates
target = 'tajine.csv'   # tajine.csv is the path of the file to be populated with formatted dates
with open(source, 'r') as csvfile: # open the source file
    datareader = csv.reader(csvfile) # read the source file
    datawriter = csv.writer(open(target, 'w')) # open the target file
    for row in datareader: # loop through the rows of the source file
        print('before convertion', row[0]) # print the date before convertion
        time = datetime.strptime(row[0], "%m/%d/%Y") # convert the date to a datetime object using the strptime method of the datetime module and the format of the date in the source file as the first argument of the method and the date as the second argument of the method
        print('after convertion', time) # print the date after convertion
        datawriter.writerow([time]) # write the converted date to the target file
