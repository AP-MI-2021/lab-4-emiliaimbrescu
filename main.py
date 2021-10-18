def printmenu():
    print("1. Citirea unei liste de numere intregi.")
    print("2. Afișarea numărului obținut prin concatenarea tuturor numerelor pozitive din listă.")
    print("3. Afisarea sumei dintre cel mai mare si cel mai mic numar din lista.")
    print("4. Afișarea tuturor numerelor care au suma cifrelor mai mare sau egală decat un număr n citit de la tastatură.")
    print("5. Afișarea listei obținute din lista inițială în care numerele pătrat perfect sunt înlocuite cu radicalul acestora.")
    print("x. Iesire.")


def citirelista() -> list[int]:
    lst = []
    n = int(input("Dati un numar de elemente:"))
    for i in range(n):
        lst.append(int(input("l["+str(i)+"]=")))
    return lst


def concat_of_2(a: int, b: int):
    """
    Concatenam doar doua numere.
    :param a: int, primul numar la care se adauga b
    :param b: int, al doilea numar care este adaugat la finalul lui a
    :return: int, numarul a rezultat dupa concatenarea celor doua numere
    """
    y = b
    c = 1
    while y > 0:
        c = c * 10
        y = y // 10
    a = a * c + b
    return a


def get_concat_of_even(lst: list[int] ) -> int:
    x = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            x = concat_of_2(x, lst[i])
    print(x)


def maxim(lst: list[int]) -> int:
    """
    Aflam maximul dintr-un sir.
    :param lst: lista de intregi
    :return: maximul din lista
    """
    maxi = 0
    for i in range(len(lst)):
        if lst[i] > maxi:
            maxi = lst[i]
    return maxi
def minim(lst: list[int]) -> int:
    """
    Aflam minimul dintr-o lista
    :param lst: lista de intregi
    :return: minimul din lista
    """
    mini = 1000000
    for i in range(len(lst)):
        if lst[i] < mini:
            mini = lst[i]
    return mini



def sum_of_max_and_min_from_lst(lst: list[int]) -> int:
    a = maxim(lst)
    b = minim(lst)
    suma = a + b
    print(suma)


def suma_cifrelor(a: int) -> int:
    """
    Se afla suma cifrelor unui singur numar.
    :param a: int, numarul ale carui cifre se folosesc pentru aflarea sumei
    :return: suma cifrelor lui a
    """
    y = a
    su = 0
    while y > 0:
        su = su + y % 10
        y = y // 10
    return su


def sum_grater_or_equal_n(lst: list[int]) -> int:
    n = int(input("Dati un numar cu care sa se compare suma cifrelor numerelor din lista:"))
    for i in range(len(lst)):
        if suma_cifrelor(lst[i]) >= n:
            print(lst[i])


def main():
    lst = []
    while True:
        printmenu()
        optiune = input("Dati optiunea:")
        if optiune == "1":
            lst = citirelista()
        elif optiune == "2":
            get_concat_of_even(lst)
        elif optiune == "3":
            sum_of_max_and_min_from_lst(lst)
        elif optiune == "4":
            sum_grater_or_equal_n(lst)
        elif optiune == "5":
            pass
        elif optiune == "x":
            break
        else:
            print("Nu se gaseste optiunea. Incearca din nou!")

if __name__ == "__main__":
    main()