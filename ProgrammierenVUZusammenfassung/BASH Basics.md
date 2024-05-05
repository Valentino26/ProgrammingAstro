## Grundlegendes

![[Screenshot 2024-05-02 123119.png]]
## Standardbefehle
![[Screenshot 2024-05-02 123230.png]]
## Basics
man(ual)-Pages enthalten die Anleitungen von Kommandozeilenprogrammen
* Die eingegebene Befehlszeile wird durch whitespaces in Wörter aufgeteilt. Wenn das ein einfaches vorhandenes Kommando + optionale Argumente ergibt, wird die Befehlszeile ausgeführt.
* Wenn es keine eingebaute Funktion ist und kein Pfad angegeben ist, werden Kommandos im Suchpfad $PATH ausgeführt
* `[usr@blt ~]$ echo $PATH`
* Ausführen bedeutet: 
	* die Bash erzeugt eine separate Umgebung 
	* das Programm wird als eigenständiger Prozess gestartet 
	* die Bash “wartet“ im Hintergrund, bis das Programm beendet ist
	* `[usr@blt ~]$ set BASH=/usr/bin/bash`
* das gestartete Programm kann “POSIX-Signale“ empfangen → 
	* das wichtigste Signal ist das Abbruchsignal SIGINT: CTRL-C

## Filesystem-Hierarchie
![[Screenshot 2024-05-02 123611.png]]

## Filesystem-Tools
![[Screenshot 2024-05-02 123726.png]]![[Screenshot 2024-05-02 123747.png]]
## Zugriffsrechte
Wem gehört etwas und was dürfen die anderen damit machen?

In Unix-artigen Systemen gibt es eine*n Superuser*in (Administrator*in): root 
* mit __su__ können wir zu jemand anderem werden, auch zu root 
* mit __sudo__ führen wir einzelne Kommandos als root aus (sofern wir das dürfen)

Die Benutzer*innen gehören überdies noch einer oder mehreren Gruppen an, die ihnen weitere Rechte gewähren.
* z.B. wer zu “wheel“ gehört, darf sudo verwenden![[Screenshot 2024-05-02 124004.png]]![[Screenshot 2024-05-02 124018.png]]

## Ausgabe von Dateien
Mit < lässt sich die Standardeingabe umleiten. Mit > lässt sich die Standardausgabe und der Standardfehler umleiten.

- 1: Standard output (stdout)
- 2: Standard error (stderr)
- &: Beide
### Redirection
> >und >> repräsentieren beide output redirection in Linux. Beides sind stdout redirections, jedoch überschreibt > eine schon bestehende Datei oder eine neue Datei wird erstellt, vorrausgesetzt dass der dateiname noch nicht im Verzeichnis vorhanden ist. Das bedeutet, dass wenn man bestehendes aus einer Datei überschreiben will, dann sollte man > verwenden. Wohingegen >> zu einer bestehenden Datei appendet/hinzufügt oder eine neue Datei erstellt, vorrausgesetzt der Dateiname ist noch nicht in diesem Verzeichnis vorhanden.

## Ausfuehrungszeichen
![[Screenshot 2024-05-02 124311.png]]![[Screenshot 2024-05-02 124324.png]]![[Screenshot 2024-05-02 124340.png]]![[Screenshot 2024-05-02 124340 1.png]]![[Screenshot 2024-05-02 124403.png]]![[Screenshot 2024-05-02 124418.png]]![[Screenshot 2024-05-02 124428.png]]![[Screenshot 2024-05-02 124447.png]]![[Screenshot 2024-05-02 124459.png]]![[Screenshot 2024-05-02 124511.png]]![[Screenshot 2024-05-02 124528.png]]![[Screenshot 2024-05-02 124538.png]]![[Screenshot 2024-05-02 124548.png]]![[Screenshot 2024-05-02 124608.png]]![[Screenshot 2024-05-02 124623.png]]