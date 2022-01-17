#Napište funkci, která pro zadané číslo number najde nejbližší
#větší číslo, které je násobkem čísla k.

#Dále napište funkci, která pro zadané číslo number najde nejbližší větší
#prvočíslo.



def next_multiple(number,k):
    number+=1
    found = False
    while (found == False):
        if (number % k == 0):
            found = True
        else:
            number +=1
    return number

def next_prime(number):
    number+=1
    if number<1: return 1
    elif number>1:
        for i in range(2,number):
            if (number % i) == 0:
                number+=1
                break
    return number            
                

def main():
    assert next_multiple(1, 2) == 2
    assert next_multiple(10, 7) == 14
    assert next_multiple(10, 5) == 15
    assert next_multiple(54, 6) == 60
    assert next_multiple(131, 29) == 145
    assert next_multiple(123, 112) == 224
    assert next_multiple(423, 90) == 450
    
    assert next_prime(1) == 2
    assert next_prime(2) == 3
    assert next_prime(3) == 5
    assert next_prime(4) == 5
    assert next_prime(11) == 13
    assert next_prime(12) == 13


if __name__ == "__main__":
    main()