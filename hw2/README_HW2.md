# Mankala

Mankala je souborné označení pro deskové hry pro dva hráče, jejichž společným znakem je přemisťování kuliček (kamínků, pecek, apod.) mezi důlky. V tomto domácím úkolu si naprogramujete jednoduchou variantu takové hry – pravidla jsou inspirována hrou Kalaha, resp. jednou z jejích obměn.

Hrací deska sestává z dvou řad menších důlků (jejich počet bude parametrem hry, viz níže) a dvou větších důlků vlevo a vpravo. Vypadá tedy např. takto (počet menších důlků v každé řadě je zde šest):

╭───────╮╭───╮╭───╮╭───╮╭───╮╭───╮╭───╮╭───────╮
│       ││ M ││ L ││ K ││ J ││ I ││ H ││       │
│   N   │╰───╯╰───╯╰───╯╰───╯╰───╯╰───╯│       │
│       │╭───╮╭───╮╭───╮╭───╮╭───╮╭───╮│   G   │
│       ││ A ││ B ││ C ││ D ││ E ││ F ││       │
╰───────╯╰───╯╰───╯╰───╯╰───╯╰───╯╰───╯╰───────╯
Hru hrají dva hráči, kteří sedí proti sobě. Každému hráči patří menší důlky na jeho straně a větší důlek vpravo – tento větší důlek nazýváme hráčovou bankou. Na začátku hry je v každém menším důlku předem určený počet kuliček (toto je druhý parametr hry), banky jsou prázdné. Hra probíhá po kolech, přičemž se hráči střídají. Průběh každého kola je následující:

Hráč si vybere jeden ze svých menších důlků, který obsahuje nějaké kuličky. Pokud jsou všechny důlky hráče prázdné, hra končí (viz níže).
Hráč vezme všechny kuličky z vybraného důlku a začne je po jedné rozdělovat do následujících důlků proti směru hodinových ručiček, včetně svého banku, ale ne do banku soupeře. Pokud tedy např. spodní hráč vzal kuličky z důlku C, pak je bude postupně rozdělovat do důlků D, E, F, G, H, I, J, K, L, M, A, B, C, atd., dokud mu nějaké kuličky budou zbývat.
Pokud při rozdělování padla poslední kulička do prázdného menšího důlku na straně aktuálního hráče a jeho oponent má v protějším důlku nějaké kuličky, sebere hráč svou poslední kuličku a všechny kuličky v protějším důlku a přesune je do své banky.
Pokud při rozdělování padla poslední kulička do hráčovy banky, v dalším kole hraje tentýž hráč znovu; v opačném případě se hráči vystřídají.
Hra končí, když má hráč, který je na tahu, všechny menší důlky prázdné. Jeho protivník si pak přesune všechny kuličky ze svých menších důlků do své banky. Vyhrává ten hráč, který má v bance více kuliček. Příklad průběhu hry je na konci této stránky.

Hrací desku budeme reprezentovat pomocí dvou seznamů nezáporných celých čísel. Každý seznam reprezentuje důlky jednoho z hráčů (postupně zleva doprava z hráčova pohledu), přičemž počet kuliček v bance hráče je posledním prvkem seznamu. Desce naznačené výše tedy odpovídají seznamy [A, B, C, D, E, F, G] a [H, I, J, K, L, M, N].

Abyste si hru mohli vyzkoušet (poté, co vyřešíte níže uvedené úlohy), je vám k dispozici soubor hw2_game.py, který vložte do stejného adresáře, jako je soubor s vaším řešením, případně jej upravte dle komentářů na jeho začátku a spusťte. Kliknutím na jeden z důlků se provede tah, kliknutí na tlačítko Random vybere náhodný neprázdný důlek hráče, klávesa R hru resetuje a Q ukončí. Program nijak nekontroluje konec hry ani střídání tahů hráčů.