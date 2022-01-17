Vigenèrova šifra funguje podobně, ale klíčem je řetězec (slovo), nikoliv pouze jediné
číslo z rozsahu 0–26.  
Šifrujeme (i dešifrujeme) tak, že pod vstupní text si podepíšeme klíč,
který zopakujeme tolikrát, aby byl stejně dlouhý jako text. Každou takovou dvojici pak použijeme jako vstup pro Caesarovou šifru (písmeno
klíče udává posuv — A = 0, B = 1, …).  
Jako příklad zašifrujeme slovo „PYTHON“ klíčem „BCD“: klíč nejprve
prodloužíme opakováním na „BCDBCD“, poté spočítáme:  
• caesar('P', 1) = 'Q'  
• caesar('Y', 2) = 'A'  
• caesar('T', 3) = 'W'  
• caesar('H', 1) = 'I'  
• caesar('O', 2) = 'Q'  
• caesar('N', 3) = 'Q'  
  
Napište (čistou) funkci, která na vstupu dostane text k zašifrování a
klíč. Obojí budou řetězce libovolné délky, přičemž klíč je neprázdný
a tvořený pouze písmeny anglické abecedy a text písmeny anglické
abecedy a mezerami. Výstupem bude daný text zašifrovaný pomocí
daného klíče. Pro zjednodušení budeme vracet zašifrovaný text ve
velkých písmenech.
  
Dále napište (opět čistou) funkci, která na vstupu dostane zašifrovaný
text a odpovídající klíč (obojí ve stejném formátu, jako parametry předešlé funkce) a vrátí dešifrovaný text. Pro zjednodušení budeme dešifrovaný text opět vracet ve velkých písmenech.

