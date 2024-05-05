Der Datentyp beschreibt, um welche Art Daten es sich handelt bzw. woraus der Datensatz zusammengesetzt ist und welche Operationen darauf erlaubt sind. Wir unterschieden:

- Elementare Datentypen sind diskret und begrenzt. Bsp.: Integer, Char;
- Auch floats sind im computer diskret d.h. nur endlich genau! Pointer, d.h. Adressen auf die Daten im RAM, die als Refernezen fungieren bzw. einen indirekten Zugriff erlauben Zusammengesetzte Datentypen (z.B.: Strings, Strukturen)

## Echte Datentypen
"Echte" Datentypen sind, was Prozessor/FPU wirklich verwenden (Floating Point UNit, eine Recheneinheit nur für floats)

Der Prozessor/die FPU hat Instruktionen und Register für:

- Integer in (8), (16), (32), (64) bit, signed (d.h. mit Vorzeichen bzw. auch negativ) und unsigned, sind eine Teilmenge von 𝑍
- IEEE-754 Floats in single (32 bit) und double precision (64 bit) zur Darstellung von Gleitkommazahlen

alle anderen Datentypen sind von der SW erzeugt. z.B.: Booleans gibt es eigentlich so nichtm weil sie immer in 8 bzw. 32 Bit gespeichert werden. Generell gilt False=0 und True $\neq 0$ 
![[Screenshot 2024-05-02 125027.png]]![[Screenshot 2024-05-02 125054.png]]

## Typenwandlung / Casting

* __implizit__ = vom Compiler/Interpreter durchgeführt z.B. float a = 3.14 * 5; 
* __explizit__ = vom Programm vorgeschrieben z.B.: int a = (int) 3.99; /* ergibt 3 * / 
* Wir unterscheiden: 
	- Typerweiterung (type promotion)
	- Typeinschränkung (type demotion) 
	- Achtung: ein double precision float hat typ. 17 signifikante Stellen:![[Screenshot 2024-05-02 125301.png|200]]
## Under- and Overflow
Overflow errors come up when working with integers and floating points, and underflow errors are generally just associated with floating points.
### Overflow
Lets assume we have an integer stored in 1 byte. The greatest number we can store in one byte is 255, so let’s take that. This is 11111111. Now, suppose we add 2 to it to get 00000010. The result is 257, which is 100000001. The result has 9 bits, whereas the integers we are working with consist of only 8. What does a computer then do in this scenario? A computer will discard the most-significant bit (MSB) and keep the rest.

```C++
#include using namespace std;

int main() { // Define a variable to store the value (1 byte) unsigned char value = 255; // Maximum value for 1 byte
// Add 2 to the value
value = value + 1;

// Print the result
cout << "The result after adding 2: " << static_cast<int>(value) << endl;

return 0;
}
```
### Underflow
Underflow is a bit trickier to understand because it has to do with precision in floating points. Again, due to the discrete nature of storage in computers, we cannot store an arbitrarily small number either. The floating-point convention comes up with techniques to represent fractional numbers. When we use these in calculations that result in a smaller number than our least value, we again exceed our designated space. Without going into details of floating-point representation, we can see how this problem would manifest by considering a decimal example. 
__Example__: Suppose we are given designated boxes to write decimal numbers in. We have one box on the left of the decimal point and three boxes on the right. So, we can easily represent 0.004. Now, we want to perform a calculation, 0.004×0.004. The answer to this is 0.000016, but we simply do not have this many places available to us. So we discard the least-significant bits and store 0.000, which is quite obviously an erroneous answer.
```C++
#include using namespace std;

int main() { // Define a variable to store the value (1 byte) unsigned char value = 0; // Minimum value for 1 byte
// Subtract 2 from the value (underflow)
value = value - 1;

// Print the result
cout << "The result after subtracting 2: " << static_cast<int>(value) << endl;

return 0;
}
```
![[Screenshot 2024-05-02 125622.png]] 

## IEEE-754 Gleitkommazahlendarstellung
IEEE-754 schreibt die Formate für single und double precision vor. Eine Gleitkommazahl berechnet sich aus: 
* Vorzeichen s (in 1 bit) -Mantisse m(in p=23 bzw. 52 bit)(=Nachkommatiel 1,m) 
* Exponent (Charackteristik)e(in 8 bzw. 11.bit) 
* Basis b (=2) und Bias B(=127 bzw 1023)

		$$X = (-1)^s \cdot (1 + \frac{m}{2^p})\cdot b^{e-B}$$
![[Screenshot 2024-05-02 125922.png||200]]
Achtung: float ist in: -C single -Python double

## Strings
Sind __Arrays__ von __Charactern__
* __Array__ = sequenzielle Abfolge von Elementen desselben Datentyps 
* __Character__ = Zeichen aus einer __Symboltabelle__, das durch seinen __Index__ als __unsigned integer__ (__8__,16,32 bit) gegeben ist 
* z.B. ACII (7 bzw. 8 bit)![[Screenshot 2024-05-02 130206.png]]