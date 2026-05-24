"""
Creare lista, aggiungere elementi, stampare tutti elementi
Lista della spesa (aggiungi prodotti, stampa lista finale)
"""
import random

"""
fruitslist= []
fruitslist.append("orange")
fruitslist.insert(0,"banana")
fruitslist.insert(1,"cherry")
fruitslist.append("strawberry")
print(fruitslist)
"""

# Chiedi 5 numeri, mettili in lista, calcola media, stampa risultato (riassunto di tutta la settimana)

print("Dammi 5 numeri: ")
i1, i2, i3, i4, i5= int(input()), int(input()), int(input()), int(input()), int(input())

numList= [i3,i2,i5]
numList.append(i1)
numList.insert(0,i4)

media=0
contatore=0
for x in numList:
    media+=x
    contatore+=1
#media= media/contatore
media= media/len(numList)

print(numList)
print(f"Media: {media}")