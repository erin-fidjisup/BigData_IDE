import os
import csv
import sys
import psycopg2

good_filename = r"C:\Users\Théotime\Desktop\professionnel_sante_GOOD.csv"
print(sys.argv[0])
print(sys.argv[1])

file = sys.argv[1]

if os.path.isfile(good_filename):
    os.remove(good_filename)

with open(file, "r", encoding='ISO-8859-1') as csvfile, \
    open(good_filename, "w", newline='', encoding='ISO-8859-1') as goodfile:

    reader = csv.reader(csvfile)
    writer = csv.writer(goodfile, delimiter=';')

    for row in reader:

        row = [cell.replace(';', '').replace(',', ';') for cell in row]

        writer.writerow(row)