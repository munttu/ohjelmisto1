'''Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako tämä
syöttää uuden lentoaseman,
hakea jo syötetyn lentoaseman tiedot vai lopettaa.
 Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
  Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
  Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
  Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
  (ICAO-koodi on lentoaseman yksilöivä tunniste.
Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)'''
valintateksti = """\n 1) Lisää uusi lentoasema
 2) Anna tietoa lentoasemasta 
 3) Lopeta \n"""



def main():
    lentoasemat={}
    while True:
        print(valintateksti)
        valinta = int(input("valitse 1, 2 tai 3: "))
        if valinta==1:
            icao=input("anna lentoaseman icao koodi: ")
            uusiasema=input("anna lentoaseman nimi: ")
            lentoasemat[icao] = uusiasema
            print(f"lentoasema {uusiasema} (ICAO: {icao})")
        elif valinta==2:
            icao=input("anna lentokentän icao: ")
            if icao in lentoasemat:
                print(f"lentoasema {icao} : {lentoasemat [icao]}")
            else:
                print(f"lentoasemaa ICAO-koodilla {icao} ei löytynyt")
        if valinta==3:
            print("ohjelma lopetettu")
            break
        else:
            print("virheellinen valinta 1, 2 tai 3")






main()








