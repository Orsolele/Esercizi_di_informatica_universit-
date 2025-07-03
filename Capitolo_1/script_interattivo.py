def saluto(nome1):
    if "mario" in nome1.lower():
        print(f"ciao {nome1} è un piacere fare la tua conoscenza")
    elif "carlo" in nome1.lower():
        print(f"ciao {nome1} sei una forza della natura")
    else:
        print(f"ciao {nome1}, sei il migliore")
while True:
    nome = input("Inserisci il tuo nome: ")
    saluto(nome)
