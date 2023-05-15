base=int(input('Ingrese número en base 10: '))
for n in range(2,10):
    D=base
    q=D//n
    numero_str=''
    while q>=n:
        r=D%n
        numero_str=str(r)+numero_str
        D=q
        q=D//n
    numero_str=str(q)+numero_str
    if numero_str==numero_str[::-1]:
        print('El número es capicua en la.base:',n,'(pues el número es',numero_str,')')