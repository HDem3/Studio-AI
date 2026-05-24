# crea e usa moduli

# moduli: file che contiene un insieme di funzioni

"""
import car
# import car as x  # x.pres() invece di car.pres()
# from car import car/ pres # importa solo dict o def del modulo

car.pres(car.car["marca"],car.car["anno"])
"""

# Gioco indovina numero avanzato
# Numero casuale
# Tentativi limitati
# Difficoltà

import random

print("Indovina Numero")
print("Scegli difficolta:")
print("1) Facile")
print("2) Normale")
print("3) Difficile")

class OutRange(Exception): # non uso print perche se no melo stampa anche se non voglio
    def __init__(self,min,max):
        super().__init__(f"Errore, il numero dev'essere tra {min} e {max}")
    
def controllo(a, min , max):
    if a<min or a>max:
        raise OutRange(min,max)

min=1 
max=3

isOk=False

while(not isOk):

    try:
        scelta= int(input("scelta: "))
        controllo(scelta,min,max)

    except ValueError:
        print("Errore, dev'essere un numero")

    except OutRange as e:
        print(e)

    else: isOk= True


if scelta==1:
    max= 10
    vita=3
elif scelta== 2:
    max= 50
    vita=5
elif scelta==3:
    max=100
    vita=5

numero= random.randint(min,max)
print(f"\nIndovina numero da {min} a {max}\n")

win=False

while(vita>0 and not win):    
    
    try:
        x= int(input(f"Hai {vita} tentativi: "))
        controllo(x,min,max)
    except ValueError:
        print("Errore, dev'essere un numero")
    except OutRange as e:
        print(e)
        print()
    else:
        if numero==x:
            win=True
            print(f"\nHai vinto!!! il numero è {numero}")
            break

        elif numero>x:
            vita-=1 
            print(f"Hai sbagliato, il numero è più grande di {x}\n")

        elif numero<x: 
            vita-=1 
            print(f"Hai sbagliato, il numero è più piccolo di {x}\n")

if vita==0:
    print(f"Hai perso il numero è {numero}")
