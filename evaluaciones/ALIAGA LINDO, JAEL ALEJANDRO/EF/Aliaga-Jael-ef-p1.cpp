# include <iostream>
# include <conio.h>
using namespace std;
struct nodo{
	char dato;
	nodo *sgte;
};
nodo *h;
nodo *p, *q;
nodo *x;
char op;
int main(){
cout<<"Seccion y nota"<< " -> "; cin>>op;
	if (p != NULL) {
	h = new nodo;
	p = h;
	p->dato = op;
	}
	cout<<"Seccion y nota"<< " -> "; cin>>op;
	while (op != '*') {
	p->sgte = new nodo;
	p = p->sgte;
	p->dato = op;
	cout<<"Seccion y nota"<< " -> "; cin>>op;}
	p = h; //mostrando elementos de la lista
	while (p != NULL) {
		cout<<p->dato;
		p = p->sgte;}
		
return 0;	
}