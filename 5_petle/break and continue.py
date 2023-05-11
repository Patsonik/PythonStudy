"""
break and continue - przerwa i kontynuowanie

chce dodać trzy kolejnę liczby do siebie 


break - przerwa natychmiast wykonywanie danego zadania
continue - przerwa chwilowo i wraca do dalszgo kończenia zadania 
"""

"""
wynik = 0

for i in range(3):

    x=int(input("Podaj dodatnią liczbę: "))
    if (x>0):
          wynik +=x
    else:
        print("Miała być dodatania liczba! Kończymy za karę!")
        continue
    print ("Aktualny wynik dodawania to: ", wynik)

"""
print("Podaj trzy liczby dodatnie to je dodam :) " )

wynik = 0

i=0

while i < 3:

    x=int(input("Podaj dodatnią liczbę: "))
    if (x>0):
          wynik +=x
    else:
        print("Miała być dodatania liczba!Ponownie pytam o liczbę dodatnią ")
        continue
    print ("Aktualny wynik dodawania to: ", wynik)
    i +=1
    
# teraz przy petli while pomimo podania ujemnej liczby, dalej zapyta o kolejna liczbe do podania

#for tylko robi liczbe zadań którą mu wyznaczono, pomimo jakiegoś złego wyniku wśród działań
# while robi zadania w ilości wszystkich dopóki każdy nie będzie dobre
#while tak długo wykonywana póki wszystkie warunki na wszystkie zadania nie zostaną prawidłowo wykonane

