m=int(input("Ingrese el numero de filas: "))
n=int(input("Ingrese el numero de columnas: "))
x=[]
a=[]
for i in range(m):
    y=[]
    for j in range(n):
        s=int(input("Ingrese los valores de la matriz: "))
        y.append(s)
        a.append(s)
    x.append(y)

print("-"*50)
print("La matriz original es: ")
for i in range(m):
    for j in range(n):
        print(x[i][j],end=" ")
    print()
print()
#creando la otra matriz:
m1=[]
for i in range(n):
    m1.append([0]*m)
l=0
for i in range(n):
    k=m-1
    for j in range(m):
        m1[i][j]=x[k][l]
        k-=1
    l+=1
print("La matriz girada 90 por primera ves: ")
for i in range(n):
    for j in range(m):
        print(m1[i][j],end=" ")
    print()
#creando la tercera matriz: 
m2=[]
for i in range(m):
    m2.append([0]*n)
l=0
for i in range(m):
    k=n-1
    for j in range(n):
        m2[i][j]=m1[k][l] # 20 10 00  21 11 11
        k-=1
    l+=1 
print("La matriz girada 90 por segunda ves")
for i in range(m):
    for j in range(n):
        print(m2[i][j],end=" ")
    print()
#creando la cuarta matriz:
m3=[]
for i in range(n):
    m3.append([0]*m)
l=0
for i in range(n):
    k=m-1
    for j in range(m):
        m3[i][j]=m2[k][l]
        k-=1
    l+=1
print("La matriz girada 90 por tercera vez")
for i in range(n):
    for j in range(m):
        print(m3[i][j],end=" ")
    print()

#creando la quinta matriz:
m4=[]
for i in range(m):
    m4.append([0]*n)
l=0
for i in range(m):
    k=n-1
    for j in range(n):
        m4[i][j]=m3[k][l] # 20 10 00  21 11 11
        k-=1
    l+=1
print("La matriz girada 90 por cuarta vez: ")
for i in range(m):
    for j in range(n):
        print(m4[i][j],end=" ")
    print()