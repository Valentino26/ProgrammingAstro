* Der __Prozessor__ holt sich __Instruktionen__ (und Daten) aus dem __RAM__ und arbeitet diese sequenziell ab. 
* Eine Menge an Instruktionen bilden ein __Programm__. 
* Das Programm muss irgendwoher kommen: __→__ aus dem __NVM__ 
* Im __NVM__ können viele Programme sein, das muss irgendwie organisiert sein. → Wir brauchen ein Betriebssystemprogramm, das alle Ressourcen managed. 
* Um das NVM zu managen, braucht es ein _Dateisystem_, d.h. Regeln, wie Programme und Daten im NVM gefunden werden. Zusammengehörende __Daten__ sind in einer Datei (=File) gespeichert. 
* Ein Betriebssystem (__OS__ = Operating System) hat noch viele weitere Aufgaben: User-Management, Multitasking, Peripherie … 
* __Unix__-artige Betriebssysteme gehen auf die späten 1960er Jahre zurück

## Human Interface

Um mit einem Computer arbeiten zu können, brauchen wir irgendeine Form von Schnittstelle: “Computer Terminal“ 
* __TTY (TeleTYpewriter)__ = an die ersten Computer wurden __Tastaturen__ von Telegraphen angeschlossen. Ausgabe: erst ein paar Lämpchen, später Papier. 
* die Ära der __“Glass TTYs“__, also __Tastatur + Bildschirm__ für Text Ein-und Ausgabe begann in den 1970ern 
* bald (1973) ging es auch in Richtung __graphischer Bedienung__ (mit Maus) → __GUI__, siehe Einheit “Grafik“ 
* die Bedienung per Text (__CLI__=Command Line Interface) ist bis heute geblieben:
	* Vielseitigkeit, Mächtigkeit, dennoch technisch anspruchslos → besonders gut für Fernzugriff

## Shell
„Shell“ wird für die äußere Schicht des Betriebssystems verwendet (innen Kernel, außen Shell), die für die Interaktion mit Menschen gedacht ist (HMI = Human-Machine Interface), also entweder CLI oder GUI. Das CLI ist ein “Programm“, welches User*innen-Eingaben interpretiert (d.h. prüft und ausführt)
* primärer Zweck: andere Programme ausführen ... `[usr@dune ~]$ firefox`… mit Argumenten! `[usr@dune ~]$ firefox www.univie.ac.at`
* die Shell hat eingebaute Schlüsselwörter und Variablen … … wie eine Programmiersprache 
* Shells können daher auch Skripte interpretieren (Programme in Interpretersprachen nennt man Skripte) 
* die verbreitetste Unix-Shell ist BASH

## Betriebssystem
… ein Programm, das die Abwicklung von anderen Programmen steuert und als Schnittstelle zwischen Benutzer*innen, Programmen und Hardware dient.

#### Mit folgenden Aufgaben:
* __Schnittstelle zwischen Mensch und Hardware__
	* Bedienschnittstelle (User Interface) zwischen Benutzer*innen und Programmen: dialogorientierte Konsole oder grafische Benutzeroberfläche 
* __Verwaltung von Ressourcen__
	* geordnete und kontrollierte Zuteilung von Prozessoren, Speichereinheiten und Peripheriegeräten (z.B. Maus) 
* __Programmierschnittstelle (API, Application Programming Interface)__
	* stellt die Infrastruktur für Programmabwicklung

## Wieso GNU/Linux?
Weil es portabel, open source, vergleichsweise sicher und hervorragend für Netzwerkanwendungen ist. 1991 von Linus Torvalds begonnen, wird Linux als Unix-artiger Kernel entwickelt. Ergänzt wird Linux um die GNU Software, seit 1983 eine Softwaresammlung von Anwendungen und Entwicklungswerkzeugen aus der Unix-Welt.
* __Portabilität__ = es funktioniert auf vielen verschiedenen Architekturen, vom Handy bis zum Supercomputer
* __Open Source__ = wir können den Quellcode (=Sourcecode) anschauen, verändern und so oft legal kopieren, wie wir wollen
* __Sicherheit__: es sollen viele Aufgaben von vielen Benutzer*innen gleichzeitig ausgeführt werden können, ohne dass diese sich gegenseitig stören
* __Netzwerk__: idealerweise merken wir keinen Unterschied, ob wir direkt neben dem Computer oder über’s Netz verbunden arbeiten

