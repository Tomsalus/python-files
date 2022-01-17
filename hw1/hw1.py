from turtle import left, right, forward
from math import sin, degrees, radians, sqrt, acos


def house(width, height, roof_angle):
    alpha = (180 - roof_angle) / 2
    roof_side = (width / 2) * (sin(radians(90)) / sin(radians(roof_angle / 2)))
    diagonal = sqrt(width ** 2 + height ** 2)
    diagonal_angle = degrees(acos(
        (width ** 2 + diagonal ** 2 - height ** 2) / (2 * width * diagonal)))

    for _ in range(2):
        right(90)
        forward(height)
        right(90)
        forward(width)

    right(alpha)
    forward(-roof_side)
    right(roof_angle)
    forward(roof_side)

    left(180 - alpha - diagonal_angle)
    forward(diagonal)
    right(180 - diagonal_angle)
    forward(width)
    right(180 - diagonal_angle)
    forward(diagonal)


def nth_element_lu(p, q, index):
    first = 0
    second = 1
    if (index == 0):
        return first
    elif (index == 1):
        return second

    for _ in range(index - 1):
        next_num = p * second - (q * first)
        first = second
        second = next_num

    return next_num


def nth_unique_smallest_prime_divisor(num, index):
    prime_divisor = 0
    i = 2
    while i <= num and index > 0:
        if num % i:
            i += 1
        else:
            num //= i
            if prime_divisor != i:
                index -= 1
            prime_divisor = i

    if index != 0:
        return None
    else:
        return prime_divisor


def main():
    house(100, 150, 30)

    assert nth_element_lu(7, 9, 0) == 0
    assert nth_element_lu(5, 4, 1) == 1
    assert nth_element_lu(1, -1, 5) == 5
    assert nth_element_lu(3, 2, 7) == 127

    assert nth_unique_smallest_prime_divisor(12, 2) == 3
    assert nth_unique_smallest_prime_divisor(42350, 2) == 5
    assert nth_unique_smallest_prime_divisor(42350, 3) == 7
    assert nth_unique_smallest_prime_divisor(42350, 4) == 11
    assert nth_unique_smallest_prime_divisor(42350, 5) is None


if __name__ == '__main__':
    main()