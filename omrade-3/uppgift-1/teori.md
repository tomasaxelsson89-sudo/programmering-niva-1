# Område 3 – Uppgift 1: Variabler och datatyper

## Del 1 – Teoretiska frågor

### 1. Vad är en variabel och vad används den till i ett program?

En variabel är ett namn som används för att lagra ett värde i ett program. Värdet kan till exempel vara text eller ett tal. Genom att använda variabler kan programmet spara information och använda den senare i koden. Ett exempel är ålder = 37 där ålder är variabelns namn och 37 är värdet.

### 2. Vad är skillnaden mellan datatyperna `int`, `float` och `str` i Python?

`int` används för heltal till exempel `37` eller `-5`. `float` används för tal som innehåller decimaler, till exempel `19.95` eller `21.5`. `str` används för text till exempel `"Tomas"` eller `"Södertälje"`. Datatypen är viktig eftersom den påverkar hur Python behandlar värdet och vilka operationer som kan utföras på det. Till exempel kan två `int`-värden adderas matematiskt medan två `str`-värden kan sättas ihop som text.

### 3. Vad händer om man försöker addera en sträng med ett tal?

Om man försöker använda `+` mellan en `str` och ett `int` får man ett `TypeError` eftersom Python inte automatiskt kan addera text och ett tal. Till exempel fungerar inte `"Jag är " + 37`. För att det ska fungera kan talet först omvandlas till en sträng med `str(37)`, eller så kan man använda en f-string. Det visar varför det är viktigt att förstå vilken datatyp en variabel har.

### 4. Varför är det viktigt att använda beskrivande namn på variabler?

Det är viktigt att använda beskrivande namn eftersom det gör koden lättare att läsa, förstå och felsöka. Namnet bör tydligt visa vilken information variabeln innehåller. Till exempel är `ålder = 37` tydligare än `x = 37`, eftersom man direkt förstår vad värdet representerar. Beskrivande variabelnamn gör också koden enklare att underhålla och förstå för andra som läser eller arbetar med programmet.

### 5. Vad är typomvandling och när behöver man använda det i Python?

Typomvandling innebär att man ändrar ett värde från en datatyp till en annan, till exempel från `str` till `int` eller från `str` till `float`. Det behövs bland annat när man använder `input()`, eftersom all information som användaren skriver in läses in som text. Om man vill kunna räkna med ett värde från `input()` måste man därför omvandla det till en numerisk datatyp exempelvis med `int()` eller `float()`. Man kan även använda `str()` för att omvandla ett tal till text när man behöver kombinera talet med annan text.