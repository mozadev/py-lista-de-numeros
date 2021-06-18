listanumeros=[]

while True:
    n=int(input("ingrese un numero: "))
    listanumeros.append(n)
    palabra=input("ingrese la palabra BASTA si quiere deternese: ")
    if (palabra == "BASTA"):
        break

numPosit=[]
numMenPro=[]

for i in range(len(listanumeros)):
    if listanumeros[i]>0:
        numPosit.append(listanumeros[i])
suma=0
for i in range(len(listanumeros)):
    suma=suma+listanumeros[i]
promedio=suma/len(listanumeros)

for i in range(len(listanumeros)):
    if listanumeros[i]<promedio:
        numMenPro.append(listanumeros[i])

print(listanumeros)
print(numPosit)
print(numMenPro)