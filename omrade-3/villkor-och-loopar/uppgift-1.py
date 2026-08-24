# 1. Fråga användaren efter lösenord
# 2. Kontrollera om lösenordet är rätt
# 3. Om lösenordet är fel, fråga igen
# 4. När lösenordet är rätt, skriv "Välkommen in!"

lösenord = input("Ange lösenord: ")

while True:
    if lösenord == "kod123":
        print("Välkommen in!")
        break
    else:
        print("Fel lösenord, försök igen.")
        lösenord = input("Ange lösenord: ")   

