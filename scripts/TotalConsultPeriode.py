#!/usr/bin/python3
import psycopg2
import csv
import sys
import psycopg2

param1 = sys.argv[1]
param2 = sys.argv[2]

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="root"
)

cur = conn.cursor()


#requetes
sql_query = 'SELECT COUNT("Num_consultation"),"Date" FROM "Consultation" WHERE "Date" BETWEEN \'%' + param1 + '%\' AND \'%' + param2 + '%\' GROUP BY "Date" ORDER BY "Date";'

#execution requete
try :
    cur.execute(sql_query)
    print("requete TotalConsultPeriode effectuée ! ✔️ ")
except psycopg2.OperationalError as e:
    print("Erreur lors de la requette : {e} ❌")

#affichage resultat requete
rows = cur.fetchall()

#ecriture csv
with open('Resultats_TotalConsultPeriode.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['Nombre_de_consultations', 'Date'])
    for row in rows:
        writer.writerow(row)

#fermeture
cur.close()
conn.close()

