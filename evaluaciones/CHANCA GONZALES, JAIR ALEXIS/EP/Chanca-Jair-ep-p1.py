n=int(input('Ingresar "n":'))
lista=[]
for i in range(n):
    alumnos=[]
    for j in range(3):
        alumnos.append(0)
    lista.append(alumnos)

lista[0]=[12,60.6,1.55]
lista[1]=[29,73.8,1.82]
lista[2]=[15,82.4,1.78]
lista[3]=[31,60.6,1.71]
lista[4]=[73,73.8,1.77]
lista[5]=[62,82.1,1.91]
print(lista)

for i in range(1,n):
    elemento=lista[i]
    j = i - 1
    while j >= 0 and lista[j][1] > lista[i][1]:
        lista[j+1] = lista[j]
        j -= 1
    lista[j+1] = elemento

print(lista)

añadir_P=input('Desea añadir alumnos? S/N: ')
while añadir_P == 'S':
    codigo=int(input('Añadir código de alumno')
    codigovalido = True
    for i in range(n):
        if codigo <10 or codigo == lista[i][0]:
            codigovalido = False
    if codigovalido:
        peso=float(input('Añadir peso del alumno: '))
        talla = float(input('Añadir talla del alumno: '))
        nuevoalumno=[codigo,peso,talla]
        lista.append(nuevoalumno)
        
        for i in range(1,n):
            elemento=lista[i]
            j = i - 1
            while j >= 0 and lista[j][1] > lista[i][1]:
                lista[j+1] = lista[j]
                j -= 1
            lista[j+1] = elemento
            
        print(lista)
        
        añadir_P=input('Desea añadir alumnos? S/N: ')
    else:
        print('codigo no valido...')
        añadir_P=input('Desea añadir alumnos? S/N: ')