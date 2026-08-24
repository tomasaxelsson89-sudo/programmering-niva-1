from datetime import date

# Enkel meny med olika alternativ

while True:
    print("\n--- Huvudmeny ---")
    print("1. Hälsa användaren")
    print("2. Visa dagens datum")
    print("3. Avsluta")

    val = input("Välj ett alternativ: ")

    # Hälsar användaren
    if val == "1":
        print("Hej och välkommen!")

    # Visar dagens datum
    elif val == "2":
        print("Dagens datum är:", date.today())

    # Avslutar programmet
    elif val == "3":
        print("Programmet avslutas.")
        break

    # Hanterar ogiltigt menyval
    else:
        print("Ogiltigt val. Välj 1, 2 eller 3.")

# Testning:
# Test 1: Alternativ 1 hälsade användaren korrekt.
# Test 2: Alternativ 2 visade dagens datum korrekt.
# Test 3: Alternativ 3 avslutade programmet korrekt.
# Test 4: Ett ogiltigt menyval gav ett tydligt felmeddelande.
# Testerna visar att programmets meny, användarinteraktion och kontrollflöde fungerar som planerat.