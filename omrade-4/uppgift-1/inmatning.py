# Program som kontrollerar om användaren skriver ett giltigt heltal

try:
    # Försöker omvandla användarens inmatning till ett heltal
    heltal = int(input("Skriv ett heltal: "))
    print(f"Du skrev: {heltal}")

except ValueError:
    # Hanterar ValueError om användaren inte skriver ett giltigt heltal
    print("Fel: Du måste skriva ett heltal, till exempel 25.")

# Testning:
# Test 1: Inmatning 25 gav resultatet "Du skrev: 25".
# Test 2: Inmatning "hej" fångades av ValueError och gav ett tydligt felmeddelande.