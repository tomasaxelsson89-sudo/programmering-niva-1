### 1. Vad är ett villkor (if-sats) och vad används det till i ett program?

Ett villkor används för att låta ett program fatta beslut beroende på om ett påstående är sant eller falskt. Med en `if`-sats kontrollerar programmet ett villkor och kör den kod som hör till om villkoret är sant. Med `else` kan man ange vad som ska hända om villkoret är falskt.

Villkor används för att styra programmets flöde och göra att programmet kan ta olika vägar beroende på informationen det får. Till exempel kan ett program kontrollera om en person är myndig. Om `ålder >= 18` är sant kan programmet skriva ut att personen är myndig, annars kan det skriva ut att personen inte är myndig.

På så sätt gör villkor program mer flexibla eftersom programmet inte alltid behöver göra exakt samma sak utan kan reagera olika beroende på vilka värden eller vilken information som används.

### 2. Hur fungerar en while-loop och när passar det att använda den?

En `while`-loop används för att upprepa en eller flera instruktioner så länge ett villkor är sant. Innan varje iteration kontrollerar programmet villkoret. Om villkoret är sant körs koden i loopen och sedan kontrolleras villkoret igen. När villkoret blir falskt avslutas loopen och programmet fortsätter med koden efter loopen.

En `while`-loop passar bra när man inte vet exakt hur många gånger koden behöver upprepas, utan när upprepningen istället ska fortsätta tills ett visst villkor uppfylls. Ett exempel är en lösenordskontroll där användaren får försöka skriva in lösenordet flera gånger tills rätt lösenord anges.

Ett annat exempel är ett program som låter användaren mata in tal tills en viss summa har uppnåtts. I sådana situationer är det villkoret som avgör när loopen ska fortsätta och när den ska avslutas.

### 3. Vad är skillnaden mellan en for-loop och en while-loop?

En `for`-loop används för att upprepa kod för varje element i exempelvis en lista, sträng eller ett bestämt antal gånger. En `for`-loop passar därför bra när man vill gå igenom en samling värden eller när man vet hur iterationen ska genomföras.

En `while`-loop upprepar istället kod så länge ett villkor är sant. Den passar därför bra när man inte vet exakt hur många gånger koden behöver upprepas, utan när repetitionen ska fortsätta tills ett visst villkor blir falskt.

En viktig skillnad är alltså att `for` vanligtvis används för att iterera över en bestämd samling eller ett bestämt antal gånger, medan `while` styrs av ett villkor. Båda används för repetition, men de passar olika typer av problem.

Exempelvis kan en `for`-loop användas för att skriva ut alla tal i en lista, medan en `while`-loop kan användas i ett program som fortsätter fråga efter ett lösenord tills användaren skriver rätt lösenord.

### 4. Vad händer om villkoret i en while-loop aldrig blir falskt?

Om villkoret i en `while`-loop aldrig blir falskt kommer loopen att fortsätta köra om och om igen. Detta kallas för en oändlig loop. Programmet fastnar då i loopen och kommer inte vidare till koden som står efter den.

En oändlig loop kan uppstå om programmeraren har skrivit ett villkor som alltid är sant eller om värdet som används i villkoret aldrig förändras på ett sätt som gör att villkoret kan bli falskt.

Exempelvis skulle följande kod skapa en oändlig loop:

while True:
    print("Loopen fortsätter")

Eftersom `True` alltid är sant finns det inget villkor som gör att loopen avslutas. En oändlig loop kan även uppstå av misstag, till exempel om programmet glömmer att uppdatera en variabel som används i loopens villkor.

För att undvika detta behöver man se till att villkoret någon gång kan bli falskt, eller använda exempelvis `break` för att avsluta loopen när en viss situation uppstår.

### 5. Ge ett exempel där en kombination av if och for används för att fatta beslut baserat på en lista.

En `for`-loop kan användas för att gå igenom varje element i en lista. Genom att kombinera `for` med en `if`-sats kan programmet kontrollera varje element och fatta ett beslut beroende på vilket värde elementet har.

Ett exempel är en lista med tal där programmet ska kontrollera om varje tal är jämnt eller udda. `for`-loopen går igenom talen ett i taget och `if`-satsen kontrollerar om talet är delbart med 2. Om resten vid division med 2 är 0 är talet jämnt, annars är det udda.

Exempel:

lista = [3, 6, 7, 12]

for tal in lista:
    if tal % 2 == 0:
        print("Jämnt")
    else:
        print("Udda")

Här används `for` för att iterera över listan och `if` för att fatta ett beslut för varje tal. Operatorn `%` beräknar resten vid en division. Därför kan `tal % 2 == 0` användas för att kontrollera om talet är jämnt.
