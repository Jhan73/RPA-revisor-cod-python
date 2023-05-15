
n=int(input("Ingrese el numero de alumnos"))
lista=[]
c=0
for i in range(n):
    nota=int(input("Ingrese la nota del alumno"+str(i+1)+" : "))
    lista.append(nota)
    if(nota>=10):
        c+=1
q=n*0.7
r=round((c*100)/n,2)
print(lista,r,"porcentaje de aprobados")

if(c<q):
    o=True
    while(o==True):
        cont=0
        for i in range(len(lista)):
            if(lista[i]<=20):
                lista[i]=lista[i]+1
                if(lista[i]>=10):
                    cont+=1
        print(lista,round((cont*100/n),2),"porcentaje de aprobados")
        if(n%2==0):
            if(cont>=n*0.7):
                o=False
        if(n%2!=0):
            if(cont>=n*0.7):
                o=False

