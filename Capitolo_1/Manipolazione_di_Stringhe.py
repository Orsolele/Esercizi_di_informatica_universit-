frase = input("Inserisci la tua frase: ")
if " " in frase:
    print("La frase che hai inserito ha uno spazio vuoto")
trovare_indice = frase.find("f")
print("la lunghezza della frase inserita è", len(frase))
print("i primi cinque caratteri di questa frase sono: ", frase[:5])
print("La frase: ", frase, "è lunga: ",len(frase),"e i primi 5 caratteri sono:", frase[:5])
print (trovare_indice)
