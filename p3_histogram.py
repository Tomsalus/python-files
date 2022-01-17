# Ze seznamu nezáporných čísel vrátí nový seznam obsahující dvojice – číslo a jeho četnost. 
# Výstupní seznam musí být seřazený vzestupně dle prvního prvku dvojice.

def histogram(data):
    lst_data = sorted(data)
    lst_unique_elements = []
    output = []

    for elem in lst_data:
        current_elem = elem
        count = 0

        if not(current_elem in lst_unique_elements):
            for element in lst_data:
                if element == current_elem:
                    count += 1

            output.append((current_elem, count))
            lst_unique_elements.append(current_elem)

    return (output)


def main():
    assert histogram([1, 2, 3, 2, 1]) == [(1, 2), (2, 2), (3, 1)]
    assert histogram([7, 1, 7, 1, 5]) == [(1, 2), (5, 1), (7, 2)]
    assert histogram([1, 1, 1]) == [(1, 3)]
    assert histogram([]) == []


if __name__ == "__main__":
    main()