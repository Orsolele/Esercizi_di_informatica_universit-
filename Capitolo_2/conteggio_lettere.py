parola = input("Inserisci una parola: ")
conteggio = 0
cercare = ""
while len(cercare) != 1:
    cercare = input("Inserisci la lettera da ricercare: ")

for l in parola:
    print(l)
    if cercare in l:
        conteggio +=1
print(f"nella tua frase ci sono: {conteggio} A")