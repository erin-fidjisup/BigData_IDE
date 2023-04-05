#!/usr/bin/python3
import psycopg2
import csv
import sys
import psycopg2

diag1 = sys.argv[1]

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="root"
)


cur = conn.cursor()

    #requetes
sql_query ='SELECT COUNT("Diagnostic") AS "Total",LOWER("Diagnostic") AS "Diagnostic", TO_CHAR("Date", \'mm-yyyy\') AS "Date" FROM "Diagnostic" INNER JOIN "Consultation" ON "Diagnostic"."Code_diag" = "Consultation"."Code_diag" WHERE "Diagnostic" LIKE \'%'+ diag1 +'%\' GROUP BY "Diagnostic","Date" ORDER BY MAX("Date");'

#execution requete
try :
    cur.execute(sql_query)
    print("requete TotalConsultDiagPeriode effectuée ! ✔️")
except psycopg2.OperationalError as e:
    print("Erreur lors de la requette : {e} ❌")


    #affichage resultat requete
rows = cur.fetchall()


    #ecriture csv
with open('Resultats_TotalConsultDiagPeriode.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['Total','Diagnostic', 'Date'])
    for row in rows:
        writer.writerow(row)

    #fermeture
cur.close()
conn.close()

