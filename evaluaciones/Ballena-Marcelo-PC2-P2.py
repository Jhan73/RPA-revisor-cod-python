# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S2EoI8ryZOdkVOOA1u3r94DVbWtnhykU
"""

matriz = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
codigo=1
while codigo!=0:
  codigo=int(input("Codigo de empleado: "))
  if codigo== 1 or codigo== 2 or codigo== 3 or codigo== 4:
    producto=int(input("Codigo del producto: "))
    if producto == 1 or producto == 2 or producto == 3:
      cantidad=int(input("Cantidad del producto: "))
      matriz[codigo-1][producto-1]=matriz[codigo-1][producto-1]+cantidad
    else:
      print("ERROR")
  elif codigo==0:
    print("")
  else:
    print("ERROR")

for  i in range(4):
  if matriz[i]!=[0,0,0]:
    print(f"Codigo de empleado:{i+1}")
    for j in range(3):
      if matriz[i][j]!=0:
        print(f"Producto {j+1}: {matriz[i][j]}")
    print("")
    