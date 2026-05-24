"""
Funzione saluto
Fuzione somma
Fuzione pari/dispari
"""

import random
"""
def saluto(name):
    print(f"ciao {name}")

def somma(a,b):
    return a+b

def isPari(a):
    if a%2==0: return True
    else: return False

name= "dem" 
a= random.randrange(1,10)
b= random.randrange(1,10)

saluto(name)
print(f"Somma tra {a} e {b}: {somma(a,b)}")
print(f"{a} è un pari? {isPari(a)}")
"""

#Calcolatrice con funzioni:
#somma()
#sottrazione()
#moltiplicazione()
#divisione()

def somma(a,b):
    return a+b
def sottrazione(a,b):
    return a-b
def moltiplicazione(a,b):
    return a*b
def divisione(a,b):
    return a/b

print("Calcolatrice")
print("Scegli operazione da eseguire: ")
print("1) Somma \n2) Sottrazione \n3)Moltiplicazione \n4)Divisione")

scegli= int(input())
a= random.randrange(1,10)
b= random.randrange(1,10)

if scegli==1: 
    print(f"somma tra {a} e {b}: {somma(a,b)}")
elif scegli==2:
    print(f"sottrazione tra {a} e {b}: {sottrazione(a,b)}")
elif scegli==3:
    print(f"Moltiplicazione tra {a} e {b}: {moltiplicazione(a,b)}")
elif scegli==4:
    print(f"Divisione tra {a} e {b}: {divisione(a,b)}")