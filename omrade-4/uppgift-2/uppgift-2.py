# Program som simulerar ett biljettköp

# Frågar användaren vilken biljettkategori som ska köpas
kategori = input("Välj biljettkategori (barn, vuxen eller pensionär): ")

# Bestämmer priset beroende på biljettkategori
if kategori == "barn":
    pris = 20
elif kategori == "vuxen":
    pris = 50
elif kategori == "pensionär":
    pris = 30
else:
    pris = 0

# Skriver ut kvittot
if pris > 0:
    print("----- Kvitto -----")
    print("Biljett:", kategori)
    print("Pris:", pris, "kr")
    print("------------------")
else:
    print("Fel: Du måste välja barn, vuxen eller pensionär.")

# Testning:
# Test 1: "barn" gav priset 20 kr.
# Test 2: "vuxen" gav priset 50 kr.
# Test 3: "pensionär" gav priset 30 kr.
# Test 4: "student" gav ett tydligt felmeddelande.
# Testerna visar att programmet hanterar både giltiga och ogiltiga biljettkategorier.