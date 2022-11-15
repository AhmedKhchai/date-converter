import csv
from datetime import datetime
source = 'khoubza.csv'
target = 'tajine.csv'

with open(source, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    datawriter = csv.writer(open(target, 'w'))
    for row in datareader:
        print('before convertion', row[0])
        time = datetime.strptime(row[0], "%m/%d/%Y")
        print('after convertion', time)
        datawriter.writerow([time])
