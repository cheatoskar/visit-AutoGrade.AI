# Test-GPT
KI-Modell, was darauf trainiert wird, Tests zu bewerten/Analysieren. Insbesondere Geschichte!
> [!IMPORTANT]
> [**Funktionsweise Des Trainings**](./Readme/Funktionsweise-Code.md)
> 
> [**Fortschritt Dokumentiert, jeder Modelle:**](.\Readme\ModellTest.md)


### Update 1.0
> [!NOTE]
> basierend auf 12 Tests

> basierend auf 0 Aufgaben

### Update 1.1
> [!NOTE]
> basierend auf 18 Tests

> basierend auf 0 Aufgaben
- verbesserte/vereinfachte Fehleranalyse -> besseres leanring
- Fehlerbehebung in Trainingsdaten

## Update 1.2 out 29.10.23
> [!NOTE]
> basierend auf 20 Tests

> basierend auf 0 Aufgaben


> [!IMPORTANT]
> Verbesserungen:
- verbesserte Einbindung von Zitaten, welche nun makiert werden (Website GUI)
- Erste Formatierung basierend auf Markdown
- Formatierte Tests als Trainingsdaten fuer mehr variabelitaet
- Einbindung von CSV formatierten tabellen als Trainingsdaten.
> [!NOTE]
> Trainingsdaten wurden eingebunden formatierung funktioniert!.




Beispiel:
<img src=".\Readme\Openai-show2.png">

- Testanalyse mithilfe eines weiterfuehrenden Chatbots, zur befragen von z.b. Fehlern: getestet, funktioniert!
<img src=".\Readme\Openai-show1.png">

> [!IMPORTANT]
> [Das Dokument, mit Modell Tests kann man sich hier anschauen, es zeigt Probleme, verbesserungen (auch in der Zukunft) und Beispiele jeder Modelle:](.\Readme\ModellTest.md)

> [!WARNING]
> Experimente der Parameter, folgen mit kommenden Versionen, um das Verhalten zu untersuchen!


### OpenAI Playground GPT-3-Parameter
#### model: 
Wählen Sie das gewünschte GPT-3-Modell aus. Verschiedene Modelle haben unterschiedliche Fähigkeiten und Größen.

#### temperature: 
Steuert die Zufälligkeit der Ausgabe. Niedrige Werte führen zu konservativeren Texten, während hohe Werte zu kreativeren Texten führen.

#### max_tokens: 
Begrenzen Sie die maximale Länge der generierten Texte.

#### top_p: 
Steuern Sie die Wahrscheinlichkeit von Wörtern in der Ausgabe. Niedrige Werte erzeugen konservativere Texte, während hohe Werte zu mehr Vielfalt führen.

#### frequency_penalty: 
Passen Sie die Verwendung von häufig vorkommenden Wörtern in der Ausgabe an.

#### presence_penalty: 
Passen Sie die Verwendung von selten vorkommenden Wörtern in der Ausgabe an.

stop_sequence: Definieren Sie eine benutzerdefinierte Sequenz, die als Endpunkt für die generierte Ausgabe dient.
