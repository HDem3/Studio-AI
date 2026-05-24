# Scrivere su file
# Leggere file
# Aggiungere testo

import os

"""
file= open("prova.txt", "w")
file.write("Ciao\n")
file.write("Ciao Mondo")
file.close()

file= open("prova.txt","r")
print(file.read())
file.close()

with open("prova.txt","a") as file:
    file.write("Hello world")

with open("prova.txt","r") as file:
    print(file.read())
"""

# To-do list salvata su file
# Aggiungi task
# Salva task
# Leggi task dal file

if not os.path.exists("todolist.txt"): 
    with open("todolist.txt","wt") as file:
        file.write("To do list:\n")

def addTask(task):
    with open("todolist.txt","at") as file:
        file.write(f"{task}\n")   

def readFile():
    with open("todolist.txt","rt") as file:
        print(file.read())

addTask(input())
readFile()


