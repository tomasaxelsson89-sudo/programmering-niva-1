# Fungerande version efter felsökning

# Skapa en lista med tal
numbers = [10, 20, 30, 40, 50]

# Räkna ut summan av talen
total = 0

for num in numbers:
    total = total + num

# Beräkna medelvärdet
average = total / len(numbers)

# Skriv ut resultatet
print("Medelvärdet är:", average)

# Felsökning och åtgärder
#
# Fel 1 - Syntaxfel:
# Listans avslutande hakparentes ] saknades.
# Detta gjorde att Python inte kunde tolka listan korrekt.
# Åtgärd: Lade till ] efter det sista talet.
#
# Fel 2 - Syntaxfel:
# Kolon : saknades efter for-satsen.
# Detta gjorde att Python inte kunde tolka for-satsen korrekt.
# Åtgärd: Lade till kolon efter "for num in numbers".
#
# Fel 3 - Exekveringsfel (NameError):
# Variabeln "numberss" var felstavad och fanns därför inte.
# Detta gjorde att programmet kraschade när medelvärdet skulle beräknas.
# Åtgärd: Ändrade "numberss" till "numbers".
#
# Fel 4 – Exekveringsfel (TypeError):
# Programmet försökte kombinera en sträng med ett decimaltal
# med hjälp av operatorn +.
# Åtgärd: Använde komma i print() istället.

# Test av den färdiga koden
# Testdata: [10, 20, 30, 40, 50]
# Förväntat resultat: 30.0
# Faktiskt resultat: 30.0
# Testet visar att programmet beräknar medelvärdet korrekt.