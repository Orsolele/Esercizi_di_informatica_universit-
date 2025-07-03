def prendi(prendere):
    """Richiedere in input dati"""
    while True:
        try:
            numero = int(input(prendere))
            return numero
        except ValueError:
            print("Errore: Inserire intero Valido. RIPROVARE!")
def stampa():
    """Stampa un saluto"""
    print("\nCiao Mondo\n")

def somma():
    "Somma di due numeri"
    print("\nSomma due Numeri")
    num1 = prendi("Inserisci il primo numero da sommare: ")
    num2 = prendi("Inserisci il secondo numero da Sommare: ")
    print(f"La somma di {num1} e {num2} è: {num1 + num2}\n")
def menu():
    """Mostra il menu principale all'utente"""
    print("--Benvenuti nel magico mondo di ORSO!--")
    print("1. Stampa un SALUTO!")
    print("2. Somma due Numeri!")
    print("3. ESCI!")
    print("----------------------------\n")

def inizio():
    """Funzione Principale che Gestisce il Ciclo del menu!"""
    while True:
        menu()
        scelta = prendi("scegli un'opzione (1, 2 o 3): ")
        if scelta == 1:
            stampa()
        elif scelta == 2:
            somma()
        elif scelta == 3:
            print("Grazie per aver usato programma orso")
            break
        else:
            print("Scelta non valida, inserisci 1, 2 o 3\n")
if __name__ == "__main__":
    inizio()
