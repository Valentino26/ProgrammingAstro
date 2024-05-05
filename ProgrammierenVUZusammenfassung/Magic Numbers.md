![[Screenshot 2024-05-05 181009.png]]
* Urspruenglich aus der Unix-Welt kommend, ist ein spezieller Wert, der ein bestimmtes Dateiformat am Dateibeginn kennzeichnet (wie ihn zum Beispiel der Unix-Befehl file auswertet)
* Ein auffaelliger Wert, um ein Register oder einen Speicherbereich zu markieren, der spaeter mittels eines Debuggers auf Fehler untersucht werden soll. Solche makrierende Magische Zahlen werden meistens aus folgenden Domaenen ausgewaehlt
	* ACII
	* Hexadezimale
	* Hexspeak
* Ein im Quellcode eines Programms auftauchender Zahlenwert (hard coded value), dessen Bedeutung sich nicht unmittelbar erkennen laesst - seine Bedeutung ist somit magisch. Derartige Magische Zahlen sind zu vermeiden und durch gut benannte Konstantendefinitionen zu ersetzten, deren Namen, Bedeutung und Herkunft klar angegeben ist

# Magische Zahlen zur Kennzeichnung von Dateitypen

Eine fruehe Konvention in unixartigen Betirebssystemen war, dass Binaries mit zwei Bytes anfingen (Magic Bytes), die eine Magische Zahl enthielten, die den Type der Datei angibt. Am Anfang wurden damit Objektdateien fuer verschiedene Plattformen gekennzeichnet. Nach und nach wurde dieses Konzept auch auf andere Dateien uebertragen, und mittlerweile findet sich in fast jeder Binaerdatei eine magische Zahl.

Viele andere Typenn von Dateien haben einen Inhalt, der den Dateityp identifiziert. So faengt XML mit der speziellen Zeichenfolge `<?xml` an, die die Datei als XML kennzeichnet. Wandelt man diesen Dateianfang in eine Zahl um, kann man anhand eines einfachen Vergleichens schnell den Dateityp bestimmen, ohne viel ueber das Format wissen zu muessen.

Einige Beispiele:
* Die Stelle mit wichtigen Netzwerkparametern des BOOTP/DHCP-Protokolls beginnt mit einem hexadezimalen Magic Cookie 0x6382536
* [kompilierte](https://de.wikipedia.org/wiki/Compiler "Compiler") [Java](https://de.wikipedia.org/wiki/Java_(Programmiersprache) "Java (Programmiersprache)")-Klassendateien ([Bytecode](https://de.wikipedia.org/wiki/Bytecode "Bytecode")) beginnen mit `0xCAFEBABE`.
* [GIF](https://de.wikipedia.org/wiki/Graphics_Interchange_Format "Graphics Interchange Format")-Dateien enthalten am Anfang den [ASCII](https://de.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange "American Standard Code for Information Interchange")-Code für ‚`GIF89a`‘ (`0x474946383961`) oder ‚`GIF87a`‘ (`0x474946383761`)
- [JPEG](https://de.wikipedia.org/wiki/JPEG "JPEG")/[JFIF](https://de.wikipedia.org/wiki/JPEG_File_Interchange_Format "JPEG File Interchange Format")-Dateien fangen mit `0xFFD8FF` an und enthalten weiterhin die ASCII-Entsprechung für ‚`JFIF`‘ (`0x4A464946`).
- [PNG](https://de.wikipedia.org/wiki/Portable_Network_Graphics "Portable Network Graphics")-Dateien beginnen mit einem 8-Byte-MagicByte, welches die Datei als PNG identifiziert und eine Erkennung von Dateiübertragungsproblemen ermöglicht: `\211 P N G \r \n \032 \n` (`0x89504e470d0a1a0a`)
- Standard-[MIDI](https://de.wikipedia.org/wiki/Musical_Instrument_Digital_Interface "Musical Instrument Digital Interface")-Dateien enthalten die ASCII-Zeichenfolge ‚`MThd`‘ (`0x4D546864`) gefolgt von Metadaten.
- [Unix](https://de.wikipedia.org/wiki/Unix "Unix")-[Scripte](https://de.wikipedia.org/wiki/Skriptsprache "Skriptsprache") aller Art starten normalerweise mit einem [Shebang](https://de.wikipedia.org/wiki/Shebang "Shebang"), ‚`#!`‘ (`0x23` `0x21`), gefolgt von einem Pfad zum Interpreter (z. B. ,`#!/usr/bin/perl`‘ für [Perl](https://de.wikipedia.org/wiki/Perl_(Programmiersprache) "Perl (Programmiersprache)"))
- [EXE](https://de.wikipedia.org/wiki/EXE "EXE")-Dateien für [MS-DOS](https://de.wikipedia.org/wiki/MS-DOS "MS-DOS") sowie [Microsoft-Windows](https://de.wikipedia.org/wiki/Microsoft_Windows "Microsoft Windows")-EXE und -[DLLs](https://de.wikipedia.org/wiki/Dynamic_Link_Library "Dynamic Link Library") starten mit den ASCII-Zeichen ‚`MZ`‘ (`0x4D5A`) oder auch selten ‚`ZM`‘ (`0x5A4D`), den Initialen des Erfinders dieses Formats, [Mark Zbikowski](https://de.wikipedia.org/wiki/Mark_Zbikowski "Mark Zbikowski"), siehe [MZ-Datei](https://de.wikipedia.org/wiki/MZ-Datei "MZ-Datei").
- Der [Berkeley-Fast-File-System](https://de.wikipedia.org/wiki/Unix_File_System "Unix File System")-[Superblock](https://de.wikipedia.org/wiki/Superblock "Superblock") wird identifiziert durch `0x19540119` oder `0x011954` je nach Version; beides ist das Geburtsdatum des Designers [Marshall Kirk McKusick](https://de.wikipedia.org/wiki/Marshall_Kirk_McKusick "Marshall Kirk McKusick").
- Programme für den [Game Boy](https://de.wikipedia.org/wiki/Game_Boy "Game Boy") und [Game Boy Advance](https://de.wikipedia.org/wiki/Game_Boy_Advance "Game Boy Advance") haben eine 48 oder 156 Byte lange magische Zahl. Diese Zahl kodiert ein [Bitmap](https://de.wikipedia.org/wiki/Rastergrafik "Rastergrafik") des [Nintendo](https://de.wikipedia.org/wiki/Nintendo "Nintendo")-Logos.
- Alte [Fat Binaries](https://de.wikipedia.org/wiki/Fat_Binary "Fat Binary") (die Code für sowohl den [68K-](https://de.wikipedia.org/wiki/Motorola_68000 "Motorola 68000") als auch den [PowerPC](https://de.wikipedia.org/wiki/PowerPC "PowerPC")-Prozessor enthalten) auf [Mac OS 9](https://de.wikipedia.org/wiki/Mac_OS_9 "Mac OS 9") beginnen mit der ASCII-Zeichenfolge von ‚`Joy!`‘ (englisch für _Freude!_; hexadezimal `0x4A6F7921`).
- [TIFF](https://de.wikipedia.org/wiki/Tagged_Image_File_Format "Tagged Image File Format")-Dateien fangen mit `II` oder `MM` an, abhängig von der [Endianness](https://de.wikipedia.org/wiki/Byte-Reihenfolge "Byte-Reihenfolge") („II“ entspricht Intel und „MM“ Motorola), gefolgt von `0x2A00` oder `0x002A` (im [Dezimalsystem](https://de.wikipedia.org/wiki/Dezimalsystem "Dezimalsystem") [42](https://de.wikipedia.org/wiki/42_(Antwort) "42 (Antwort)")).
- [ZIP](https://de.wikipedia.org/wiki/ZIP-Dateiformat "ZIP-Dateiformat")-Dateien beginnen mit `PK`, den Initialen ihres Erfinders [Phil Katz](https://de.wikipedia.org/wiki/Phil_Katz "Phil Katz"). Das betrifft aber auch andere mit dem [Deflate](https://de.wikipedia.org/wiki/Deflate "Deflate")-Algorithmus komprimierte Dateien, wie z. B. die [Microsoft Office-Formate](https://de.wikipedia.org/wiki/Office_Open_XML "Office Open XML") DOCX, XLSX und PPTX.
Das Unix-Kommando `[file](https://de.wikipedia.org/wiki/File "File")` liest und interpretiert magische Zahlen aus Dateien. Auch das [Linux-Kernelmodul](https://de.wikipedia.org/wiki/Linux_(Kernel) "Linux (Kernel)") _[binfmt misc](https://de.wikipedia.org/wiki/Binfmt_misc "Binfmt misc")_ erkennt anhand magischer Zahlen den Dateityp einer Anwendung. Die eigentliche „Magie“ liegt in der Datei `/usr/share/misc/magic.mgc` (unter Debian `/usr/share/file/magic.mgc`).

# File Magic Numbers

Magic numbers are the first bits of a file which uniquely identify the type of file. This makes programming easier because complicated file structures need not be searched in order to identify the file type.

For example, a jpeg file starts with ffd8 ffe0 0010 4a46 4946 0001 0101 0047 ......JFIF.....G
ffd8 shows that it's a JPEG file, and ffe0 identify a JFIF type structure. There is an ascii encoding of "JFIF" which comes after a length code, but that is not necessary in order to identify the file. The first 4 bytes do that uniquely.

This gives an ongoing list of file-type magic numbers.

## Image Files

<table border=1>
<tr>
  <th>File type</th>  <th>Typical <br>extension</th>  
  <th>Hex digits<br>xx = variable</th>
  <th>Ascii digits<br>. = not an ascii char</th>
</tr>

<tr>
  <td>Bitmap format</td>
  <td>.bmp</td>
  <td>42 4d</td>
  <td>BM</td>
</tr>

<tr>
  <td>FITS format</td>
  <td>.fits</td>
  <td>53 49 4d 50 4c 45</td>
  <td>SIMPLE</td>
</tr>

<tr>
  <td>GIF format</td>
  <td>.gif</td>
  <td>47 49 46 38</td>
  <td>GIF8</td>
<tr>

<tr>
  <td>Graphics Kernel System</td>
  <td>.gks</td>
  <td>47 4b 53 4d</td>
  <td>GKSM</td>
</tr>

<tr>
  <td>IRIS rgb format</td>
  <td>.rgb</td>
  <td>01 da</td>
  <td>..</td>
</tr>

<tr>
  <td>ITC (CMU WM) format</td>
  <td>.itc</td>
  <td>f1 00 40 bb</td>
  <td>....</td>
</tr>

<tr>
  <td>JPEG File Interchange Format</td>
  <td>.jpg</td>
  <td>ff d8 ff e0</td>
  <td>....</td>
</tr>

<tr>
  <td>NIFF (Navy TIFF)</td>
  <td>.nif</td>
  <td>49 49 4e 31</td>
  <td>IIN1</td>
</tr>

<tr>
  <td>PM format</td>
  <td>.pm</td>
  <td>56 49 45 57</td>
  <td>VIEW</td>
</tr>

<tr>
  <td>PNG format</td>
  <td>.png</td>
  <td>89 50 4e 47</td>
  <td>.PNG</td>
</tr>

<tr>
  <td>Postscript format</td>
  <td>.[e]ps</td>
  <td>25 21</td>
  <td>%!</td>
</tr>

<tr>
  <td>Sun Rasterfile</td>
  <td>.ras</td>
  <td>59 a6 6a 95</td>
  <td>Y.j.</td>
</tr>

<tr>
  <td>Targa format</td>
  <td>.tga</td>
  <td>xx xx xx</td>
  <td>...</td>
</tr>

<tr>
  <td>TIFF format (Motorola - big endian) </td>
  <td>.tif</td>
  <td>4d 4d 00 2a</td>
  <td>MM.*</td>
</tr>

<tr>
  <td>TIFF format (Intel - little endian) </td>
  <td>.tif</td>
  <td>49 49 2a 00</td>
  <td>II*.</td>
</tr>

<tr>
  <td>X11 Bitmap format</td>
  <td>.xbm</td>
  <td>xx xx</td>
  <td></td>
</tr>

<tr>
  <td>XCF Gimp file structure</td>
  <td>.xcf</td>
  <td>67 69 6d 70 20 78 63 66 20 76</td>
  <td>gimp xcf</td>
</tr>

<tr>
  <td>Xfig format</td>
  <td>.fig</td>
  <td>23 46 49 47</td>
  <td>#FIG</td>
</tr>

<tr>
  <td>XPM format</td>
  <td>.xpm</td>
  <td>2f 2a 20 58 50 4d 20 2a 2f</td>
  <td>/* XPM */</td>
</tr>

</table>

## Compressed files

<table border=1>
<tr>
  <th>File type</th>  <th>Typical <br>extension</th>  
  <th>Hex digits<br>xx = variable</th>
  <th>Ascii digits<br>. = not an ascii char</th>
</tr>

<tr>
  <td>Bzip</td>
  <td>.bz</td>
  <td>42 5a</td>
  <td>BZ</td>
</tr>

<tr>
  <td>Compress</td>
  <td>.Z</td>
  <td>1f 9d</td>
  <td>..</td>
</tr>

<tr>
  <td>gzip format</td>
  <td>.gz</td>
  <td>1f 8b</td>
  <td>..</td>
</tr>

<tr>
  <td>pkzip format</td>
  <td>.zip</td>
  <td>50 4b 03 04</td>
  <td>PK..</td>
</tr>

</table>

## Archive files

<table border=1>
<tr>
  <th>File type</th>  <th>Typical <br>extension</th>  
  <th>Hex digits<br>xx = variable</th>
  <th>Ascii digits<br>. = not an ascii char</th>
</tr>

<tr>
  <td>TAR (pre-POSIX)</td>
  <td>.tar</td>
  <td>xx xx</td>
  <td>(a filename)</td>
</tr>

<tr>
  <td>TAR (POSIX)</td>
  <td>.tar</td>
  <td>75 73 74 61 72</td>
  <td>ustar (offset by 257 bytes)</td>
</tr>

</table>

## Excecutable files

<table border=1>
<tr>
  <th>File type</th>  <th>Typical <br>extension</th>  
  <th>Hex digits<br>xx = variable</th>
  <th>Ascii digits<br>. = not an ascii char</th>
</tr>

<tr>
  <td>MS-DOS, OS/2 or MS Windows</td>
  <td>&nbsp;</td>
  <td>4d 5a</td>
  <td>MZ</td>
</tr>

<tr>
  <td>Unix elf</td>
  <td>&nbsp;</td>
  <td>7f 45 4c 46</td>
  <td>.ELF</td>
</tr>
</table>

##Miscellaneous files

<table border=1>
<tr>
  <th>File type</th>  <th>Typical <br>extension</th>  
  <th>Hex digits<br>xx = variable</th>
  <th>Ascii digits<br>. = not an ascii char</th>
</tr>

<tr>
  <td>pgp public ring</td>
  <td>&nbsp;</td>
  <td>99 00</td>
  <td>..</td>
</tr>

<tr>
  <td>pgp security ring</td>
  <td>&nbsp;</td>
  <td>95 01</td>
  <td>..</td>
</tr>

<tr>
  <td>pgp security ring</td>
  <td>&nbsp;</td>
  <td>95 00</td>
  <td>..</td>
</tr>

<tr>
  <td>pgp encrypted data</td>
  <td>&nbsp;</td>
  <td>a6 00</td>
  <td>&#166;.</td>
</tr>

</table>


