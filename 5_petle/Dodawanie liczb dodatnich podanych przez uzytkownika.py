"""

CWICZENIE - Dodawanie liczb parzystych (nie dodatnich! xD) podanych
przez mua

"""

print("Podaj kolejno trzy liczby parzyste")

wynik = 0

i=0
while i < 3:
    x=int(input("Podaj parzystą liczbę: "))
    if (x>0 and x % 2==0):
        wynik +=x

    else:
        print("Miała być liczba parzysta")
        continue

    print("Wynik z dodawania to: ", wynik)

    i+=1



