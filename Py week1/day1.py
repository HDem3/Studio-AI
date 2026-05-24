"""
Stampare “Ciao mondo”
Chiedere nome e salutare
Chiedere età e stampare messaggio tipo “Ciao [nome], hai [età] anni”
Variante extra: chiedi il colore preferito e stampa “Wow [colore] è bello!”
"""

"""
print("ciao mondo")

nome = input("Come ti chiami? ")
print("Ciao " + nome + "!") #print(f"Ciao {nome}!")

eta = input("Quanti anni hai? ")
print("ciao " + nome + ", hai " + eta + " anni!") #print(f"Ciao {nome}, hai {eta} anni!")

colore = input("Qual' ò il tuo colore preferito? ")
print(f"Wow {colore} è bello!")
"""


# Scrivi un programma che chiede 5 numeri, li salva in lista, calcola media e stampa il risultato

#num1, num2, num3, num4, num5 = input("Dammi 5 numeri:\nnum1: "), input("num2: "), 
#                               input("num3: "), input("num4: "), input("num5: ")
#list = [num1, num2, num3, num4, num5]

list = [int(input("Dammi 5 numeri:\nnum1: ")), int(input("num2: ")), 
        int(input("num3: ")), int(input("num4: ")), int(input("num5: "))]

print(f"media: {(list[0]+list[1]+list[2]+list[3]+list[4])/5}")
