"""
Stampare numeri da 1 a 100
Somma numeri 1–100
Indovina numero (gioco semplice)
"""

import random

"""
# v1.0
i=1
while i<=100:
    print(i)
    i+=1

# v2.0
for i in range(100):
    print(i+1)

# v3.0    
for i in range(1,101):
    print(i)

somma= 0

# v1.0
i=1
while i<=100:
    somma+=i
    i+=1
print(somma)

# v2.0
for i in range(101):
    somma+=i
print(somma)

# v3.0
for i in range(1,101):
    somma+=i
print(somma)


ris= random.randrange(1,100)

i= int(input("Indovina il numero: "))

while i!=ris:
    if i<ris: 
        i= int(input(f"Ops, il numero è piu grande di {i}. Riprova: "))
    elif i>ris: 
        i= int(input(f"Ops, il numero è piu piccolo di {i}. Riprova: "))

print(f"Congratulazioni hai vinto, il numero è {ris}")   
"""

# Contatore di parole: chiedi frase e conta quante parole contiene

frase= input()
contatore= 0
in_parola= False

#aumenta contatore solo alla prima lettera che becca della parola
for char in frase:
    if char!=" " and not in_parola:
        in_parola= True 
        contatore+=1
    elif char ==" ":
        in_parola= False

print(f"La frase contiene {contatore} parole")