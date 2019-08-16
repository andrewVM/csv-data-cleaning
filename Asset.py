import os
import sys
import csv

input_file = r"C:\Users\aN_v_M__\Desktop\python\RH_Assets_Threats_points_updated_July_2019.csv"

data = csv.reader()(open(input_file), delimiter = ',')

data = list(csv.reader()(open(input_file), delimiter = ','))


for row in data:
    newline = [item.strip() for item in row]
    newline = [item.title() for item in newline]
    newdata.append(newline)

newdata = []
for row in data:
    newline = [item.strip() for item in row]
    newline = [item.title() for item in newline]
    newline = [newline[].replace("Pentecoste", "Pentecostal")]



    infile_name = os.path.splitext(input_file)[0]
    infile_ext = os.path.splitext(input_file)[1]

    outfile = ("{}{}{}".format(infile_name, '_cleaned', infile_ext))

    writer = csv.writter(open(outfile, 'w'), deli)

#adding new items
#rstyjuhi
