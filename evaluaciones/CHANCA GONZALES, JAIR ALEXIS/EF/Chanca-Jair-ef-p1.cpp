# include <iostream>
# include <conio.h>
#include <fstream>
using namespace std;

struct nodo
{int dato;
nodo *sgte;
};

nodo *U, *V, *W;
nodo *p, *q ;

int main(){
string nombreArchivo = "ALGORITMIA.txt";
ifstream archivo(nombreArchivo.c_str());
string linea;
string text("");
while (getline(archivo, linea)) {
text += linea;
text += " ";
}

}
