# Program som kontrollerar om användaren är myndig

# Frågar användaren efter ålder
ålder = int(input("Hur gammal är du? "))

# Kontrollerar om användaren är under 18 år
if ålder < 18:
    print("Du är inte myndig.")
else:
    print("Du är myndig.")