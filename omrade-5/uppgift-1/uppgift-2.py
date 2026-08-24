# Dictionary som lagrar kontakter
kontakter = {}

while True:
    print()
    print("--- Kontaktmeny ---")
    print("1. Lägg till kontakt")
    print("2. Sök efter kontakt")
    print("3. Ta bort kontakt")
    print("4. Avsluta")

    val = input("Välj ett alternativ: ")

    if val == "1":
        print("Du valde att lägga till en kontakt.")

        namn = input("Skriv kontaktens namn: ")
        telefonnummer = input("Skriv kontaktens telefonnummer: ")

        kontakter[namn] = telefonnummer

        print("Kontakten har lagts till.")

    elif val == "2":
        namn = input("Skriv namnet på kontakten du söker: ")

        if namn in kontakter:
            print("Telefonnummer:", kontakter[namn])
        else:
            print("Kontakten finns inte.")

    elif val == "3":
        namn = input("Skriv namnet på kontakten du vill ta bort: ")

        if namn in kontakter:
            del kontakter[namn]
            print("Kontakten har tagits bort.")
        else:
            print("Kontakten finns inte.")

    elif val == "4":
        print("Programmet avslutas.")
        break

    else:
        print("Ogiltigt val. Välj 1, 2, 3 eller 4.")

# Testning:
# Test 1: Alternativ 1 lade till en kontakt med namn och telefonnummer.
# Test 2: Alternativ 2 hittade en befintlig kontakt och visade telefonnumret.
# Test 3: Sökning efter en kontakt som inte fanns gav ett tydligt felmeddelande.
# Test 4: Alternativ 3 tog bort en befintlig kontakt korrekt.
# Test 5: Försök att ta bort en kontakt som inte fanns gav ett tydligt felmeddelande.
# Test 6: Alternativ 4 avslutade programmet korrekt.
# Testerna visar att programmets dictionary och menyfunktioner fungerar som planerat.