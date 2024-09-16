import mysql.connector
'''Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja 
tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava 
tieto siitä, että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.'''

def main(maakoodi):
    yhteys = mysql.connector.connect(
        host="localhost",
        user="root",
        password="6afroninja9",
        database="flight_game",
        autocommit=True,
        collation="utf8mb4_general_ci"
    )
    sql=f"SELECT type, COUNT(*) FROM airport WHERE iso_country=%s GROUP by type "
    kursori = yhteys.cursor()
    kursori.execute(sql, (maakoodi,))
    tulos= kursori.fetchall()
    if tulos:
        for rivi in tulos:
            print(f"Lentokenttien määrä tyypille {rivi[0]} on {rivi[1]} kappaletta")
    else:
        print(f"Ei löytynyt lentokenttiä maalle '{maakoodi}'")
    kursori.close()
    yhteys.close()

maakoodi=input("Makoodi: ")
main(maakoodi)