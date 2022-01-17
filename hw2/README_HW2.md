# Mankala

Mankala je souborné označení pro deskové hry pro dva hráče, jejichž společným znakem je přemisťování kuliček (kamínků, pecek, apod.) mezi důlky. V tomto domácím úkolu si naprogramujete jednoduchou variantu takové hry – pravidla jsou inspirována hrou Kalaha, resp. jednou z jejích obměn.  
  
Hrací deska sestává z dvou řad menších důlků (jejich počet bude parametrem hry, viz níže) a dvou větších důlků vlevo a vpravo. Vypadá tedy např. takto (počet menších důlků v každé řadě je zde šest):  
 
![image](https://user-images.githubusercontent.com/97029126/149747967-0d2c80b9-e152-48c8-9b9e-96f467d29500.png)
 
Hru hrají dva hráči, kteří sedí proti sobě. Každému hráči patří menší důlky na jeho straně a větší důlek vpravo – tento větší důlek nazýváme hráčovou bankou. Na začátku hry je v každém menším důlku předem určený počet kuliček (toto je druhý parametr hry), banky jsou prázdné. Hra probíhá po kolech, přičemž se hráči střídají. Průběh každého kola je následující:
  
Hráč si vybere jeden ze svých menších důlků, který obsahuje nějaké kuličky. Pokud jsou všechny důlky hráče prázdné, hra končí (viz níže).  
Hráč vezme všechny kuličky z vybraného důlku a začne je po jedné rozdělovat do následujících důlků proti směru hodinových ručiček, včetně svého banku, ale ne do banku soupeře. Pokud tedy např. spodní hráč vzal kuličky z důlku C, pak je bude postupně rozdělovat do důlků D, E, F, G, H, I, J, K, L, M, A, B, C, atd., dokud mu nějaké kuličky budou zbývat.  
Pokud při rozdělování padla poslední kulička do prázdného menšího důlku na straně aktuálního hráče a jeho oponent má v protějším důlku nějaké kuličky, sebere hráč svou poslední kuličku a všechny kuličky v protějším důlku a přesune je do své banky.  
Pokud při rozdělování padla poslední kulička do hráčovy banky, v dalším kole hraje tentýž hráč znovu; v opačném případě se hráči vystřídají.  
Hra končí, když má hráč, který je na tahu, všechny menší důlky prázdné. Jeho protivník si pak přesune všechny kuličky ze svých menších důlků do své banky. Vyhrává ten hráč, který má v bance více kuliček. Příklad průběhu hry je na konci této stránky.  
  
Hrací desku budeme reprezentovat pomocí dvou seznamů nezáporných celých čísel. Každý seznam reprezentuje důlky jednoho z hráčů (postupně zleva doprava z hráčova pohledu), přičemž počet kuliček v bance hráče je posledním prvkem seznamu. Desce naznačené výše tedy odpovídají seznamy [A, B, C, D, E, F, G] a [H, I, J, K, L, M, N].  
