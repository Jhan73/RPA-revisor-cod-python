#include<iostream>
using namespace std;
struct nodo{
	int numero;
	nodo *sgte;
}*p,*q,*r,*aux,*inicio,*final;

main(){
int n,i,dato,h,j;
cout<<"Ingrese la cantidad de datos: ";cin>>h;
for(i=0;i<h;i++){
	cout<<"Ingrese un numero para el dato "<<i+1<<" : ";cin>>dato;
	if(i==0){
		p = new nodo;
		p->numero=dato;
		r = p;
	}
	else{
		q = new nodo;
		q->numero=dato;
		q->sgte=NULL;
		r->sgte=q;
		r = r->sgte;
	}
}
cout<<endl;
aux = p;
while(aux!=NULL){
	if(aux->sgte==NULL){
		cout<<aux->numero<<endl;
	}
	else{
		cout<<aux->numero<<" -> ";
	}
	aux = aux->sgte;
}
final = p;
for(i=0;i<h;i++){
	aux=p;
	for(j=1;j<h-i;j++){
		aux=aux->sgte;
	}
	if(i==0){
		inicio=aux;
		r=inicio;
	}
	else{
		aux->sgte=NULL;
		r->sgte=aux;
		r=r->sgte;
	}			
}
cout<<endl<<"Ahora invertimos: "<<endl<<endl;
aux=inicio; 
while(aux!=NULL){
	if(aux->sgte==NULL){
		cout<<aux->numero<<endl;
	}
	else{
		cout<<aux->numero<<" -> ";
	}
	aux = aux->sgte;
}
return 0;
}
