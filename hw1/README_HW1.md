# House function

Napište proceduru house(width, height, roof_angle), která nakreslí domeček (viz obrázky níže). Obdélníková část domečku má šířku width a výšku height (kladná reálná čísla), úhel špičky střechy je roof_angle stupňů (v rozsahu 1 až 179).

# Ntý prvek posloupnosti

Napište čistou funkci nth_element_lu(p, q, index), která vrátí index-tý prvek posloupnosti, která vzniká takto:
x0 = 0
x1 = 1
xn = p * xn − 1 − q * xn − 2
Parametry p, q mohou být libovolná celá čísla, parametr index libovolné nezáporné celé číslo (v tomto příkladu indexujeme posloupnost od nuly).

# Ntý unikátní nejmenší prvočíselný dělitel

Napište čistou funkci nth_unique_smallest_prime_divisor(num, index), která vrátí index-té unikátní nejmenší prvočíslo, které se vyskytuje v prvočíselném rozkladu čísla num. Pokud se v rozkladu vyskytuje některé prvočíslo vícekrát, počítáme jeho výskyt pouze jednou, tedy např. v čísle 2 ⋅ 2 ⋅ 3 ⋅ 3 ⋅ 3 ⋅ 5 = 540 je třetím unikátním nejmenším prvočíslem číslo 5. Pokud má num méně než index unikátních prvočísel v rozkladu, funkce vrátí None. Předpokládejte, že num i index jsou kladná celá čísla.