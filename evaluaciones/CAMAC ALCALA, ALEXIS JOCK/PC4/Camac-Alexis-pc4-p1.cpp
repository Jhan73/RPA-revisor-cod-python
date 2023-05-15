#include<iostream>
#include<string.h>
#include<conio.h>
#include<stdio.h>
#include<fstream>
using namespace std;
void invertir(int x[],int n){
	struct nodo2{
		int valor;
		nodo2 *sgte2;
		
	}*inicio2,*actual2,*ante2,*aux2,*fin2;
	inicio2=NULL;
	
	while(0<n){
		if(inicio2==NULL){
			inicio2=new nodo2;
			actual2=inicio2;
		}
		else{
			actual2->sgte2=new nodo2;
			actual2=actual2->sgte2;
			
		}
		actual2->valor=x[n-1];
		actual2->sgte2=NULL;
		n--;
	}
	actual2=inicio2;
	while(actual2!=NULL){
		cout<<actual2->valor<<" ";
		actual2=actual2->sgte2;
	}
}

int main(){
	struct nodo{
		int dato;
		nodo *sgte;
	}*inicio,*actual,*ante,*aux,*fin;
	inicio=NULL;
	
	int n,i,j,c,l,index=0;
	int x[50],lista[50],val[50],last[50];
	do{
	
	cout<<"Ingrese la cantidad de numeros: ";cin>>n;
	}while(n>=50);
	
	i=0;
	for(i=0;i<n;i++){
	
		do{
			cout<<"Ingrese el numero #"<<i+1<<" : ";cin>>x[i];
		}while(x[i]<10);
	}
	int k=0,z=0;
	//eliminando parecidos
	for (i=0;i<n;i++){
		l=x[i];
		c=0;
		val[k]=l;
		k++;
		for (j=0;j<n;j++){
			if(val[j]==l){
				c++;
			}
		}
		if(c==1){
			lista[index]=l;
			index++;
		}
	}
	i=0;
	while(i<index){
		if(inicio==NULL){
			inicio=new nodo;
			actual=inicio;
		}
		else{
			actual->sgte=new nodo;
			fin=actual;
			actual=actual->sgte;
			
		}
		actual->dato=lista[i];
		actual->sgte=NULL;
		i++;
	}
	cout<<"--------------------------------------------"<<endl;
	//mostrando la primera lista:
	cout<<"Mostrando la lista original: "<<endl;
	actual=inicio;
	while(actual!=NULL){
		cout<<actual->dato<<" ";
		actual=actual->sgte;
	}
	cout<<"\nMostrando la lista invertida: "<<endl;
	invertir(lista,index);
}

