# Enkel kalkylator med meny

while True:
    print("\n--- Kalkylator ---")
    print("1. Addera")
    print("2. Subtrahera")
    print("3. Multiplicera")
    print("4. Avsluta")

    val = input("Välj ett alternativ: ")

    # Adderar två tal
    if val == "1":
        tal1 = float(input("Skriv det första talet: "))
        tal2 = float(input("Skriv det andra talet: "))

        resultat = tal1 + tal2

        print("Resultat:", resultat)

    # Subtraherar två tal
    elif val == "2":
        tal1 = float(input("Skriv det första talet: "))
        tal2 = float(input("Skriv det andra talet: "))

        resultat = tal1 - tal2

        print("Resultat:", resultat)

    # Multiplicerar två tal
    elif val == "3":
        tal1 = float(input("Skriv det första talet: "))
        tal2 = float(input("Skriv det andra talet: "))

        resultat = tal1 * tal2

        print("Resultat:", resultat)

    # Avslutar programmet
    elif val == "4":
        print("Programmet avslutas.")
        break

    # Hanterar ogiltigt menyval
    else:
        print("Ogiltigt val. Välj 1, 2, 3 eller 4.")

# Testning:
# Test 1: Alternativ 1 adderade två tal och visade rätt resultat.
# Test 2: Alternativ 2 subtraherade två tal och visade rätt resultat.
# Test 3: Alternativ 3 multiplicerade två tal och visade rätt resultat.
# Test 4: Alternativ 4 avslutade programmet korrekt.
# Test 5: Ett ogiltigt menyval gav ett tydligt felmeddelande.
# Testerna visar att kalkylatorns meny, beräkningar och kontrollflöde fungerar som planerat.