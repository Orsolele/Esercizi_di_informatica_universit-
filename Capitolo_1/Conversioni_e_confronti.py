numero_fisso = 150
while True:
    while True:
        inserimento = input("Inserisci il valore: ")
        try:
            inserimento = int(inserimento)
            break
        except ValueError:
            print("Non hai inserito un intero")

    if inserimento == numero_fisso:
        print("Hai indovinato:")
        break
    elif inserimento < numero_fisso:
        print("Il numero è più piccolo di quello che ho scelto")
    else:
        print("Il numero che hai inserito è più grande:")