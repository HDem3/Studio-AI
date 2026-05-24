# Funzionalità:
# Inserire studenti
# Salvare voti
# Calcolare media
# Trovare migliore studente 

# Usa:
# funzioni
# liste
# dizionari
# loop
# if/else

import random

def addStu(dict, nome, voto):
    dict.update({nome: voto})

def salvaVoti(dict,lista):
    lista.extend(list(dict.values())[len(lista):])

def media(lista, lun):
    media=0
    for x in lista:
        media+=x
    return media/lun

def votoMax(lista,x,max):
    if lista is None or len(lista)==0: return 0
    if x== len(lista):
        return lista[max]
    else:
        if lista[x]>=lista[max]: max=x
        return votoMax(lista, x+1, max)

studente= dict()
listaVoti= list()

addStu(studente, "dem", 22)
addStu(studente, "mar", 26)
addStu(studente, "ziy", 26)
addStu(studente, "dav", 23)
addStu(studente, "nik", 26)

salvaVoti(studente, listaVoti)
print(listaVoti)


print(f"Media: {media(listaVoti,len(listaVoti))}")

votoMassimo=votoMax(listaVoti, 0, 0)
print(f"Voto max: {votoMassimo}")


print("Studente col voto piu alto : ")
for x in studente.keys():
    if studente[x]==votoMassimo:
        print(x)

