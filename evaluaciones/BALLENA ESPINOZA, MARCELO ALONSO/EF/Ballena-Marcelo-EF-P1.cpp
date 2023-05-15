#include<iostream>
#include<fstream>
using namespace std;

struct nodo{
	char seccion;
	int nota;
	nodo *sgte;
}*p,*q,*r,*aux;

int main(){
	int cont =0,x,y,num,cont_u=0,cont_w=0,cont_v=0;	
	char cadena[128], subcadena[10];
	ifstream fe("Algoritmia.txt");
	while(!fe.eof()){
		fe>>cadena;
		cout<<cadena<<endl;
		if(cont==0){
			p = new nodo;
			p->seccion=cadena[0];
			x=cadena[1]-48;
			y=cadena[2]-48;
			num=x*10+y;
			p->nota=num;
			r=p;
			cont++;
		}
		else{
			q = new nodo;
		    q->seccion=cadena[0];
		    x=cadena[1]-48;
			y=cadena[2]-48;
			num=x*10+y;
		    q->nota=num;
		    q->sgte=NULL;
		    r->sgte=q;
		    r = r->sgte;
		}
	}
	aux = p;
    while(aux!=NULL){
    	if (aux->seccion=='W'){
    		cont_w++;
		}
		if (aux->seccion=='U'){
    		cont_u++;
		}
		if (aux->seccion=='V'){
    		cont_v++;
		}
 	    aux = aux->sgte;
    }
    cout<<"Cantidad de aprobados de la seccion w:"<<cont_w<<endl;
    cout<<"Cantidad de aprobados de la seccion v:"<<cont_v<<endl;
    cout<<"Cantidad de aprobados de la seccion u:"<<cont_u<<endl;
	fe.close();
	return 0;
}
