#include<iostream>
#include<string.h>
#include<conio.h>
#include<stdio.h>
#include<fstream>
using namespace std;

int main(){
	ifstream f("ALGORITMIA.txt");
	string cadena;
	char sec;
	int lf,i,j,lc,dig,cero='0',num=0;
	struct nodo{
		char seccion;
		int nota;
		nodo *sgte;
	}*inicio,*actual,*aux,*ante;
	inicio=NULL;
	while(!f.eof()){
		getline(f,cadena);
		lc=cadena.length();
		for(i=0;i<lc;i++){
			if(cadena[i]=='U' || cadena[i]=='V' || cadena[i]=='W'){
				sec=cadena[i];
			}
			if((cadena[i]>='0') && (cadena[i]<='9')){
				dig=cadena[i];
				num=num+dig-cero;
			}
			if(cadena[i]==' ' || cadena[i]=='\n'){
				if(inicio=NULL){
					inicio=new nodo;
					actual=inicio;
				}
				else{
					actual->sgte=new nodo;
					actual=actual->sgte;
				}
				actual->seccion=sec;
				actual->nota=num;
				actual->sgte=NULL;
				num=0;
			}

		}
	}
	int napu=0,napv=0,napw=0,max=0;
	int nu=0,nw=0,nv=0,c1=0,c2=0,c3=0;
	int notas[3];
	actual=inicio;
	while(actual!=NULL){
		if(actual->seccion =='U'){
			nu=nu+actual->nota;
			c1++;
			if(actual->nota>10){
			
				napu++;
			}	
		}
		if(actual->seccion =='V'){
			nv=nv+actual->nota;
			c2++;
			if(actual->nota>10){
			
				napv++;
			}
		}
		if(actual->seccion =='W'){
			nw=nw+actual->nota;
			c3++;
			if(actual->nota>10){
			
				napw++;
			}
		}
	}
	notas[0]=napu;notas[1]=napv;notas[2]=napw;
	for(i=0;i<3;i++){
		if(max<notas[i]){
			max=notas[i];
		}
	}
	if(max=napu){
		cout<<"\nLa seccion con mayor aprobados es la seccion U"<<endl;
	}
	if(max=napv){
		cout<<"La seccion con mayor aprobados es la seccion V"<<endl;
	}
	if(max=napw){
		cout<<"La seccion con mayor aprobados es la seccion W"<<endl;
	}
	cout<<"El promedio de la seccion U es: "<<nu/c1<<endl;
	cout<<"El promedio de la seccion V es: "<<nv/c2<<endl;
	cout<<"El promedio de la seccion W es: "<<nw/c3<<endl;
	
}

