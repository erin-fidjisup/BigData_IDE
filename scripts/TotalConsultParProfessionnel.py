#!/usr/bin/python3
import psycopg2
import csv
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="root"
)

cur = conn.cursor()

#requetes

sql_query ='SELECT COUNT("Num_consultation") AS "Total Consultations", CONCAT("Prenom",\' \', "Nom") AS "Professionnel" FROM "Consultation" INNER JOIN "Professionnel_de_sante" ON "Consultation"."Id_prof_sante" = "Professionnel_de_sante"."Identifiant" GROUP BY "Prenom", "Nom" ORDER BY "Nom";'

#execution requete
try :
    cur.execute(sql_query)
    print("requete TotalConsultParProfessionnel effectuée ! ✔️")
except psycopg2.OperationalError as e:
    print("Erreur lors de la requette : {e} ❌")


#affichage resultat requete
rows = cur.fetchall()
#ecriture csv
with open('Resultats_TotalConsultParProfessionnel.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['Nombre_de_consultations', 'Professionnel_de_Sante'])
    for row in rows:
        writer.writerow(row)

#fermeture
cur.close()
conn.close()
