"""
Conta lettere in una parola
Trasforma testo in maiuscolo
Conta quante volte appare una lettera
"""

import random
"""
parola= "banana"
print(len(parola))

contatore= 0
for x in parola:
    contatore += 1
print(contatore)

testo = "hello world"
testoUP= testo.upper()
print(testoUP)

parola= "banana"
print(parola.count("n"))
"""

# Analizzatore testo
# Input:
# “ciao come stai”
# Output:
# Numero caratteri
# Numero parole
# Testo maiuscolo

frase= "ciao come stai"
print(f"Numero caratteri: {len(frase)}")

cont= 0
in_word= False

for x in frase:
    if x!=" " and not in_word:
        in_word= True
        cont += 1
    elif x==" ":
        in_word = False

print(f"Numero parole: {cont}")
print(frase.upper())