"""
CWICZENIE WYPISANIE LICZB DO 1200, KTÓRE SĄ PODZIELNE PRZEZ 5,
ALE NIE DZIELĄ SIĘ PRZEZ 7


a=5

print(6 % a )

% - oznacza resztę z dzielenia czyli np 6/5 reszta 1 

"""


for i in range(1200):
    if (i % 5 ==0  and not i % 7 == 0):
        print("Liczba", i, "dzieli się przez 5 i nie dzieli się przez 7")

        
"""

for i in range(1200):
    if (i % 5 ==0  and   % 7 == 1):
        print("Liczba", i, "dzieli się przez 5 i nie dzieli się przez 7")


 # dałoby wynik dzielenia przez 5 i reszty 1 z dzielenia przez 7

 """
