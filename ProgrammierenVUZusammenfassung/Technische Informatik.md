## Woraus besteht ein Computer?
![[Screenshot 2024-05-02 113909.png|300]]

* Binäre Digitaltechnik verwendet __“binary digits“__. Ein Bit hat entweder den Zustand 1 („true“) oder 0 („false“), die Basis im __Dualsystem__ ist 2. 
* __Operationen__ im Computer sind mit __Schaltungen__ bestehend aus __Dioden__, __Transistoren__ und __Widerständen__ realisiert = __logische Gatter__  
* Diese Operationen werden von einem Prozessorbaustein __(CPU)__ in Form von __Instruktionen__ (=Befehle) verarbeitet. Jede Instuktion besteht aus einer __Nummer__, die sie kennzeichnet __(“OpCode“)__ und typischerweise __1-2 Operanden__.
* __Instruktionen__ verwenden __Register__ für die Ein- und Ausgabe und es gibt __Instruktionen__ für den __Austausch__ zwischen __Registern__ und dem Speicher __(RAM)__. 
* Die Instruktionen selbst werden __sequenziell__ aus dem Speicher __gelesen__. Eine __Abfolge__ solcher __(Assembler-) Instruktionen__ ist schon ein__ Programm__. 
* Instruktionen, die eine CPU nicht hat, müssen aus den vorhandenen zusammengesetzt werden. 
* Damit wir nicht in __Assembler__ programmieren müssen, werden “höhere“ Sprachen in Assembler übersetzt __(=kompiliert)__.![[Screenshot 2024-05-02 114422.png|400]]
## Beispiel fuer ARM Assembler![[Screenshot 2024-05-02 114827.png]]
## Zahlendarstellung
* Ein Bit hat entweder den Zustand 1 („true“) oder 0 („false“). 
* mehrere Bits stellen eine binäre Zahl dar: z.B.: 1101 = 1*23+1*22+0*21+1*20 = 13 
* eine Gruppe von 8 Bits nennt man 1 Byte, 16 bits = halfword, 32 bits = word 
* Präfixe (SI bzw. IEC International Electrotechnical Commission): 1kB „Kilobyte“ = 1000 Bytes, 1 KiB „Kibibyte“ = 1024 (210) Bytes 1MB „Megabyte“ = 106 Bytes, 1 MiB „Mebibyte“ = 220 Bytes …
* Oft werden Zahlen im Hexadezimalsystem (Basis=16) angegeben. 
	* Zähler: 0 1 2 3 4 5 6 7 8 9 A B C D E F 
	* erkennbar am vorangestellten 0x z.B.: 0x8 = 8, 0xF = 15, 0x10 = 16, 0x18 = 24, 0xABAD1DEA = 2880249322

## Speicher
Man unterschiedet zwischen __volatilen Speicher__ __(Strom weg -> Daten weg)__ und __nonvolatilem Speicher (die Daten bleiben ohne Strom erhalten)__
### RAM (Random Access Memory) - der Arbeitsspeicher
* whalfreier Zugriff moeglich, d.h. jede beliebige Speicherstelle kann jederzeit angefordert werden
* im PC als volatiles SDRAM realisiert (als winzige Kondensatoren)
### SSD
* FLASH-basierter nonvolatiler Speicher
* Basiert auf Feldeffekt-Transistoren (FET)
* Zugriff in Bloecken
* begrenzte Lebensdauer, weil der Loeschvorgagn Schaeden hinterlaesst

## Kernel
![[Screenshot 2024-05-02 115630.png|500]]
### Aufgaben des Kernels:
* Abstraktion von __Devices__
* Behandeln von __Interrupts__
* Ausfuehren von __Prozessen__
* __Speicherverwaltung__
* __Filesystem__-Verwaltung
* __Netzwerk__-Verwaltung
* Verwaltung der Zugriffsrechte
