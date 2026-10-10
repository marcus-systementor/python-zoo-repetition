# Djurparken – repetition av Python

Bygg ett litet terminalprogram för en djurpark under torsdag/fredags självstudier. Du får repetera `while`, menyval, `dict`, functions, en `class`, flera objects, methods, separat `state` och validering i **ett** program. Samma byggstenar är användbara i kommande uppgifter, men djurparken har egna regler och är ingen lösning på Bankomat-inlämningen.

Detta är en **stor men enkel repetitionslabb**. Arbeta i små steg, kör ofta och pausa gärna vid en fungerande kontrollpunkt. Du behöver inte göra allt på en gång. Ingen file I/O, databas, automatiserad testing, externa packages eller inheritance behövs i grundlabben.

## Börja här

Om du får labben som en publik GitHub-template: välj **Use this template → Create a new repository**, skapa normalt ett eget **Private** repository och klona det till din dator. Öppna terminalen i mappen med denna README. Kör:

```text
python main.py
```

På Windows kan `py main.py` fungera; på vissa datorer `python3 main.py`. Startprogrammet skriver ett välkomstmeddelande, visar **0 djur** och avslutas utan fel. I [animal.py](animal.py) finns redan en liten `Animal`-class, men ingen färdig `feed()`-method. I [main.py](main.py) finns ett tomt `animals`-dictionary och en körbar start. Du bygger resten.

Filerna du ändrar är `main.py` och `animal.py`. [HJALP.md](HJALP.md) ger ledtrådar för varje steg och [REFLECTION.md](REFLECTION.md) innehåller korta frågor. **Facit finns i `facit/`. Försök först bygga funktionaliteten själv innan du jämför.** Facit är ett möjligt sätt, inte det enda.

Spara gärna en liten `commit` efter ett fungerande steg. Exempel: `Add main menu`, `Explore Animal objects`, `Complete zoo flow`. Om ett steg bara är läsning eller kontroll kan du skriva en kort anteckning i `REFLECTION.md` före din `commit`.

### Enkla regler för programmet

- Varje djur har ett `animal_id` som är en **sträng** från `input()`, till exempel `"1"` eller `"lion-1"`. Använd samma sträng som key i `animals`. Försök inte konvertera ID till `int`.
- Ett nytt djur börjar med `hunger = 5`. Skalan är `0` (inte hungrig) till `10` (mycket hungrig). Matning måste vara större än `0` och får inte vara större än djurets aktuella hunger. En nekad matning ska lämna hunger oförändrad.
- När du matar anger du i grundlabben ett **heltal**. Prova både positiva, noll och negativa heltal samt ett värde större än hunger. Du behöver inte hantera text som `abc` i mängdfältet; exception handling ingår inte.
- Ett duplicerat ID får inte ersätta ett befintligt object. En nekad operation ska lämna `state` oförändrat.

## Steg 1 – huvudmeny med `while`

**Mål:** Håll programmet igång tills användaren väljer att avsluta.

**Gör:** I `main.py`, behåll `animals = {}` inuti `main()`. Lägg till en boolean variable som styr en `while`-loop. Visa valen `1. Lägg till djur`, `2. Lista djur`, `3. Välj djur`, `4. Avsluta`, läs valet med `input()` och använd `if`/`elif`/`else`. Vid `4` avslutas loopen. Låt `1`–`3` tills vidare skriva ett kort meddelande som ”Kommer senare”; de ska inte krascha. Okända val ska ge ett meddelande och visa menyn igen. Om du behöver minnas loopformen:

```python
running = True

while running:
    # Show menu, read choice, and handle it.
```

**Kontroll:** Kör `python main.py`; välj `2`, ett okänt val och sedan `4`. Menyn ska visas på nytt efter de första två valen och programmet ska avslutas efter `4`.

**Commit:** `Add main menu`

## Steg 2 – förstå och prova `Animal`

**Mål:** Se vad som hör till ett enskilt object.

**Gör:** Läs `animal.py` och identifiera `class`, `__init__`, `self`, attributes och `state`. Skriv kort i `REFLECTION.md`: vilka värden tillhör varje djur, vad får ett nytt djur för hunger och delar två objects samma hunger? Skapa sedan tillfälligt ett `Animal`-object i `main.py`, före menyloopen, och skriv ut dess attributes. Kontrollera att hunger börjar på `5`. Ta bort provkoden när nästa steg fungerar.

**Kontroll:** Kör `python main.py`: före menyn syns ID `1`, namn `Leo`, art `Lion` och hunger `5`. Du kan förklara varför `self.hunger = 5` körs för varje nytt `Animal`-object.

**Commit:** `Explore Animal objects`

## Steg 3 – lägg till djur

**Mål:** Spara flera `Animal`-objects utan att skriva över ett befintligt.

**Gör:** Skapa en vanlig function i `main.py`, till exempel `add_animal(animals)`, ovanför `main()`. Be om ID med `input()`. **Innan** du skapar ett object: kontrollera om ID redan finns som key i dictionaryt. Om det finns, visa ett meddelande, avbryt och ändra inget. Annars fråga efter namn och art, skapa ett `Animal`-object, spara det under ID-keyn och meddela att det lades till. Koppla huvudmenyns val `1` till functionen. Behåll `animals` utanför menyloopen men inuti `main()`, så att djuren finns kvar mellan menyval. Ta bort det tillfälliga djuret från steg 2.

**Kontroll:** Starta programmet, lägg till `1`/`Leo`/`Lion` och sedan `2`/`Mira`/`Monkey`. Prova därefter ID `1` igen. Det ska nekas **innan** du frågar efter nytt namn; dictionaryt ska fortfarande ha exakt två entries och Leo ska inte ha bytts ut.

## Steg 4 – lista djur

**Mål:** Visa allt som sparats i dictionaryt.

**Gör:** Skapa en function i `main.py`, till exempel `list_animals(animals)`, och anropa den vid menyval `2`. Använd en `for`-loop över dictionaryts keys; för varje key hämtar du dess `Animal`-object och skriver minst ID, namn och art. Du får också visa hunger. Vid tomt dictionary: skriv ”Inga djur” i stället för en tom utskrift.

**Kontroll:** Före registrering visar val `2` att listan är tom. Lägg sedan till Leo och Mira och välj `2` igen: båda visas, med sina egna ID. Prova att ge dem olika namn och se att rätt namn hamnar på rätt rad.

## Steg 5 – hitta och välj rätt djur

**Mål:** Hämta ett befintligt object via dess ID-key.

**Gör:** Byt ut platshållaren för huvudmenyns val `3`. Fråga efter `animal_id`. Om keyn finns i `animals`, hämta objectet och skriv till exempel dess namn. Om keyn saknas, skriv ett tydligt meddelande och återgå till huvudmenyn. Skapa inte ett nytt object när du bara ska hitta ett befintligt.

**Kontroll:** Lägg till `1`/`Leo` och `2`/`Mira`. Välj ID `2`: Mira ska visas, inte Leo. Välj ett ID som saknas, till exempel `9`: programmet ska fortsätta och huvudmenyn visas igen.

## Steg 6 – djurmeny

**Mål:** Arbeta vidare med **samma** object som användaren nyss valde.

**Gör:** Skapa en function i `main.py`, till exempel `animal_menu(animal)`, som tar det valda objectet som parameter. Ge den en egen enkel `while` med `1. Visa status`, `2. Mata djuret`, `3. Tillbaka`. Koppla huvudmenyns lyckade uppslagning från steg 5 till denna function. Vid `3` återgår du till huvudmenyn, inte ut ur hela programmet. Låt `1` och `2` tills vidare visa ”Kommer senare”. Ett okänt val ska stanna i djurmenyn.

**Kontroll:** Välj ett befintligt djur, välj `1`, välj `3` och välj sedan `4` i huvudmenyn. Du ska se djurmenyn igen efter `1`, huvudmenyn efter `3` och lämna programmet efter `4`. Prova också ett okänt val i djurmenyn.

## Steg 7 – `feed()` med validering

**Mål:** Låta ett `Animal`-object skydda sin egen hunger.

**Gör:** Lägg till `feed(self, amount)` i `animal.py`. Tillåten matning är `0 < amount <= animal.hunger`. Validera **före state-förändringen**: vid ogiltigt värde returnerar metoden `False` och hunger förblir oförändrad. Vid giltigt värde minskar hunger med `amount` och metoden returnerar `True`. Koppla djurmenyns val `2` till att läsa ett heltal med `int(input(...))`, anropa det valda objectets `feed()` och skriva ett tydligt meddelande utifrån dess bool-svar. I denna labb antar vi att användaren skriver ett heltal; ingen exception handling behövs.

**Kontroll:**

```text
Nytt djur: hunger = 5
feed(2) → True, hunger = 3
feed(0) → False, hunger oförändrad
feed(-2) → False, hunger oförändrad

hunger = 1
feed(5) → False, hunger = 1
feed(1) → True, hunger = 0
```

Prova via menyn och skriv tillfälligt ut `animal.hunger` om statusvalet ännu inte är klart.

**Commit:** `Add feed method`

## Steg 8 – visa status

**Mål:** Visa det aktuella objectets `state` utan att ändra det.

**Gör:** Ersätt platshållaren för djurmenyns val `1`. Visa namn, art och hunger, till exempel `Name: Leo`, `Species: Lion`, `Hunger: 3/10`. Du får välja en method på `Animal` som returnerar text eller en vanlig function i `main.py` som skriver text. Välj ett sätt och var beredd att förklara varför det passar.

**Kontroll:** Välj Leo, visa status, mata med `2` och visa status igen: hunger ska gå från `5/10` till `3/10`, medan namn och art är oförändrade. Välj `3` och återvänd till huvudmenyn.

## Steg 9 – fristående validation function

**Mål:** Skilja en vanlig function från en method på ett object.

**Gör:** Flytta kontrollen av ID i steg 3 till en liten fristående validation function ovanför `add_animal()` i `main.py`, till exempel `can_add_animal(animals, animal_id)`. Den ska **bara** svara `True` eller `False` och inte ändra dictionaryt. Ett ID är tillåtet när det inte är tomt och inte redan används. Låt `add_animal()` anropa den **före** namn/art efterfrågas och före dictionaryt ändras. `feed()` stannar som method, eftersom den ändrar ett bestämt djurs hunger.

**Kontroll:** Ett nytt ID tillåts. Tomt ID och ett befintligt ID nekas utan nytt object eller ändrat dictionary. Efter nekade försök kan du fortfarande välja och visa de djur som fanns tidigare.

## Steg 10 – hela programmet och separat state

**Mål:** Ha ett sammanhängande program, inte separata provbitar.

**Gör:** Ta bort tillfälliga utskrifter och ”Kommer senare”-grenar. Skapa minst två djur och kontrollera att de har separat state. Mata endast ett av dem och kontrollera att det andra inte påverkas. Kör hela huvudmeny → dictionary → object → djurmeny → method → validation-flödet. Läs sedan [REFLECTION.md](REFLECTION.md) och förklara hur delarna hänger ihop. Kontrollera att `animal.py` inte innehåller menylogik och att `main.py` inte ändrar hunger direkt. Du ska kunna peka ut en vanlig validation function, en method, två olika objects, två `while`-loopar, var state ändras och var state skyddas.

**Kontroll:** Hela flödet fungerar från `python main.py` till avslut. Förutsäg vad som händer med båda djuren innan du matar det ena.

**Commit:** `Complete zoo flow`

## Kontrollera hela flödet

Kör manuellt från ett tomt program:

1. Lägg till djur A (`1`, `Leo`, `Lion`).
2. Lägg till djur B (`2`, `Mira`, `Monkey`).
3. Försök lägga till ett nytt djur med ID `1`. Det ska nekas; Leo finns kvar.
4. Lista djuren. Båda ska visas, inte tre djur.
5. Välj djur A och mata med `2`: hunger går från `5` till `3`.
6. Kontrollera att djur B fortfarande har hunger `5`.
7. Försök mata djur B med `0`: nekas, hunger kvar `5`.
8. Försök mata djur B med `-2`: nekas, hunger kvar `5`.
9. Försök mata djur B med `8`: nekas, hunger kvar `5`.
10. Mata djur B med `5`: lyckas, hunger blir `0`.
11. Prova ett saknat ID.
12. Avsluta via huvudmenyn.

Om detta fungerar har du repeterat flera av kursens viktigaste byggstenar i ett sammanhängande program.

## Frivilligt efter grundlabben

Välj **högst en** bonus så att projektet inte blir för stort:

- **Aktivitetshistorik:** Lägg till `self.history = []` i varje `Animal`. Lägg till en enkel sträng, exempelvis `Fed 2`, endast när en matning lyckas, och visa sedan historiken. Varje object ska ha sin egen history-list. Bonusen kräver inte file I/O och ingår inte i grundlabben.
- **Inheritance:** Skapa exempelvis `class Lion(Animal):` med en egen liten method eller en enkel override. Detta är inte ett krav och behövs inte för menyflödet.
- **Fler actions eller mer state:** Lägg till till exempel `play()` eller `sleep()`, eller pröva `energy` eller `happiness`, men bestäm först vilka förändringar som är tillåtna.

Om du fastnar: läs [HJALP.md](HJALP.md) för just ditt steg, kör efter en liten ändring och jämför det faktiska resultatet med kontrollpunkten. Vid traceback: börja med sista raden, hitta fil och radnummer och kontrollera särskilt indrag, key-namn och vilken meny du är i. Be om hjälp med vad du körde, vad du väntade dig och vad som faktiskt hände.
