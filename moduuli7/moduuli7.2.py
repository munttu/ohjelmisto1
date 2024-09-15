'''Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää
 tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty
 nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet
yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
Käytä joukkotietorakennetta nimien tallentamiseen.'''
nimet=set()
def nimet(nimi,nimijoukko):
    nimijoukko.add(nimi)
    return nimi


nimijoukko= {""}
nimi=input("anna nimi: ")

while nimi!="":
    if not nimi in nimijoukko:
        print("uusi")
        nimet(nimi,nimijoukko)
    else:
        print("sama nimi")
    nimi=input("anna nimi: ")
for nimi in nimijoukko:
    print(nimi)









