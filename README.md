# Djurparken – repetition av Python

Bygg ett litet terminalprogram för en djurpark under torsdag/fredags självstudier. Du får repetera `while`, menyval, `dict`, functions, en `class`, flera objects, methods, separat `state` och validering i **ett** program. Samma byggstenar är användbara i kommande uppgifter, men djurparken har egna regler och är ingen lösning på Bankomat-inlämningen.

Detta är en **stor men enkel repetitionslabb**. Arbeta i små steg, kör ofta och pausa gärna vid en fungerande kontrollpunkt. Du behöver inte göra allt på en gång. Inga extra paket, filer, automatiserade test eller inheritance behövs i grundlabben.

## Börja här

Om du får labben som en publik GitHub-template: välj **Use this template → Create a new repository**, skapa normalt ett eget **Private** repository och klona det till din dator. Öppna terminalen i mappen med denna README. Kör:

```text
python main.py
```

På Windows kan `py main.py` fungera; på vissa datorer `python3 main.py`. Startprogrammet skriver ett välkomstmeddelande, visar **0 djur** och avslutas utan fel. I [animal.py](animal.py) finns redan en liten `Animal`-class, men ingen färdig `feed()`-method. I [main.py](main.py) finns ett tomt `animals`-dictionary och en körbar start. Du bygger resten.

Filerna du ändrar är `main.py` och `animal.py`. [HJALP.md](HJALP.md) ger ledtrådar för varje steg och [REFLECTION.md](REFLECTION.md) innehåller korta frågor. **Facit finns i `facit/`. Försök först bygga funktionaliteten själv innan du jämför.** Facit är ett möjligt sätt, inte det enda.

Spara gärna en liten `commit` efter ett fungerande steg. Exempel: `Add main menu`, `Add animal lookup`, `Add feed method`. Om ett steg bara är läsning eller kontroll kan du skriva en kort anteckning i `REFLECTION.md` före din `commit`.

### Enkla regler för programmet

- Varje djur har ett `animal_id` som är en **sträng** från `input()`, till exempel `"1"` eller `"lion-1"`. Använd samma sträng som key i `animals`. Försök inte konvertera ID till `int`.
- Ett nytt djur börjar med `hunger = 5`. Skalan är `0` (inte hungrig) till `10` (mycket hungrig). Matning minskar hunger, aldrig under `0`.
- När du matar anger du i grundlabben ett **heltal**. Prova både positiva och icke-positiva heltal. Du behöver inte hantera text som `abc` i mängdfältet; exception handling ingår inte.
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

## Steg 2 – förstå `Animal`

**Mål:** Se vad som hör till ett enskilt object.

**Gör:** Läs `animal.py`. Peka ut `class`, `__init__`, `self` och attributes. Skriv kort i `REFLECTION.md`: vilka värden tillhör varje djur, vad får ett nytt djur för hunger och delar två objects samma hunger? Ändra inte class-koden än.

**Kontroll:** Kör `python main.py` igen. Programmet ska fortfarande fungera. Du kan förklara varför `self.hunger = 5` körs för varje nytt `Animal`-object.

**Commit:** `Explain Animal state`

## Steg 3 – ett djur för hand

**Mål:** Skapa och läsa ett object innan du bygger registrering.

**Gör:** I `main()` i `main.py`, **före** menyns `while`-loop, skapa tillfälligt ett `Animal` med ID `"1"`, namn `"Leo"` och art `"Lion"`. Skriv ut dess fyra attributes med `print()`. Lägg inte detta djur i `animals` ännu. När steg 4 fungerar tar du bort de tillfälliga raderna, så att bara registrerade djur finns i programmet.

**Kontroll:** Kör programmet: före menyn syns ID `1`, namn `Leo`, art `Lion` och hunger `5`. Byt tillfälligt namnet till `Mira`, kör igen och se att rätt object-värde visas. Återställ eller ta bort provraderna i nästa steg.

**Commit:** `Create first Animal object`

## Steg 4 – lägg till djur

**Mål:** Spara flera `Animal`-objects utan att skriva över ett befintligt.

**Gör:** Skapa en vanlig function i `main.py`, till exempel `add_animal(animals)`, ovanför `main()`. Be om ID med `input()`. **Innan** du skapar ett object: kontrollera om ID redan finns som key i dictionaryt. Om det finns, visa ett meddelande, avbryt och ändra inget. Annars fråga efter namn och art, skapa ett `Animal`-object, spara det under ID-keyn och meddela att det lades till. Koppla huvudmenyns val `1` till functionen. Behåll `animals` utanför menyloopen men inuti `main()`, så att djuren finns kvar mellan menyval. Ta nu bort det tillfälliga djuret från steg 3.

**Kontroll:** Starta programmet, lägg till `1`/`Leo`/`Lion` och sedan `2`/`Mira`/`Monkey`. Prova därefter ID `1` igen. Det ska nekas **innan** du frågar efter nytt namn; dictionaryt ska fortfarande ha exakt två entries och Leo ska inte ha bytts ut. Du kan tillfälligt skriva `len(animals)` efter ett menyval för att kontrollera antalet.

**Commit:** `Add animal creation`

## Steg 5 – lista djur

**Mål:** Visa allt som sparats i dictionaryt.

**Gör:** Skapa en function i `main.py`, till exempel `list_animals(animals)`, och anropa den vid menyval `2`. Använd en `for`-loop över dictionaryts keys; för varje key hämtar du dess `Animal`-object och skriver minst ID, namn och art. Du får också visa hunger. Vid tomt dictionary: skriv ”Inga djur” i stället för en tom utskrift.

**Kontroll:** Före registrering visar val `2` att listan är tom. Lägg sedan till Leo och Mira och välj `2` igen: båda visas, med sina egna ID. Prova att ge dem olika namn och se att rätt namn hamnar på rätt rad.

**Commit:** `List registered animals`

## Steg 6 – hitta och välj rätt djur

**Mål:** Hämta ett befintligt object via dess ID-key.

**Gör:** Byt ut platshållaren för huvudmenyns val `3`. Fråga efter `animal_id`. Om keyn finns i `animals`, hämta objectet och skriv till exempel dess namn. Om keyn saknas, skriv ett tydligt meddelande och återgå till huvudmenyn. Skapa inte ett nytt object när du bara ska hitta ett befintligt.

**Kontroll:** Lägg till `1`/`Leo` och `2`/`Mira`. Välj ID `2`: Mira ska visas, inte Leo. Välj ett ID som saknas, till exempel `9`: programmet ska fortsätta och huvudmenyn visas igen.

**Commit:** `Add animal lookup`

## Steg 7 – en meny för valt djur

**Mål:** Arbeta vidare med **samma** object som användaren nyss valde.

**Gör:** Skapa en function i `main.py`, till exempel `animal_menu(animal)`, som tar det valda objectet som parameter. Ge den en egen enkel `while` med `1. Visa status`, `2. Mata djuret`, `3. Tillbaka`. Koppla huvudmenyns lyckade uppslagning från steg 6 till denna function. Vid `3` återgår du till huvudmenyn, inte ut ur hela programmet. Låt `1` och `2` tills vidare visa ”Kommer senare”. Ett okänt val ska stanna i djurmenyn.

**Kontroll:** Välj ett befintligt djur, välj `1`, välj `3` och välj sedan `4` i huvudmenyn. Du ska se djurmenyn igen efter `1`, huvudmenyn efter `3` och lämna programmet efter `4`. Prova också ett okänt val i djurmenyn.

**Commit:** `Add animal menu`

## Steg 8 – `feed()` med validering

**Mål:** Låta ett `Animal`-object skydda sin egen hunger.

**Gör:** Lägg till `feed(self, amount)` i `animal.py`. Om `amount` är `0` eller negativt: returnera `False` **utan** att ändra `self.hunger`. Om `amount` är positivt: minska hunger, men stanna vid `0` om mängden är större än nuvarande hunger; returnera sedan `True`. Koppla djurmenyns val `2` till att läsa ett heltal med `int(input(...))`, anropa det valda objectets `feed()` och skriva ett tydligt meddelande utifrån dess bool-svar. I denna labb antar vi att användaren skriver ett heltal; ingen exception handling behövs.

**Kontroll:** För ett nytt djur ger `feed(2)` hunger `3`. Ett nytt djur med hunger `5` som får `feed(0)` eller `feed(-2)` stannar på `5` och anropet ger `False`. Om hunger är `1` och du matar med `5` blir den `0`, **inte** `-4`. Prova via menyn och skriv tillfälligt ut `animal.hunger` om statusvalet ännu inte är klart.

**Commit:** `Add feed method`

## Steg 9 – visa djurets status

**Mål:** Visa det aktuella objectets `state` utan att ändra det.

**Gör:** Ersätt platshållaren för djurmenyns val `1`. Visa namn, art och hunger, till exempel `Name: Leo`, `Species: Lion`, `Hunger: 3/10`. Du får välja en method på `Animal` som returnerar text eller en vanlig function i `main.py` som skriver text. Välj ett sätt och var beredd att förklara varför det passar.

**Kontroll:** Välj Leo, visa status, mata med `2` och visa status igen: hunger ska gå från `5/10` till `3/10`, medan namn och art är oförändrade. Välj `3` och återvänd till huvudmenyn.

**Commit:** `Show animal status`

## Steg 10 – två objects, två olika states

**Mål:** Kontrollera att varje `Animal`-object har eget `state`.

**Gör:** Registrera minst två djur i en ny körning. Visa bådas hunger. Mata **bara** det första djuret. Visa bådas status igen. Förutsäg resultaten innan du kör.

**Kontroll:** Om Leo och Mira börjar på `5`, och bara Leo matas med `2`, ska Leo visa `3/10` medan Mira fortfarande visar `5/10`. Kör sedan ett separat försök där bara Mira matas. Om båda ändras av ett anrop har du sannolikt använt fel object i djurmenyn.

**Commit:** `Verify independent animal state`

## Steg 11 – en fristående validation function

**Mål:** Skilja en vanlig function från en method på ett object.

**Gör:** Flytta kontrollen av ID i steg 4 till en liten fristående validation function ovanför `add_animal()` i `main.py`, till exempel `can_add_animal(animals, animal_id)`. Den ska **bara** svara `True` eller `False` och inte ändra dictionaryt. Ett ID är tillåtet när det inte är tomt och inte redan används. Låt `add_animal()` anropa den **före** namn/art efterfrågas och före dictionaryt ändras. `feed()` stannar som method, eftersom den ändrar ett bestämt djurs hunger.

**Kontroll:** Ett nytt ID tillåts. Tomt ID och ett befintligt ID nekas utan nytt object eller ändrat dictionary. Efter nekade försök kan du fortfarande välja och visa de djur som fanns tidigare.

**Commit:** `Add animal ID validation`

## Steg 12 – koppla ihop och förklara

**Mål:** Ha ett sammanhängande program, inte separata provbitar.

**Gör:** Ta bort tillfälliga utskrifter och ”Kommer senare”-grenar. Följ helhetskontrollen nedan. Läs sedan [REFLECTION.md](REFLECTION.md) och förklara hur `while` → huvudmeny → dictionary → valt object → djurmeny → method → validering hänger ihop. Kontrollera att `animal.py` inte innehåller menylogik och att `main.py` inte ändrar hunger direkt.

**Kontroll:** Hela flödet fungerar från `python main.py` till avslut. Du kan peka ut en validation function, en operation i en method, två oberoende objects och var båda menylooparna slutar.

**Commit:** `Complete zoo flow`

## Kontrollera hela flödet

Kör manuellt från ett tomt program:

1. Starta programmet och lägg till djur A (`1`, `Leo`, `Lion`).
2. Lägg till djur B (`2`, `Mira`, `Monkey`).
3. Försök lägga till ett nytt djur med ID `1`. Det ska nekas; Leo finns kvar.
4. Lista djuren. Båda ska visas, inte tre djur.
5. Välj djur A och visa status (`5/10`). Mata med `2`; visa status igen (`3/10`).
6. Gå tillbaka, välj djur B och se att hunger fortfarande är `5/10`.
7. Försök mata B med `0` och `-2`. Båda nekas och hunger förblir `5/10`.
8. Mata B med `8`. Hunger ska bli `0/10`, aldrig negativ.
9. Gå tillbaka, prova ett saknat ID och avsluta programmet via huvudmenyn.

Om detta fungerar har du repeterat flera av kursens viktigaste byggstenar i ett sammanhängande program.

## Frivilligt efter grundlabben

Välj **högst en** bonus så att projektet inte blir för stort:

- **Inheritance:** skapa exempelvis `class Lion(Animal):` med en egen liten method eller en enkel override. Detta är inte ett krav och behövs inte för menyflödet.
- **Fler actions:** lägg till till exempel `play()` eller `sleep()` med en tydlig regel.
- **Mer state:** pröva `energy` eller `happiness`, men bestäm först vilka förändringar som är tillåtna.

Om du fastnar: läs [HJALP.md](HJALP.md) för just ditt steg, kör efter en liten ändring och jämför det faktiska resultatet med kontrollpunkten. Vid traceback: börja med sista raden, hitta fil och radnummer och kontrollera särskilt indrag, key-namn och vilken meny du är i. Be om hjälp med vad du körde, vad du väntade dig och vad som faktiskt hände.
