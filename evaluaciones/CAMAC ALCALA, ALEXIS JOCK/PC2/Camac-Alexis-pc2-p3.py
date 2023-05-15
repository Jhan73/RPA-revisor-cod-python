
a=int(input("Inserte el primer numero: "))
b=int(input("Inserte el segundo numero: "))
base=int(input("Ingrese la base a operar:"))
auxa=a
auxb=b
n1=[]
n2=[]
if(n2>n1):
  aux=n2
  n2=n1
  n1=aux
while(a>0):
  c=a%10
  n1.append(c)
  a=a//10
while(b>0):
  c=b%10
  n2.append(c)
  b=b//10
v=[]
for j in range(len(n2)):
  debe=0
  num=0
  for i in range(len(n1)):
    c=n2[j]*n1[i]+debe
    if(c<base):
      num=num*10+c
      debe=0
    if(c>=base):
      debe=c//base
      c=c-(debe*base)
      num=num*10+c
    if(i==len(n1)-1):
        if(debe!=0):
          num=num*10+debe
  v.append(num)
sumas=[]
for i in range(len(v)):
  p=v[i]
  nump=0
  while(p>0):
    c=p%10
    nump=nump*10+c
    p=p//10
  sumas.append(nump)
q=sumas[0]
exp=1
nr=0
for i in range(1,len(sumas)):
  p=sumas[i]*(10**exp)
  exp+=1
  debe=0
  o=True
  r=0
  ff=0
  while(p>0):
    c=p%10
    ver=1
    while(q>0 and o==True):
      d=q%10
      cif=c+d+debe
      ver=0
      if(cif<base):
        r=r*10+cif
        debe=0
      if(cif>=base):
        debe=cif//base
        cif=cif-(debe*base)
        r=r*10+cif
      o=False
      q=q//10
    if(q==0 and ver==1):
      if(p!=0):
        cif=c+debe
        if(cif<base):
          r=r*10+cif
          debe=0
        if(cif>=base):
          debe=cif//base
          cif=cif-(debe*base)
          r=r*10+cif
    p=p//10
    o=True

  if(p==0):
    if(debe!=0):
      r=r*10+debe
  final=r

  while(final>0):
    re=final%10
    ff=ff*10+re
    final=final//10
  q=ff
"""
auxa=a
auxb=b
"""
auxq=q
mostrar1=[]
mostrar2=[]
resultado=[]
while(auxa>0):
    cif1=auxa%10
    mostrar1.append(cif1)
    auxa=auxa//10
while(auxb>0):
    cif2=auxb%10
    mostrar2.append(cif2)
    auxb=auxb//10
#para mostrar: 

k=len(mostrar1)
# k=n+1
for i in range(len(mostrar1)//2):
    aux1=mostrar1[k-1]
    mostrar1[k-1]=mostrar1[i]
    mostrar1[i]=aux1
    k-=1
print("Los digitos del primer numero en base ",base," : ",mostrar1)
k=len(mostrar2)
# k=n+1
for i in range(len(mostrar2)//2):
    aux1=mostrar2[k-1]
    mostrar2[k-1]=mostrar2[i]
    mostrar2[i]=aux1
    k-=1
print("Los digitos del segundo numero en base ",base,": ",mostrar2)

while(auxq>0):
    cif3=auxq%10
    resultado.append(cif3)
    auxq=auxq//10
k=len(resultado)
# k=n+1
for i in range(len(resultado)//2):
    aux1=resultado[k-1]
    resultado[k-1]=resultado[i]
    resultado[i]=aux1
    k-=1
print("Los digitos del producto de los numeros son: ",resultado)