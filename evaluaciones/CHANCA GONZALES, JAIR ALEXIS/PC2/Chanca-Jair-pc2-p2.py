# Crear matriz de 4 filas * 3 columnas
matriz = [[0]*3 for n in range(4)]

# Añadir las cantidades a los productos del respectivo empleado
ce=int(input('Código de empleado: '))
while ce != 0:
    cp=int(input('Código de producto: '))
    cantidad=int(input('Cantidad: '))
    matriz[ce-1][cp-1]=cantidad
    ce=int(input('Código de empleado: '))

print('-'*20)

# Mostrar reporte
for i in range(4):
    if matriz[i] != [0,0,0]:
        print('Empleado:',i+1)
        for j in range(3):
            if matriz[i][j] != 0:
                print('Producto',j+1,':',matriz[i][j])
