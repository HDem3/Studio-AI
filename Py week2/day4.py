"""
Dizionario
Stampa valori
Modifica valori
Aggiungi nuovi campi
"""

import random
"""
dict= {
    "nome": "dem",
    "cognome": "huang", 
    "eta": 22
}

print(dict)

dict.update({"eta": 23})
dict.update({"birth": "09/08/2003"})

for x in dict.keys(): 
    print(f"{x}: {dict[x]}")

"""

# Rubrica contatti
# Ogni contatto:
# nome
# numero telefono

rubrica= {}
esci= True

while(esci):
    print("Rubrica")
    print("1) Aggiungi contatto")
    print("2) Elimina contatto")
    print("3) Visualizza rubrica")
    scelta= int(input("scelta: "))
    
    if scelta==1 :
        rubrica.update({input("nome: "): int(input("numero: "))})
    elif scelta==2:
        del rubrica[input("contatto da eliminare: ")]
    elif scelta==3:
        for x in rubrica:
            print(f"{x}: {rubrica[x]}")
    else: esci= False
