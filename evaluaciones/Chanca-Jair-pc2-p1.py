n=int(input('Cantidad de notas a ingresar: '))
notas=[0]*n

for i in range(n):
    notas[i]=int(input('Ingrese nota: '))
indice_aprobados=0.0
repeticiones=0

while indice_aprobados < 70.0:
    aprobados=0
    for i in range(n):
        if notas[i]<20:
            notas[i]+=repeticiones
    for nota in notas:
        if nota >= 10:
            aprobados+=1
    indice_aprobados=int((aprobados/n*100)*100)/100
    repeticiones+=1
    print(notas,str(indice_aprobados)+'%','de aprobados')

