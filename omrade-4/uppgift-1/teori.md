# Område 4 – Felsökning, feltyper och kodkvalitet

## Fråga 1 – Syntaxfel, logiska fel och exekveringsfel

Syntaxfel innebär att koden bryter mot reglerna för hur Python ska skrivas. Ett exempel är om man glömmer kolon efter en if-sats, eftersom Python då inte kan tolka programmets struktur och programmet inte kan köras. Ett logiskt fel är annorlunda eftersom programmet kan köras utan att visa ett felmeddelande, men ändå ge fel resultat. Exempelvis kan man råka använda `+` istället för `-` i en beräkning och då fungerar programmet tekniskt men resultatet blir fel. Ett exekveringsfel uppstår när programmet körs och något går fel under körningen, till exempel om programmet försöker dividera ett tal med noll. Skillnaden är alltså framför allt när och hur felet uppstår: syntaxfel hindrar Python från att tolka koden, logiska fel ger felaktigt resultat och exekveringsfel uppstår medan programmet körs.

## Fråga 2 – Vanligt fel i Python

Ett vanligt fel i Python är att försöka omvandla text till ett heltal med `int()` när texten inte innehåller ett giltigt tal. Till exempel kan `int("hej")` orsaka ett `ValueError`, eftersom Python inte kan omvandla ordet "hej" till ett heltal. Felet upptäcks normalt när programmet körs och Python visar ett felmeddelande som talar om vilken typ av fel som uppstod och var i koden det inträffade. För att åtgärda problemet kan man kontrollera användarens inmatning med `try` och `except ValueError`. På så sätt kan programmet ge användaren ett tydligt felmeddelande istället för att krascha. Det är ett exempel på hur felsökning både kan användas för att hitta ett fel och för att förebygga att samma typ av fel påverkar användaren.

## Fråga 3 – Kommentarer och tydliga variabelnamn

Kommentarer och tydliga variabelnamn gör koden lättare att förstå och kan därför minska risken för fel. Ett tydligt variabelnamn som `total_summa` visar vad variabeln innehåller, medan ett otydligt namn som `x` gör det svårare att förstå hur variabeln används. Kommentarer kan förklara syftet med en del av koden, särskilt om den innehåller logik som annars kan vara svår att följa. När koden är lätt att läsa blir det enklare att upptäcka exempelvis felaktiga beräkningar eller att en variabel används på fel sätt. Det blir också lättare för en annan programmerare att förstå och felsöka koden. På så sätt fungerar tydliga namn och relevanta kommentarer som en förebyggande åtgärd eftersom de minskar risken för att fel uppstår eller blir svåra att hitta.

## Fråga 4 – Förebyggande felsökning

Förebyggande felsökning innebär att man försöker upptäcka och förhindra fel innan de leder till problem i ett färdigt program. Ett sätt är att testa koden ofta och med olika typer av inmatningar till exempel både giltiga och ogiltiga värden. Man kan också förebygga fel genom att använda tydliga variabelnamn, korrekt kodstruktur och kommentarer som gör koden lättare att förstå. Vid inmatning från en användare kan man dessutom använda exempelvis `try` och `except` för att hantera felaktiga värden på ett kontrollerat sätt. På så sätt minskar risken att programmet kraschar eller ger ett oväntat resultat. Förebyggande felsökning handlar därför inte bara om att rätta fel som redan har uppstått utan också om att bygga programmet på ett sätt som minskar risken för fel från början.

## Fråga 5 – Social och etisk aspekt av programmering

En social och etisk aspekt av programmering är tillgänglighet. När man utvecklar ett program behöver man tänka på att användare kan ha olika förutsättningar, till exempel nedsatt syn, motoriska svårigheter eller begränsad teknisk erfarenhet. Om ett program bara är utformat för användare utan sådana begränsningar kan vissa grupper få svårare att använda tjänsten och därmed hamna utanför. Programmeraren har därför ett ansvar att försöka skapa lösningar som fungerar för så många användare som möjligt, exempelvis genom tydlig information, begriplig felhantering och en lättanvänd design. Samtidigt kan det finnas en intressekonflikt mellan att göra en lösning så tillgänglig som möjligt och att begränsas av tid, pengar eller tekniska förutsättningar. Därför är tillgänglighet inte bara en teknisk fråga utan också en fråga om jämlikhet och vilka människor som får möjlighet att använda tekniken.

## Praktisk uppgift 3 – Dokumentation och reflektion

### Dokumentation av programmet

Jag har dokumenterat koden genom att använda kommentarer som förklarar vad olika delar av programmet gör. Jag har även använt tydliga variabelnamn, till exempel `tal1`, `tal2`, `summa` och `heltal`. Det gör koden lättare att förstå och gör det enklare att hitta och åtgärda fel. Jag har också testat programmen med både giltig och ogiltig inmatning för att kontrollera hur programmen reagerar.

### Möjliga fel och hur de påverkar användaren

Ett möjligt fel är att användaren skriver text när programmet förväntar sig ett heltal. Om detta inte hanteras kan programmet ge ett `ValueError` och avslutas. Jag testade detta genom att skriva in `hej` istället för ett heltal och kunde då se att felet uppstod. I programmet `inmatning.py` används därför `try` och `except ValueError` för att fånga felet och visa ett tydligt felmeddelande istället. På så sätt får användaren information om vad som blev fel istället för att programmet kraschar.

### Sociala och etiska aspekter

Ett program bör vara utformat så att så många användare som möjligt kan förstå och använda det. Tydliga instruktioner och felmeddelanden är därför viktiga för tillgängligheten. Om ett program bara fungerar när användaren skriver exakt rätt typ av information kan vissa användare få svårare att använda det. Genom tydliga meddelanden och felhantering kan man minska risken för att användaren hamnar i en situation där programmet kraschar eller blir svårt att förstå.