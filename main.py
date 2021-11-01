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





'''def input_is_palindrome():
    x = int(input("Fct verif daca un nr este palindrom."))
    if is_palindrome(x):
        print(x, "este palindrom.")
    else:
        print(x, "nu este palindrom.")
input_is_palindrome()
'''


#1)
def is_prime(n):
    '''Verifica daca un numar este prim
    :param n : un numar intreg
    :return : daca un nr e sau nu prim
    '''
    if n < 2:
        return False

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


def test_is_prime():
    #Testeaza is_prime

    assert is_prime(7) == True
    assert is_prime(9) == False
    assert is_prime(1) == False



def printMenu():
    print("1. Dati nr n: ")
    print("2. Verifica daca numarul este palindrom")
    print("3. Verifica daca numarul este prim")
    print("4. Iesire")

def main():
    test_is_prime()
    test_is_palindrome()
    while True:
        printMenu()
        optiune = input("Dati optiune: ")
        if optiune == "1":
            n = int(input("Dati nr n: "))
        elif optiune == "2":
            print(is_palindrome(n))
        elif optiune == "3":
            print(is_prime(n))
        elif optiune == "4":
            break
        else:
            print("Optiune gresita")
main()