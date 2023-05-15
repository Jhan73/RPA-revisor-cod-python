n=int(input("Ingrese el numero: "))    
for i in range(2,10):
    p=n
    num=0
    num1=0
    while(p>0):
        cif=p%i
        num=num*10+cif
        p=p//i
    q=num
    while(q>0):
        cif2=q%10
        num1=num1*10+cif2
        q=q//10
    if(num1==num and num1>9):
        print("El numero",n," es capicua en las base",i)
        print(num)


        