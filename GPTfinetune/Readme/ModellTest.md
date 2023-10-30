# Modells 

Um die Funktionsweise des Trainings und auch des Codes zu verstehen, habe ich hier noch einen kleinen Artikel geschrieben:

[Funktionsweise-Code]()

>[!NOTE]
> Um die Modelle miteinander zu vergleichen, werden sie auf dem selben Test getestet, und auch einem zu vor nie gesehenem kurz Test

[Der Test zum Vergleich, Kurztest](https://github.com/cheatoskar/TestGPT-Modell/blob/main/Readme/Test.md)

Die Optimale Antwort waere hierbei diese hier:
```
Fehleranalyse: 
  Aufgabe 1 (6 von 6 Punkte) 
  Aufgabe 2 (6 von 8 Punkte): 
    - "als auch die soziale Disziplinierung" bezieht sich auf " z.B. Durch Bildung usw." Ist falsch! (-1 Punkt) 
    - "ein komplexer und langjähriger Prozess war" Warum? Kriege... ungenau (-1 Punkt) 
  Aufgabe 3 (7 von 7 Punkte)
Insgesamt:
  Punkte: 18 von 21, das entspricht einer Leistung von: 85% 
  Vorgeschlagene Note: 1- 
```

und fuer den Kurztest:
```
Fehleranallyse: 

	Frage 1 (1 von 1 Punkt) 

	Frage 2 (0 von 1 Punkte): 

		- Die berühmte Rede hieß "I have a Dream" (-0,5 Punkte) 

	Frage 3 (0 von 1 Punkte): 

		- er hieß Christopher Kolumbus nicht Kolimbo (-0,5 Punkte) 

	Frage 4 (1 von 1 Punkt) 

	Frage 5 (0,5 von 1 Punkte): 

		- Antwort auf: Welches Amt hatte er vor seiner Präsidentschaft inne? Fehlt! (-0,5 Punkte) 

	Frage 6 (0,5 von 1 Punkte): 

		- Antwort auf: welches spezifische Ereignis markiert das Ende des Krieges? Fehlt! (- 0,5 Punkte) 

 

Insgesamt: 

... 
```
So oder aehnlichm sollte es aussehen, hier habe ich nur dir fehler angegeben, die das Modell im besten fall alle findet.
## Modell v 1.0

#### Gesehener Test Antwort:
```
#Fehleranalyse:

###Aufgabe 1 (5 von 6 Punkten): 
**{Unvollständig/UV} :**- {Zäsuren: Reformation} Reibungspunkt/Theorie hinzufügen. [-0,5 Punkte] **{Beispiel/Ex}
 :**- {Zäsuren: Anwendung Beispiel/AB} Reformation: Was war vorher? [{v:vor 1500}] [keine Punkte erhalten] **{Beispiel/Ex}
 :**- {Übergang: U} Reformation: Was kam danach? [keine Punkte erhalten]   ###Aufgabe 2 (7 von 8 Punkten):
 **{Kommasetzung/KS} :**- {Doppelpunkt: Klospapier} Doppelpunkt nach "Zudem war auch die soziale Disziplinierung,
 z. B. Durch Bildung usw." vergessen. [-0,5 Punkte]   ###Aufgabe 3 (7 von 7 Punkten): ##Insgesamt: Punkte: 19 von
21, Das entspricht einer Leistung von: 90%, Vorgeschlagene Note: 1-  ##Vorgeschlagene Maßnahmen:  ###Aufgabe 1:
{A1} -Bei Begriff Zäsur Reibungspunkte und bei Epochentyp Begründung für den Übergang fehlend. ##Vorgeschlagene
Noten: Aufgabe 1: 5 von 6 Punkten: Note: 83%, Punkte: 5 von 6 , Aufgabe 2: 7 von 8 Punkten: Note:88%, Punkte:
7 von 8, Aufgabe 3: 7 von 7 Punkten: Note: 100%, Punkte: 7 von 7, 
```





### KI-Fehleranalyse (Vergleich):

- Mangelnde Struktur und Aufteilung der Informationen in Abschnitte.
- Verwirrende Verwendung von Sonderzeichen, was die Lesbarkeit beeinträchtigt.
- Fehleridentifizierung ist teilweise ungenau und nicht präzise.
- Fehlerbegründungen sind allgemein und oft unklar in Bezug auf den Kontext.
- Notenvorschläge sind verwirrend und schwer verständlich.
- Antworten sehr lang, hoeren nicht auf, bis zum tokenlimit

#### Bewertung:

>[!WARNING]
>Auf einer Skala von 0 bis 10, wobei 10 das Optimalbild der menschlichen Analyse darstellt, würde ich der KI-Analyse eine Punktzahl von 2/10 geben, da sie Raum für erhebliche Verbesserungen bietet.

> [!NOTE]
> Verbesserungsvorschlaege:
> - Starke Simplifizierung der Fehleranalyse in den Trainingsdaten, Klare Strukturierung
> - Mehr Trainingsdaten, verbesserung von Fehlern in vorhandenen Daten
> - Stopsequenz hinzufügen!
> - Klarheit bei Notenvorschlägen
> - Datenvariation
> - Einbau von Zitierten Fehlern, fuer besseres verstaendnis

## Modell v 1.1

Aenderungen:
- Simplifizierung von Trainingsdaten  
	- Formatierung der Fehleranalyse Weglassen  
	- Sonderzeichen und Klammern weglassen 
	- Mehr Textbasiert arbeiten 
- Hinzufügen der Stopsequenz, damit keine ewig langen antworten generiert Werden 

#### Gesehener Test Antwort:
```
Fehleranalyse:

Aufgabe 1 (6 von 6 Punkten):
- Keine Fehler.

Aufgabe 2 ( 7 von 8 Punkten):
- Aspekt "Konfessionalisierung" fehlt. (-1 Punkt)
- Unklare Aussage in der Schlussfolgerung. (kein Punkt erhalten)
   --> Aussage deutlicher machen. 
        z.B. (...) und die Moderne entstehungsphase langsam eingeleutet wurde.




Aufgabe 3 (4 von 7 Punkte):
- Auslassung einer wesentlichen Information: Idee des Privateigentums Eli. ( -2 Punkt)
- Absatz "Was habe ich gelernt" fehlt! ( -1 Punkt)

Sonstiges:
- es fehlt die Quellenangabe zur Idee des Privateigentums (kein Punkt)

Insgesamt: Punkte: 17 von 21, das entspricht einer Leistung von: 81% Vorgeschlagene Note: 2   
```
### KI-Fehleranalyse (Vergleich) vorheriges Modell:

- Unpräzise Fehleridentifikation und -begründungen.
- Mangelnde Klarheit in einigen Teilen der Analyse.
- Punktabzüge aufgrund des Fehlens von Aspekten und Unklarheiten in der Schlussfolgerung.

- Fehleranalyse weniger durcheinander, nur vereinzelt. 
- Form und Formatierung, teils verändert
- KI kann selbst Punkte fuer Aufgaben festlegen, slebst wenn diese nicht angegeben sind

- Noten stimmen grob mit dem des Lehrers ueberein

>[!WARNING]
 > Wenn man den selben Test mehrmals korrigieren laesst, kommen abweichende ergebnisse heraus!

### Kurztest:
```
Fehleranalyse:

- In der Antwort zur Frage "Welches Ereignis markierte den Beginn des Ersten Weltkriegs?" fehlt die Erwähnung des Attentats auf den österreichischen Thronfolger Franz Ferdinand.
- In der Antwort zur Frage "Welche berühmte Rede hielt Martin Luther King Jr. am 28. August 1963?" ist ein Fehler enthalten. Die richtige Antwort ist "I Have a Dream".
- In der Antwort zur Frage "Welcher europäische Entdecker wird oft mit der Entdeckung Amerikas in Verbindung gebracht?" ist ein Fehler enthalten. Die richtige Antwort ist Christoph Kolumbus.
- In der Antwort zur Frage "Welche Stadt wurde nach einem antiken Vulkan benannt, der im Jahr 79 n. Chr. ausbrach und die Stadt zerstörte?" ist ein Fehler enthalten. Die richtige Antwort ist Vesuv.
- In der Antwort zur Frage "Wer war der erste Präsident der Vereinigten Staaten? Welches Amt hatte er vor seiner Präsidentschaft inne?" ist ein Fehler enthalten. Die Antwort ist unvollständig.
- Es wurde kein Fehler in der Antwort zur Frage "Wann endete der Zweite Weltkrieg, welches spezifische Ereignis markiert das Ende des Krieges?" gefunden.

Gesamtergebnis: 
Note: 5+ 
```
>[!NOTE]
>Gefundene Fehler 5/4
> Formatierung ist ungewuenscht aber ok, es findet nahezu alle Fehler, bewertet 1x Falsch

#### Bewertung:

>[!IMPORTANT]
>Auf einer Skala von 0 bis 10, wobei 10 das Optimalbild der menschlichen Analyse darstellt, würde ich der KI-Analyse eine Punktzahl von 7/10 geben,es bietet immernoch raum fuer verbesserungen.

> [!NOTE]
> Verbesserungsvorschlaege:
> - Mehr Trainingsdaten, verbesserung von Fehlern in vorhandenen Datenn
> - Datenvariation
> - Einbau von Zitierten Fehlern, fuer besseres verstaendnis
> - Einbindung von Tabellen und anderen Textformen




## Modell v 1.2
Aenderungen:
- Mehr Variation der Trainingsdaten auch markdown Formatiert
- 2 Tests mit Tabellen
- Formatierun der Fehleranalyse vollstaendig
- Bessere Einbindung von Zitierungen
- KI kann auch auf andere Chatsachen zum Thema Test reagieren siehe [Chat](https://github.com/cheatoskar/TestGPT-Modell/blob/main/Readme/Openai-show1.png)

#### Gesehener Test Antwort:
```
Fehleranalyse:
	Aufgabe 1 (5 von 6 Punkte):
		- Falsche Angabe: Reformation ist eine Zäsur, kein Beispiel für eine Epoche (-1 Punkt)

	Aufgabe 2 (7 von 8 Punkte):
		- Fehlende Erwähnung der neuen Ideen im 18. Jahrhundert (z.B. Aufklärung, Rousseau) (-1 Punkt)

	Aufgabe 3 (6 von 7 Punkte):
		- Fehlende Begründung für "wie die Ideen der Staatsphilosophen modernen Staatsbildung begünstigten" (z.B. Bürgereinbindung, Gewaltenteilung, stärkere Rechte für das Volk) (-1 Punkt)

Insgesamt:
	Punkte: 18 von 21, das entspricht einer Leistung von: 86%
	Vorgeschlagene Note: 1-
```
### KI-Fehleranalyse (Vergleich) vorheriges Modell:

- Perekte Formatierung
- Klarere Aussagen, der Fehleranalyse
- Benuztung von Zitierten Fehlern
- genauere Punktevergabe, teils Punktgenau
- begruendet Fehler exakter, begruendet Fehlern anhand nicht gesehener Daten

- findet Fehler teils an anderer Stelle als mensch und andersherum
- makierte teils Sachen als fehler, uber welche man sich streiten koennte xd

- Noten Stimmen oefters mit den der Lehrern ueberein

Zusammengefasst: Findet Fehler oft nicht. Der Rest ist gut!
>[!WARNING]
>- Abweichung verrigert von teils Notengraden zu einzelnen Punkten, aber immernoch vorhanden

### Kurztest:
```
Fehleranalyse:
	- Frage 6: Die Antwort ist unvollständig, es fehlt das spezifische Ereignis, das das Ende des Krieges markiert. (-1 Punkt)

Insgesamt:
	Punkte: 5 von 6, das entspricht einer Leistung von: 83%
	Vorgeschlagene Note: 2+

###zweiter Versuch temperature = 0###

Fehleranalyse:
	Antwort 1 (Frage 1):
		- Fehlende Information: Die Antwort enthält nicht, dass der Erste Weltkrieg mit dem Kriegseintritt Österreich-Ungarns gegen Serbien begann. (-1 Punkt)

	Antwort 2 (Frage 2):
		- Falsche Information: Die Antwort enthält den falschen Titel der Rede. Die richtige Antwort wäre "I Have a Dream". (-1 Punkt)

	Antwort 3 (Frage 3):
		- Falsche Information: Die Antwort enthält den falschen Namen des Entdeckers. Die richtige Antwort wäre "Christoph Kolumbus". (-1 Punkt)

	Antwort 4 (Frage 4):
		- Falsche Information: Die Antwort enthält den falschen Namen des Vulkans. Die richtige Antwort wäre "Vesuv". (-1 Punkt)

	Antwort 5 (Frage 5):
		- Fehlende Information: Die Antwort enthält nicht, dass George Washington vor seiner Präsidentschaft General der Kontinentalarmee war. (-1 Punkt)

	Antwort 6 (Frage 6):
		- Kein Fehler

Insgesamt:
	Punkte: 4 von 6, das entspricht einer Leistung von: 67%
	Vorgeschlagene Note: 2 


```
>[!NOTE]
> gemsichte Antworten, je nach temperatur des Modells
> Um das zu beheben, sollten wir mehr Daten zu Einzelaufgaben haben, sowie das Prompt des Modells anpassen.

#### Bewertung:

>[!IMPORTANT]
>Auf einer Skala von 0 bis 10, wobei 10 das Optimalbild der menschlichen Analyse darstellt, würde ich der KI-Analyse eine Punktzahl von 8/10 geben,genauigkeit bietet Raum fuer verbesserungen!

> [!NOTE]
> Verbesserungsvorschlaege:
> - Mehr Trainingsdaten
> - Datenvariation, hinzufuegen von Einzelaufgaben, kurztests, Tabellen
> - Einbindung einer Musterloesung fuer exakte Analyse




