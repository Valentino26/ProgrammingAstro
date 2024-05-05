Die Grundidee des Algorithmus ist, jede Sequenz von identischen Symbolen durch deren Anzahl und ggf. das Symbol zu ersetzen. D. h., es werden nur die Stellen markiert, an denen sich das Symbol in der Nachricht ändert. Da die Längenangabe im Vergleich zur Länge der Sequenz nur [logarithmisch](https://de.wikipedia.org/wiki/Logarithmisch "Logarithmisch") wächst, spart man insbesondere bei langen Wiederholungssequenzen erheblich Speicherplatz. Umgekehrt ist die Einsparung umso geringer, je kürzer die Wiederholungen sind.

Die Lauflängenkodierung wird heutzutage als Vorkodierungsschritt (z. B. bei der [Bildkompression](https://de.wikipedia.org/wiki/Bildkompression "Bildkompression"), wie [JPEG](https://de.wikipedia.org/wiki/JPEG "JPEG")) verwendet, um sich im folgenden Kodierungsschritt Aufwand zu sparen. (Z. B. spart man sich bei der [Huffman-Kodierung](https://de.wikipedia.org/wiki/Huffman-Kodierung "Huffman-Kodierung") die Betrachtung längerer Symbole, da diese bereits zuvor reduziert wurden.)

**Beispiel:**

Statt einer Folge mit fünf Wiederholungen des Zeichens _0_ und dreimal _1_

`0000 0111`

speichert man lediglich

`5 3`

Das Startsymbol muss demnach bekannt sein oder zusätzlich kodiert werden.

Je länger eine einzelne Folge wird, umso größer ist die Einsparung, denn

- für 10 Wiederholungen benötigt man zwei Dezimalstellen,
- für 100 Wiederholungen benötigt man drei Dezimalstellen,
- für 1000 Wiederholungen benötigt man vier Dezimalstellen usw.