# 1. Börja med summan 0
# 2. Fråga användaren efter ett tal
# 3. Lägg talet till summan
# 4. Visa den aktuella summan
# 5. Upprepa så länge summan är 100 eller mindre
# 6. När summan är över 100, skriv "Du har nått gränsen!"

summa = 0
while summa <= 100:
    tal = int(input("Ange ett tal: "))
    summa += tal
    print(f"Den aktuella summan är: {summa}")
print("Du har nått gränsen!")       