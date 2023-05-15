base=int(input('Base del sistema de numeración: '))

n1=int(input('Primer número: '))
digitos_n1=[]
n=0
resto=n1//(10**(n+1))
while resto!=0:
    n+=1
    resto=n1//(10**(n+1))
while n>=0:
    digito=n1//(10**n)
    digitos_n1.append(digito)
    n1=n1%(10**n)
    n-=1
for digito in digitos_n1:
    if digito>=base:
        print('dígito no válido...')
        validacion1=False
    else:
        validacion1=True

if validacion1:
    n2=int(input('Segundo número: '))
    digitos_n2=[]
    n=0
    resto=n2//(10**(n+1))
    while resto!=0:
        n+=1
        resto=n2//(10**(n+1))
    while n>=0:
        digito=n2//(10**n)
        digitos_n2.append(digito)
        n2=n2%(10**n)
        n-=1
    for digito in digitos_n2:
        if digito>=base:
            print('dígito no válido...')
            validacion2=False
        else:
            validacion2=True
if validacion1 and validacion2:
    matriz_producto= [[0]*len(digitos_n2) for n in range(digitos_n1)]

    for i in range(len(digitos_n1)):
        for j in range(len(digitos_n2)):
            matriz_producto[i][j]=int(digitos_n1[i])*int(digitos_n2[j])
    print(matriz_producto)

