# 1. Skapa en lista med tal
# 2. Gå igenom varje tal i listan
# 3. Kontrollera om talet är delbart med 2
# 4. Om talet är delbart med 2, skriv ut "Jämnt"
# 5. Annars, skriv ut "Udda"
# 6. Upprepa tills alla tal i listan har kontrollerats

lista = [3, 6, 7, 12]
for tal in lista:
    if tal % 2 == 0:
        print("Jämnt")
    else:
        print("Udda")