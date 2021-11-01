#5)
def is_palindrome(n) -> bool:
    """Verif daca nr dat este un palindrom
    :param n:  Nr care este verificat
    :return : Daca este sau nu palindrom
    """
    inv = 0
    l = len(str(n))

    for i in range(l // 2):
        inv *= 10
        inv += n % 10
        n //= 10

    if l % 2 == 1:
        n //= 10

    return n == inv


def test_is_palindrome():
    # Testeaza is_palindrome

    assert is_palindrome(1234321) == True
    assert is_palindrome(52525) == True
    assert is_palindrome(1234) == False
    assert is_palindrome(5) == True
    assert is_palindrome(101) == True


test_is_palindrome()


def input_is_palindrome():
    x = int(input("Fct verif daca un nr este palindrom."))
    if is_palindrome(x):
        print(x, "este palindrom.")
    else:
        print(x, "nu este palindrom.")
input_is_palindrome()



#1)
def is_prime(x):
    '''Verifica daca un numar este prim
    :param x : un numar intreg
    :return : daca un nr e sau nu prim
    '''
    if x < 2:
        return False

    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False

    return True


def test_is_prime():
    #Testeaza is_prime

    assert is_prime(7) == True
    assert is_prime(9) == False
    assert is_prime(1) == False

test_is_prime()

	
