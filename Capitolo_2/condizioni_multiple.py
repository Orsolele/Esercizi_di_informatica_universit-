def calcolo_eta(calcolo):
    if calcolo < 18:
        return "Minore"
    else:
        return "Maggiore"

def risparmi(risparmio):
    if risparmio >= 1000:
        return "Hai abbastanza Risparmi"
    else:
        return "Devi ancora risparmiare"
while True:
    nome = input("Inserisci il tuo nome: ")
    while True:
        try:
            eta = int(input("Inserisci la tua età"))
            break
        except ValueError:
            print("inserisci un valore valido")
    while True:
        try:
            saldo = abs(int(input("Inserire il tuo saldo: ")))
            break
        except ValueError:
            print("Inserire un saldo corretto!")
    print(f"Ciao {nome}, sei {calcolo_eta(eta)} e {risparmi(saldo)}")