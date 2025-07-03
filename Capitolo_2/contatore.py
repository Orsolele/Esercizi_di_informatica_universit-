def controllo(prendere):
    while True:
        try:
            numero = int(input(prendere))
            return numero
            
        except ValueError:
            print("INSERIRE N NUMERO INTERO MASSIMO\n")

    
def principale():
    print("---Benvenuti ai Numeri MASSIMI di Orso---")
    numero = controllo("Inserisci un Intero: ")
    contatore = 1
    while contatore <= numero:
        if contatore % 5 != 0:
            print(contatore)
            contatore += 1
        else:
            contatore += 1
            continue
            
            
if __name__ == "__main__":
   principale() 