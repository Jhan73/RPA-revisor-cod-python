x=[]
for i in range(4):
    x.append([0]*3)
ind=[0,1,2]
o=True

while(o==True):
    cod=int(input("Ingrese el codigo del empleado: "))
    if(cod==0):
        break
    producto=int(input("Ingrese el codigo de producto: "))
    cant=int(input("Ingrese la cantidad del producto: "))
    if((cod>=1 and cod<=4) and (producto>=1 and producto<=3) and cant>0):
        x[cod-1][producto-1]=x[cod-1][producto-1]+cant
for i in range(4):
    for j in range(1,3):
        for k in range(3-j):
            if(x[i][k]>x[i][k+1]):
                aux=x[i][k]
                x[i][k]=x[i][k+1]
                x[i][k+1]=aux
                aux1=ind[k]
                ind[k]=ind[k+1]
                ind[k+1]=aux


for i in range(4):
    print("El empleado #",i+1)
    for j in range(3):
        if(x[i][j]!=0):
            print("Codigo del producto ",j+1," : ",x[i][j])
    print()
