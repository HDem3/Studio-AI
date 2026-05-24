"""
Lista
Trova numero massimo
Trova numero minimo
Ordina lista
"""

import random
"""
list= [random.randrange(1,10), random.randrange(1,10),
       random.randrange(1,10), random.randrange(1,10)]

print(list)

list.sort()
print(f"Numero massimo: {list[len(list)-1]}")
print(f"Numero minimo: {list[0]}")
print(f"lista ordinata: {list}")
"""

# Gestione voti studenti
# Inserisci voti
# Calcola media
# Trova voto massimo/minimo

print("Gestione voti studenti")
list= []
esci= True

while(esci):
    print("1) Inserire voto")
    print("2) Calcola Media")
    print("3) Visualizza massimo/minimo")
    scelta= int(input("scelta: "))
    print("\n\n")
    if scelta== 1:
        list.append(int(input("inserisci voto: ")))
    elif scelta== 2:
        ind=0
        media= 0
        for x in list:
            media += list[ind]
            ind+=1
        print(f"media: {media/len(list)}")
    elif scelta== 3:
        list.sort()
        print(list)
        print(f"massimo: {list[len(list)-1]}")
        print(f"minimo: {list[0]}")
    else :
        esci= False
