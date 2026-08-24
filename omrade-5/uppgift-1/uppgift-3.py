# Set som lagrar unika användarnamn
anvandarnamn = set()
# Användaren får skriva in flera användarnamn
while True:
    namn = input("Skriv ett användarnamn eller 'klar' för att avsluta: ")

    if namn.lower() == "klar":
        break

    anvandarnamn.add(namn)

    print("Användarnamnet har lagts till.")
# Visar alla unika användarnamn
print("\nUnika användarnamn:")
print(anvandarnamn)

# Testning:
# Test 1: Ett användarnamn lades till i setet korrekt.
# Test 2: Flera olika användarnamn lades till korrekt.
# Test 3: Ett användarnamn som skrevs in flera gånger men sparades bara en gång.
# Test 4: "klar" avslutade inmatningen korrekt.
# Test 5: Programmet visade endast unika användarnamn i slutet.
# Testerna visar att programmet använder ett set för att hantera unika användarnamn.