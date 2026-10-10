# Hjälp – öppna rätt steg

Prova först själv, kör `python main.py` och jämför med kontrollpunkten i README. Läs bara ledtråden för det steg där du sitter fast. Ledtrådarna visar riktning, inte en färdig lösning.

## Steg 1 – huvudmeny

Vilken boolean variable avgör om huvudmenyn ska visas igen? Låt alla menyval ske **inne i** `while`-loopen. Val `4` ska ändra loopens villkor; de andra valen ska inte göra det. Kontrollera först att `4` avslutar innan du bygger mer.

## Steg 2 – förstå `Animal`

`__init__` körs varje gång ett nytt object skapas. Titta på varje rad som börjar med `self.`: värdet hör till just det objectet. Vilket startvärde tilldelas hunger varje gång?

## Steg 3 – ett djur för hand

`Animal` behöver tre arguments i samma ordning som dess `__init__`: ID, namn, art. Lägg provraderna **före** menyloopen så att de inte skrivs ut på nytt vid varje menyval. Läs sedan attributes via ditt nya object.

## Steg 4 – lägga till

Spara objectet under samma ID som användaren skrev. Fråga **innan** du lägger till: finns den keyn redan i `animals`? Vid ja ska du lämna functionen innan den frågar efter namn eller ändrar dictionaryt. Två olika ID ska ge två entries.

## Steg 5 – lista

En `for`-loop kan ge dig en key i taget från ett dictionary. Med den keyn kan du hämta objectet och läsa `name` och `species`. Fundera först på vad du vill skriva när `animals` är tomt.

## Steg 6 – välja

Använd samma typ av ID som när du sparade djuret: en sträng. Kontrollera att keyn finns **före** du läser `animals[animal_id]`; annars kan programmet krascha. Att välja djur skapar inte ett nytt `Animal`.

## Steg 7 – djurmeny

Huvudmenyn och djurmenyn har olika uppgifter. Låt djurmenyn få det redan valda objectet som parameter. När användaren väljer `3` ska bara djurmenyn avslutas, så att huvudmenyn kan fortsätta.

## Steg 8 – mata

Vilket attribute ska `feed()` ändra? `self` är det valda djuret. Kontrollera `amount` **innan** hunger ändras. Om mängden är större än kvarvarande hunger ska slutvärdet vara `0`, inte ett negativt tal. Ett `False`-svar ska betyda att hunger är exakt samma som före anropet.

## Steg 9 – status

Visa `name`, `species` och `hunger` från **det object som skickades till djurmenyn**. En statusvisning ska bara läsa state. Om samma värde visas före och efter matning, kontrollera att du inte skriver ut ett gammalt fast tal i stället för objectets attribute.

## Steg 10 – separata objects

Skriv upp förväntat resultat för A och B innan du kör. När du matar A, kontrollera vilket object som får method-anropet. Ett dictionary innehåller referenser till flera olika objects; rätt key måste leda till rätt object.

## Steg 11 – validation function

Det är tillåtet att ha en vanlig function som bara **svarar** på om ett ID får användas. Den behöver läsa ID och dictionaryt men inte skapa ett object. Låt funktionen svara `False` om ID är tomt eller redan finns. Placera anropet före första state-ändringen i `add_animal()`.

## Steg 12 – helheten

Följ ett menyval i taget: var skapas `animals`, var sparas objectet, var hämtas det, och var ändras hunger? Om ett nekat försök ändå ändrar något, leta efter en tilldelning som sker **före** valideringen. Ta bort tillfälliga provrader när helhetsflödet fungerar.

## När något inte fungerar

Läs sista raden i en traceback och sedan fil och radnummer. Kontrollera indrag under `def`, `if` och `while`, stavning av dictionary-keys och att terminalen står i mappen med `main.py`. Kör efter en liten ändring. Om du ber om hjälp, visa vilket steg du gör, exakt input, förväntat resultat och faktiskt resultat.
