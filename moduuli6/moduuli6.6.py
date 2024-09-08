import math

def pizza_pint_per_hint(halk, hinta_cm):
    sade = halk / 2
    pinta = math.pi * (sade / 100)**2
    hinta = hinta_cm / pinta
    return hinta

def main():
    halk1 = float(input("Syötä ensimmäisen pitsan halkaisija cm: "))
    hinta_cm1 = float(input("Syötä ensimmäisen pitsan hinta (€): "))

    halk2 = float(input("Syötä toisen pitsan halkaisija cm: "))
    hinta_cm2 = float(input("Syötä toisen pitsan hinta (€): "))

    pizza_pint_per_hint1 = pizza_pint_per_hint(halk1, hinta_cm1)
    pizza_pint_per_hint2 = pizza_pint_per_hint(halk2, hinta_cm2)

    print(f"Ensimmäisen pitsan hinta per m²: {pizza_pint_per_hint1:.2f} €/m²")
    print(f"Toisen pitsan hinta per m²: {pizza_pint_per_hint2:.2f} €/m²")

    if pizza_pint_per_hint1 < pizza_pint_per_hint2:
        print("Ensimmäinen pizza on arvokkaampi hintaan nähden.")
    elif pizza_pint_per_hint2 < pizza_pint_per_hint1:
        print("Toinen pizza on arvokkaampi hintaan nähden.")
    else:
        print("Molemmat pizzat tarjoavat saman arvon hintaan nähden.")

main()

