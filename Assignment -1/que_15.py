import csv

samplefile=open('C:/Users/DELL/OneDrive/Desktop/Ritika ML/Assignment -1/file.csv','r')
a=csv.reader(samplefile)
for row in a:
        print(', '.join(row))