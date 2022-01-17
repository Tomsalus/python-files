import random


INVALID_POSITION = 0
EMPTY_POSITION = 1
ROUND_OVER = 2
PLAY_AGAIN = 3


def init(size, start):
    our = []
    their = []
    for _ in range(size):
        our.append(start)
        their.append(start)
    our.append(0)
    their.append(0)

    return (our, their)


def play(our, their, position):
    hole_value = 0
    board_length = len(our)
    swap = False

    if position >= board_length - 1 or position < 0:
        return INVALID_POSITION
    elif our[position] == 0:
        return EMPTY_POSITION
    elif our[position] != 0:
        hole_value, our[position] = our[position], 0
        position += 1

        while hole_value > 0:
            if position < board_length:
                if not (swap is True and position == board_length - 1):
                    our[position] += 1
                    hole_value -= 1
                position += 1

            elif position >= board_length:
                their, our = our, their
                position = 0
                swap = not(swap)

    if position - 1 == board_length - 1:
        return PLAY_AGAIN

    position -= 1
    if (our[position] == 1 and
            their[- 2 - position] != 0 and swap is False):
        our[board_length - 1] += our[position] + their[- 2 - position]
        our[position] = 0
        their[- 2 - position] = 0

    return ROUND_OVER


def random_choice(our):
    non_zero_numbers = []

    if our[:-1] == [0] * (len(our) - 1):
        return None

    for position, num in enumerate(our):
        if num != 0 and position != len(our) - 1:
            non_zero_numbers.append((num, position))

    random_position = random.randint(0, len(non_zero_numbers) - 1)
    _, position = non_zero_numbers[random_position]

    return position


def run_random_game(size, start):
    our, their = init(size, start)
    game_state = 0
    choice = random_choice(our)
    while choice is not None:

        game_state = play(our, their, choice)
        if game_state == ROUND_OVER:
            our, their = their, our
        choice = random_choice(our)

    for position in range(len(their) - 1):
        their[len(their) - 1] += their[position]

    return (our[-1], their[-1])


def main():
    # --- init ---

    assert init(6, 3) \
        == ([3, 3, 3, 3, 3, 3, 0], [3, 3, 3, 3, 3, 3, 0])

    assert init(9, 7) \
        == ([7, 7, 7, 7, 7, 7, 7, 7, 7, 0], [7, 7, 7, 7, 7, 7, 7, 7, 7, 0])

    # --- play ---

    our = [3, 0, 6, 0]
    their = [3, 3, 3, 0]
    assert play(our, their, -1) == INVALID_POSITION
    assert our == [3, 0, 6, 0]
    assert their == [3, 3, 3, 0]

    our = [3, 0, 6, 0]
    their = [3, 3, 3, 0]
    assert play(our, their, 0) == PLAY_AGAIN
    assert our == [0, 1, 7, 1]
    assert their == [3, 3, 3, 0]

    our = [3, 0, 6, 0]
    their = [3, 3, 3, 0]
    assert play(our, their, 1) == EMPTY_POSITION
    assert our == [3, 0, 6, 0]
    assert their == [3, 3, 3, 0]

    our = [3, 0, 6, 0]
    their = [3, 3, 3, 0]
    assert play(our, their, 2) == ROUND_OVER
    assert our == [4, 0, 0, 6]
    assert their == [4, 0, 4, 0]

    our = [3, 0, 6, 0]
    their = [3, 3, 3, 0]
    assert play(our, their, 3) == INVALID_POSITION
    assert our == [3, 0, 6, 0]
    assert their == [3, 3, 3, 0]

    # --- random_choice ---

    assert random_choice([1, 2, 3, 4, 0]) in [0, 1, 2, 3]

    assert random_choice([3, 3, 0, 3, 3, 7]) in [0, 1, 3, 4]

    assert random_choice([0, 0, 0, 1]) is None


if __name__ == '__main__':
    main()