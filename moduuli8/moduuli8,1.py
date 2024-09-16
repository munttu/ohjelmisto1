import mysql.connector

'''Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. 
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla 
käytettävästä lentokenttätietokannasta. 
ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.'''

yhteys = mysql.connector.connect(
    host="localhost",
    user="root",
    password="6afroninja9",
    database="flight_game",
    autocommit=True,
    collation="utf8mb4_general_ci"
    )

def kyssari(icao):
    sql=f"SELECT airport.type, airport.municipality from airport where ident='{icao}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentokentän nimi on {rivi[0]} ja sijaintikunta on {rivi[1]}")
        return
icao=input("Kerro ICAO: ")
kyssari(icao)