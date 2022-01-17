# Funkci, která vytvoří číslo zřetězením po sobě
# jdoucích kladných čísel počínaje zadaným číslem.  Tato
# čísla zřetězte vyjádřená v binární soustavě. Například volání
# ‹joined(1, 3)› zřetězí sekvenci ⟦1₂ = 1⟧, ⟦(10)₂ = 2⟧ a ⟦(11)₂ =
# 3⟧ vrátí číslo ⟦(11011)₂ = 27⟧.

def digit_count(number):
    count = 0
    while number > 0:
        count += 1
        number = number // 10
    return count


def decimal_binary(number):
    binary = 0
    exponent = 0
    while (number // (2 ** exponent) > 0):
        exponent += 1
    for i in range(exponent, -1, -1):
        binary += number // (2 ** i)
        number -= (binary % 10) * (2 ** i)
        binary *= 10
    return binary // 10


def joined(start, count):
    number = 0
    for i in range(count):
        binary = decimal_binary(start)
        digit = digit_count(binary)
        number *= 10 ** digit
        number += binary
        start += 1
    return int(str(number), 2)


def main():
    assert joined(1, 3) == 0b11011
    assert joined(10, 4) == 0b1010101111001101
    assert joined(8, 5) == 0b10001001101010111100
    assert joined(99, 2) == 0b11000111100100
    assert joined(999, 3) == 0b111110011111111010001111101001
    assert joined(1111, 1) == 0b10001010111


if __name__ == "__main__":
    main()