while True:
    while True:
        primo = input("Inserisci il primo numero: ")
        secondo = input("Inserisci il secondo numero: ")
        try:
            primo = int(primo)
            secondo = int(secondo)
            break
        except ValueError:
            print("Non hai inserito un intero: ")
    while True:
        operatore=""
        while len(operatore) != 1:
            operatore = input("Inserisci l'operatore da utilizzare (deve avere un carattere): ")
            if len(operatore)==1:
                break
            else:
                print("inserisci un solo carattere")
        if "+" in operatore:
            print(primo,operatore,secondo,"=",primo+secondo)
            break
        elif "-" in operatore:
            print(primo,operatore,secondo,"=",primo-secondo)
            break
        elif "/" in operatore:
            print(primo,operatore,secondo,"=",primo/secondo)
            break
        elif "*" in operatore:
            print(primo,operatore,secondo,"=",primo*secondo)
            break
        else:
            print("Hai inserito un valore sbagliato")
    
