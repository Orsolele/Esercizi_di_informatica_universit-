while True:
    while True:
        numero = input("Inserie un numero intero: ")
        try:
            numero = int(numero)
            break
        except ValueError:
            print("Mi dispiace, quello che hai inserito non è un intero! Riprova.")
    if numero > 0:
        while True:
            try:
                numero2 = int(input("Inserisci il secondo numero: "))
                break
            except ValueError:
                print("Inserisci un numero corretto!")
        print(f"La somma tra i due numeri è: {numero + numero2}")
    elif numero<0:
        print(f"Il valore assoluto di {numero} è: {abs(numero)}")
    else:
        print("Hai inserito 0")