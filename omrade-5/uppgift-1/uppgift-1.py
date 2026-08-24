# Lista med frukter
frukter = ["äpple", "banan", "apelsin"]

# Meny som upprepas tills användaren väljer att avsluta
while True:
    print("\n--- Fruktmeny ---")
    print("1. Visa frukter")
    print("2. Lägg till en frukt")
    print("3. Ta bort en frukt")
    print("4. Avsluta")

    val = input("Välj ett alternativ: ")

    if val == "1":
        print("Frukter:", frukter)

    elif val == "2":
        ny_frukt = input("Vilken frukt vill du lägga till? ")
        frukter.append(ny_frukt)
        print("Frukten har lagts till.")

    elif val == "3":
        frukt_att_ta_bort = input("Vilken frukt vill du ta bort? ")
        
        if frukt_att_ta_bort in frukter:
            frukter.remove(frukt_att_ta_bort)
            print("Frukten har tagits bort.")
        else:
            print("Frukten finns inte i listan.")

    elif val == "4":
        print("Programmet avslutas.")
        break

    else:
        print("Ogiltigt val. Välj 1, 2, 3 eller 4.")

# Testning:
# Test 1: Alternativ 1 visade fruktlistan korrekt.
# Test 2: Alternativ 2 lade till en ny frukt i listan.
# Test 3: Alternativ 3 tog bort en befintlig frukt korrekt.
# Test 4: Försök att ta bort en frukt som inte fanns gav ett tydligt felmeddelande.
# Test 5: Alternativ 4 avslutade programmet korrekt.
# Testerna visar att programmets meny och listfunktioner fungerar som planerat.