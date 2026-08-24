# Område 5 – Datatyper och användarinteraktion

## Del 1 – Teoretiska frågor

### Fråga 1 – Vad är en lista i Python och vad används den till?

En lista i Python är en samling av flera värden som sparas i en variabel. Listor är ordnade och föränderliga, vilket betyder att man kan lägga till, ändra och ta bort värden efter att listan har skapats. Varje värde har en plats, ett så kallat index, där det första värdet har index 0. Listor passar därför bra när man behöver spara flera värden i en bestämd ordning, till exempel namn, poäng eller inköpsvaror.

### Fråga 2 – Förklara skillnaden mellan en list och en tuple.

En list och en tuple kan båda användas för att lagra flera värden i en bestämd ordning. Skillnaden är att en list kan ändras efter att den har skapats, medan en tuple är oföränderlig. Det betyder att man kan lägga till, ändra och ta bort värden i en list, men inte i en tuple. En tuple passar därför bra när man vill spara information som inte ska kunna ändras, till exempel koordinater eller ett datum.

### Fråga 3 – Vad gör en dictionary användbar? När passar det att använda den?

En dictionary används för att lagra data i par med en nyckel och ett värde. Man kan sedan använda nyckeln för att hitta det värde man söker efter. Det gör en dictionary användbar när information behöver kopplas ihop, till exempel ett namn med ett telefonnummer eller en produkt med ett pris. En dictionary passar därför bra när man vill kunna söka efter information genom att använda en tydlig nyckel.

### Fråga 4 – Vad är ett set och hur skiljer det sig från en lista?

Ett set är en samling värden där varje värde bara kan förekomma en gång. Sets har ingen bestämd ordning och man kan därför inte använda index för att komma åt ett specifikt värde. En lista är däremot ordnad, kan ändras och tillåter att samma värde förekommer flera gånger. Ett set passar därför bra när man vill lagra unika värden och automatiskt undvika dubbletter, till exempel användarnamn.

### Fråga 5 – Vad menas med ett användargränssnitt och varför är det viktigt i program?

Ett användargränssnitt är det sätt som användaren interagerar med ett program på. I ett program som körs i terminalen kan användargränssnittet till exempel bestå av menyer, frågor med `input()` och information som visas med `print()`. Ett tydligt användargränssnitt gör det enklare för användaren att förstå vad programmet gör och vilka val som finns. Det är också viktigt att ge tydlig återkoppling och hantera felaktig inmatning så att programmet blir lättare att använda.