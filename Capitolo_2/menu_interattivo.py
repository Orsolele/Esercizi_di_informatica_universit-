"""Crea un menu testuale che mostri all’utente alcune opzioni (ad esempio, “1.
Stampa un saluto”, “2. Somma due numeri”, “3. Esci”).
Utilizza un ciclo while per riproporre il menu finché l’utente non sceglie di
uscire.
Quando l’utente seleziona un’opzione, esegui l’operazione corrispondente.
"""
def controllo(numero1):
    while True:
        try:
            numero1 = int(numero1)
            return numero1
        except ValueError:
            numero1 = input("\n\nInserisci un VALORE INTERO: ")

while True:
    print("Benvenuti nel magico mondo di Emanuele,\n scegli una tra le seguenti opzioni:")
    print("Opzione 1: Stampa un Saluto, \nOpzione 2: Somma due numeri, \nOpzione 3: Esci.")
    while True:
        try:
            scelta = int(input("\nScegli L'opzione (inserisci 1, 2 o 3: )"))
            if scelta == 1 or scelta == 2 or scelta == 3:
                break
            else:
                ("Seleziona il Parametro Giusto!\n")
                
        except ValueError:
            continue
        print(scelta)
        
    if scelta == 1:
        print("\nCiao Mondo\n")
    elif scelta == 2:
       inserisci = input("Inserire PRIMO numero: ")
       inserisci1 = input("Inserire SECONDO numero: ")
       inserisci = controllo(inserisci)
       inserisci1 = controllo(inserisci1)
       print(f"La somma dei due numeri inseriti è: {inserisci+inserisci1}\n")
    elif scelta == 3:
        print("Sei USCITO\n")
        break