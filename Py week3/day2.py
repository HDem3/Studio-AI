# Gestire input sbagliati

"""
try: # esegue il codice 
    print(x)
except: # se ce un errore (posso definire tipo di errore)
    print("errore di stampa")
else: # se non ce errore
    x=5
    print(x)
finally: # esegue anche se ce errore
    print("fine")
"""

# Login semplice:
# username
# password
# gestione errori input

username= "dem"
password= 123

try:
    user= input("username: ")
    passw= int(input("password: "))    
except ValueError:
    print("passowrd deve essere composto da 3 cifre")
    #raise ValueError("passowrd deve essere composto da 3 cifre")
else:
    if user==username and passw==password:
        print("login succeed")
    else: 
        print("login failed")
