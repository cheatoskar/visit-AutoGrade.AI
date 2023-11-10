>[!WARNING]
>Dieser Artikel ist gerade in arbeit und unvollstaendig

# Modellparameter und ihre Auswirkungen

## Die Modellparameter 
...sind entscheidend, um die gewünschten Antworten von unserem Modell zu erhalten. Hier sind einige der wichtigsten Parameter, die wir berücksichtigen:

**Prompt:** Der Ausgangspunkt jeder Modellanfrage. Das Prompt enthält die Informationen, die Sie dem Modell geben, um eine Antwort zu generieren.

**Rollenbestimmung:** Die Rolle definiert, welche Aufgabe oder Funktion ein Textausschnitt im Gespräch hat bzw. wie das Modell mit ihnen umgehen Soll.

**Maximale Token:** Dieser Parameter begrenzt die Anzahl der Tokens in der Modellantwort.

**Stop-Sequenzen:** Symbole oder Zeichen, die das Modell dazu veranlassen, die Antwort zu beenden.

**Temperatur:** Steuert die Zufälligkeit der Antworten. Eine höhere Temperatur führt zu zufälligeren Antworten, während eine niedrigere Temperatur zu konservativeren und vorhersehbareren Antworten führt.

**Top-P:** Dieser Parameter beeinflusst die Wahrscheinlichkeit, mit der das Modell die am häufigsten vorkommenden Tokens in der Antwort auswählt.

>[!IMPORTANT]
>Die fuer uns wichtigen Parameter sind: ```Rolle```,```Temperatur```,```Stop Sequenz```


## Auswirkungen der Parameter
>[!NOTE]
> Um die Auswirkung zu ueberpreufen, verwenden wir den selben Test (prompt) im OpenAI Playground, und schauen, inwiefern sich die Ausgabe des Modells aendert.
> Dadurch finden wir herraus, welche Parameter Einstellungen, die besten Ergebnisse an unserem Modell zeigen.
### Temperatur

| Temperatur | Auswirkung (Beschreibung) | Bewertung
| --- | --- | --- |
| 1 | Antworten ehr Kreativ, formatierung meist unterschiedlich. Teils werden Fehler nicht gefunden | OK
| 0.8 | Immernoch ehr kreativere antworten kein deutlicher unterschied zu temp: 1 zu erkennen. fehler werden Teils immernoch nicht gefunden. | OK
| 0.5 | Antworten haben meist die gewuenschte Formatierung, weniger abweichung. Modell findet mehr Fehler| Gut
| 0 | Antworten wie in Trainingsdaten vorgegeben, wenig Variation in der Formatierung. Das Modell findet die Meisten Fehler und liefert die logischsten Antworten | Sehr Gut



## Rolle des Modells
Die ursprüngliche Rolle lautet: "Du bist ein Geschichtslehrer, welcher Tests von Schülern kontrolliert, Fehler findet, und diese systematisch, formatiert darstellt."

## Fazit
Die Auswahl der Modellparameter ist entscheidend, um die gewünschten Antworten von unserem Modell zu erhalten.
Je nach Anwendungsfall und Zielsetzung können Sie die Parameter anpassen, um die Qualität und den Stil der Antworten zu steuern. Ein Verständnis dieser Parameter ermöglicht es Ihnen, das Modell effektiver zu nutzen und optimal auf Ihre Anforderungen abzustimmen.
