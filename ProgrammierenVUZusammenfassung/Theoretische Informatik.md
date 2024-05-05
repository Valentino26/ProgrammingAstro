## Was ist Information?
* Information ist Wissen, das von A nach B uebertragen wird
### Was sind Daten?
* Daten sind mit Symbolen (Codewoerter) gespeicherte Information
### Was ist Shannon-Entropie?

**Entropie** ist in der Informationstheorie:
* einfach gesagt: die durchschnittliche Anzahl von Entscheidungen (bits), die benoetigt werden, um ein Zeichen aus einer Zeichenmenge zu identifizieren oder zu isolieren
* abders gesagt: ein Mass, welches fuer eine Nachrichtenquelle den mittleren Informationsgehalt ausgegebener Nachrichten angibt
__Claude  Shannon__ definierte dei Entropie __H__ einer diskreten, gedaechtnislosen Quelle (diskreten Zufallsvariable) __X__ ueber einem endlichen, aus Zeichen bestehenden Alphabet $Z = \{ z_1,z_2,...,z_n \}$ wie folgt: Zunaechst ordnet man jeder Wahrscheinlichkeit __p__ eines Ereignisses seinen Informationsgehalt $I(z) = -log_2 (p_z)$ zu. Dann ist die Entropie eines Zeichens definiert als der Erwartungswert des Informationsgehalts
$$H_1 = E[I] = -\sum_{z \in Z}p_z log_2(p_z)$$
```python
def shannon_entropy_1(text):
	char_dict = {}

	for char in text:
		char_dict.update({char:text.count(char)})
		text.replace(char,'')

	total_chars = len(text)
	entropy = 0.0

	for char, count in char_dict.items():
		p = count / total_chars
		entropy -= p*np.log2(p)
	return entropy
```
## Was ist ein Algorithmus?
Ein Algorithmus ist eine eindeutige Handlungsvorschrift zur Loesung eines Problems oder einer Klasse von Problemen. Algorithmen bestehen aus endlich vielen, wohldefinierten Einzelschritten. Damit koennen sie zur Ausfuehrung in ein Computerprogramm implementiert, aber auch in menschlicher Sprache formuliert werden. Bei der Problemloesung wird eine bestimmte Eingabe in eine bestimmte Ausgabe ueberfuehrt.

### Formale Definition
Mit Hilfe des Begriffs der Turingmaschine kann folgende formale Definition des Begriffs formuliert werden: Eine Berechnungsvorschrift zur Loesung eines Problems heisst genau dann Algorithmus, wenn eine zu dieser Berechnungsvorschrift aequivalente Turngmaschine existiert, die fuer jede Eingabe, die eine Loesung besitzt, stoppt.

### Eigenschaften des Algorithmus
1. Das Verfahren muss in einem endlichen Text eindeutig beschreibbar sein (Finitheit)
2. Jeder Schritt des Verfahrens muss tatsaechlich ausfuehrbar sein (Ausfuehrbarkeit)
3. Das Verfahren darf zu jedem Zeitpunkt nur endlich viel Speicherplatz benoetigen (Dynamische Finitheit, Platzkomplexitaet)
4. Das Verfahren darf nur endlich viele Schritte benoetigen (Terminierung, Zeitkomplexitaet)

### Finite-state machine
Ein endlicher __Automat/Zustandsautomat__ ist ein Modell eines Verhaltens, bestehend aus __Zustaenden__, __Zustandsuebergaengen__ und Aktionen. 
Ein __Zustand__ kann Information ueber die Vergangenheit beinhalten, da das System ihn ja auf dessen bisherigem Weg erreicht hat.
Ein __Zustandsuebergang__ ist ein Uebergang aus dem aktuellen Zustand in einen neuen Zustand. Zu diesem Uebergang kommt es, wenn die angegebenen logischen Bedingungen vorliegen, die erfuellt sein muessen, um den Uebergang zu ermoeglichen.

# Komplexitaet
Komplexitaet bezeichnet den Ressourcenverbrach von Algorithmen, den Informationsgehalt von Daten und bewertet damit Software oder Softwareteile hinsichtlich der Anzahl von Interaktionen

