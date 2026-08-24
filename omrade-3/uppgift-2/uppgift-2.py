# Frågar användaren efter det första talet och omvandlar svaret till ett heltal
tal1 = int(input("Skriv in ett tal: "))

# Frågar användaren efter det andra talet och omvandlar svaret till ett heltal
# Möjligt exekveringsfel: ValueError om användaren skriver text istället för ett heltal
tal2 = int(input("Skriv in ett annat tal: "))

# Adderar de två talen och sparar resultatet i variabeln summa
summa = tal1 + tal2

# Skriver ut talen och resultatet för användaren
print(f"Summan av {tal1} och {tal2} är {summa}.")