from funksjoner import *

vanskelig = False

while not vanskelig:
    try:
        gradVanskelig = int(input("Velg vanskelighetsgrad: "))
        if 0 <= gradVanskelig <= 10:
            vanskelig = True
        else:
            print("Vanskelighetsgrad må være mellom 1 og 10")
    except ValueError:
        print("Vanskelighetsgrad må være et tall")

losningsord = hent_ord(vanskelighetsgrad=gradVanskelig)
korrekt = []
feil = []
godkjentInput = False
gjettet = False
forsøk = 0

losning = reveal_correct_letters(losningsord, korrekt)
print(losning)

while not gjettet:
    while not godkjentInput:
        brukerInput = input("Gjett en bokstav: ")
        if is_letter(brukerInput):
            godkjentInput = True
        else:
            print("Du kan bare skrive inn en bokstav. Prøv igjen!")

    if korrekt.__contains__(brukerInput) or feil.__contains__(brukerInput):
        print("Du har gjettet denne bokstaven før")
        print(korrekt)
        print(feil)
    elif (losningsord.__contains__(brukerInput)):
        print("ordet inneholder gjettet bokstav!")
        korrekt.append(brukerInput)
    else:
        print("ordet inneholder ikke gjettet bokstav!")
        feil.append(brukerInput)
        forsøk += 1
    losning = reveal_correct_letters(losningsord, korrekt)
    print(losning)
    figure = create_figure(forsøk)
    print_figure(figure)

    if sjekk_om_vunnet(losning):
        gjettet = True
    elif sjekk_om_tapt(forsøk):
        print("løsningsordet var: " + losningsord)
        gjettet = True
    else:
        godkjentInput = False
