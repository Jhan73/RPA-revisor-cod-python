matriz=[[2,5,7][4,3,9]]
print(matriz)
filas=len(matriz)
columnas=len(matriz[0])
while n in range(4):
    matriz2=[]
    for i in range(columnas):
        matriz2.append[[]]
        for j in range(filas):
            matriz2[0].append(0)
    for i in range(filas):
        for j in range(columnas):
            matriz2[i][j]=matriz[j][filas-i-1]
    print(matriz2)
    matriz=matriz2
    filas=len(matriz2)
    columnas=len(matriz2[0])
