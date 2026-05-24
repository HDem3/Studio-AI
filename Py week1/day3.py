"""
Verifica se un numero è pari/dispari
Controllo maggiore età
Voto esame (>=18 promosso)
"""
import random
"""
x= random.randrange(6,31)

if x%2==0: 
    print(f"x: {x} è pari")
else: 
    print(f"x: {x} è dispari")

if x>=18: 
    print("Maggiorenne")
    print("Promosso")
else:
    print("Minorenne")
    print("Bocciato")
"""

# Gioco: chiedi numero all’utente, indovina se è >10 o <=10

x= int(input("Dammi un numero: "))

if x>10: print("x è maggiore di 10")
else:    print("x è minore o uguale a 10")
