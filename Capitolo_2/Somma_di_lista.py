lista = [8,2,3,4,5,6,10]
totale = 0
totale_l = 0
x = 0
for l in lista:
    print(l)
    print(x)
    totale += lista[x]
    totale_l += l
    x+=1
print(totale)
print(totale_l)