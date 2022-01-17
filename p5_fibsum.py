# Program spočítá sumu prvních ‹n› «sudých» členů
# Fibonacciho posloupnosti. Například volání ‹fibsum(3) = 44 =
# 2 + 8 + 34›.

def fibsum(n):
    first = 0
    second = 1
    summarization = 0
    while (n>0):
        next_number = first+second
        if next_number % 2 == 0:
            n-=1
            summarization +=next_number
        first = second
        second = next_number
    return summarization       


def main():
    assert fibsum(0) == 0
    assert fibsum(1) == 2
    assert fibsum(2) == 10
    assert fibsum(3) == 44
    assert fibsum(4) == 188
    assert fibsum(5) == 798
    assert fibsum(10) == 1089154


if __name__ == "__main__":
    main()