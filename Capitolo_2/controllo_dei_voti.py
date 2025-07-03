while True:
    try:
        voto = int(input("inserisci il voto del tuo esame: "))
    except ValueError:
        print("inserisci un voto intero")
    if voto >= 0 and voto <= 5:
        print("sei insufficiente")
    elif voto >= 6 and voto <= 8:
        print("sei buono")
    elif voto >= 9 and voto <= 10:
        print("Sei Ottimo")
    else:
        print("inserisci un valore da 0 a 10!")