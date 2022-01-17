# Predikát, který ověří, zda je číslo korektní číslo
# platební karty.  Číslo platební karty ověříte podle Luhnova
# algoritmu:
#
#  1. zdvojnásobte hodnotu každé druhé cifry zprava; je-li výsledek
#     větší než 9, odečtěte od něj hodnotu 9,
#  2. sečtěte všechna takto získaná čísla a cifry na lichých
#     pozicích (kromě první cifry zprava, která slouží jako
#     kontrolní součet),
#  3. je-li potřeba přičíst přesně hodnotu kontrolní cifry, aby
#     byl součet dělitelný 10, je číslo platné.


def count_digits(number):
    count = 0
    while number > 0:
        count += 1
        number = number // 10
    return count


def get_digit(number, k):
    return (number // 10 ** k) % 10


def is_valid_card(number):
    sumarization = 0
    for i in range(1, count_digits(number)):
        digit = get_digit(number, i)
        if not(i % 2 == 0):
            if (digit * 2 > 9):
                sumarization += digit * 2 - 9
            else:
                sumarization += digit * 2
        else:
            sumarization += digit
    sumarization += get_digit(number, 0)
    return (sumarization % 10 == 0)


def main():
    assert is_valid_card(28316)
    assert is_valid_card(4556737586899855)
    assert is_valid_card(4929599116478604)
    assert is_valid_card(4929300836739668)
    assert not is_valid_card(4929300835539668)
    assert not is_valid_card(4929300836739328)
    assert not is_valid_card(5101180000000000007)

    assert is_valid_card(5294967072531977)
    assert is_valid_card(5354598557505686)
    assert is_valid_card(2720993849498580)


if __name__ == "__main__":
    main()