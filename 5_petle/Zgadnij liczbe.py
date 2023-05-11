szukanaLiczba = 40
zgadywanaLiczba=0

while zgadywanaLiczba != szukanaLiczba:
    zgadywanaLiczba= int(input("Odgadnij iczbę: "))

    if (zgadywanaLiczba > szukanaLiczba):
        print("Za duża")

    elif (zgadywanaLiczba < szukanaLiczba):
        print("Za mała")    
    
    else:
        print("Brawo")

zgadywanaLiczba +=1 
    
