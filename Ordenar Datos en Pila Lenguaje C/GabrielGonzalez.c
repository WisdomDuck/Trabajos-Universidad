#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char pila[1000];    //"pila" almacena la pila del autómata apilador. En la posición 0 siempre deberá estár el "simbolo de pila vacía" Z0 (Se llena hacia la derecha)
char CadenaEntrada[1000]; //"CadenaEntrada" posee la cadena de entrada al autómata, leída desde el archivo de texto.

//FUNCION QUE LITERALMENTE NOS AYUDA A MOSTRAR QUE HAY DENTRO DE LA PILA
/*void mustraPilita(){
	int i;printf("\n");
	for(i=0;i<20;i++){
		printf(" %c",pila[i]);
	}
}*/
void LecturaEntrada(char NomArchivo[20])
{
	FILE *archivo;

    archivo = fopen(NomArchivo , "r");// SE ABRE EL ARCHIVO
    
    if(archivo==NULL)
    {
        printf("\nEl archivo no existe.\nEste programa se cerrar%c.", 160);
        exit(-1);
    }

    AnalizaAutomata(archivo);//FUNCION QUE HACE TODO EL PROCESO
    
}
/*ESTA FUNCION DEVUELVE EL CARACTER QUE SE ESPERABA EN EL ERROR*/
char comparation(char car){
    char vuelta;
    if(car=='}'){
        vuelta='{';

    }else if(car==')'){
        vuelta='(';

    }else if(car==']'){
        vuelta='[';
    }
    return vuelta;
}
void AnalizaAutomata(FILE *arch)
{
	/*VALIABLES POR LAS QUE NOS MOVEREMOS EN LA CADENA Y LA PILA*/
    int i,j=0,contL=1;
    
    //char c;
    pila[0]='z';
    //CONDICION DE TERMINO DE CICLO DE RECONOCIMIENTO DE LINEA
    while(!feof(arch)){
    	//LEE UNA LINEA ENTERA DE CARACTERES Y LA GUARDA EN UNA VARIABLE
        fgets(CadenaEntrada, 1000 , arch);
        i=0;
        while( CadenaEntrada[i]!='\n' ){//CONDICION EN DONDE LA CADENA SE LEERA CARACTER POR CARACTER HASTA EL FIAL DE LA LINEA
        
        	/*SUPONIENDO DE QUE NO HAY ERORESDE SINTAXIS, SIEMPRE POR INICIO VA A HABER GUARDADA 
        	HASTA EL FINAL UNA LLAVE '{' LO CUAL INDICA QUE SI EXISTE ALGUNA OTRA LLAVE ANTES DE ESTA.... INMEDIATAMENTE ESTÁ MALA LA LINEA 
			DE CODIGO (CASO BASE, LA PILA SE LLENA)*/ 
            if(CadenaEntrada[i]=='{'){
            	if(pila[j]=='(' || pila[j]=='['){
            		printf("\nTiene un error de balance de parentesis en la linea %i. Se esperaba un: %c ",contL,comparation(CadenaEntrada[i]));             
                	exit(1);
				}else{
					/*EN ESTE PUNTO HACEMOS QUE SE AGREGUE UN VALOR A LA PILA Y QUE SE AVANCE HASTA EL TOPE,
					ASÍ PODEMOS LEEREL TOPE DE ESTA CUANDO PASEMOS AL SIGUIENTE CARACTER LEIDO*/
					pila[j+1]='{';
                	j++;
				}        
            }
            /*CASO BASE, LA PILA SE LLENA CON '('*/
            else if(CadenaEntrada[i]=='('){
                pila[j+1]='(';
                j++;
            }
            /*CASO BASE, LA PILA SE LLENA CON '['*/
            else if(CadenaEntrada[i]=='['){
                pila[j+1]='[';
                j++;
            }
            /*CASOS SECUNDARIOS EN DONDE EMPEZAREMOS A QUITAR VALORES A LA PILA*/
            else if(CadenaEntrada[i]=='}' && pila[j]=='{'){
            	//COLOCAMOS UN VALOR 'f' SOLO DE REFERENCIA.... PARA SABER SI ALGÚN VALOR FUE VACIADO
            	//TAMBIEN QUITAMOS UN VALOR EN LA PILA Y RETROCEDEMOS AL ANTERIOR
                pila[j]='f';
                j--;
            }
            else if(CadenaEntrada[i]==')' && pila[j]=='('){
                pila[j]='f';
                j--;
            }
            else if(CadenaEntrada[i]==']' && pila[j]=='['){
                pila[j]='f';
                j--;
            }
            /*AQUI IDENTIFICAMOS EL ERROR EN LA LINEA ESACTA EN DONDE SOBRA UN PARENTECIS O FALTA UNO,
            SE DETERMINA CUANDO LA PILA Y EL CARACTER NO COINCIDEN*/
            else if((CadenaEntrada[i]=='}' && pila[j]!='{')||(CadenaEntrada[i]==')' && pila[j]!='(')||(CadenaEntrada[i]==']' && pila[j]!='[')){
            	//LEIA UNA LINEA INEXISTENTE LA CUAL SE ARREGLABA PONIENDO UNA CONDICION "IF"
            	if(!feof(arch)){
                	printf("\nTiene un error de balance de parentesis en la linea %i. Se esperaba un: %c ",contL,comparation(CadenaEntrada[i]));    
					fclose(arch);          
                	exit(1);
				}
            }
            else if((CadenaEntrada[i]=='}' || CadenaEntrada[i]==')' || CadenaEntrada[i]==']') && pila[j]=='z'){
            	if(!feof(arch)){
                	printf("\nTiene un error de balance de parentesis en la linea %i. Se esperaba un: %c ",contL,comparation(CadenaEntrada[i]));    
					fclose(arch);          
                	exit(1);
				}
            }   
			//AUNMENTAMOS EL INDICE QUE LEEREA EL SIGUIENTE CARACTER    
            i++;
            
        }
        //CONTADOR DE LA LINEA QUE SE ESTÁ REVISANDO
        contL++;
    }
    //CONDICION EN EL CASO DE QUE SE CUMPLA QUE EL CODIGO ESTA BUENO
    if (pila[j]=='z'){
        printf("\nLos parentecis estan balanceados");
        fclose(arch);
        
    }
}

int main()
 {
	char NomArchivo[20];//NOMBRE DEL ARCHIVO
	char sig='S';//CONFIRMACION DE CICLO DE REPETICION
	int num=1;//NUMERO DE CONFIRMACION DE CICLO
	while(num){
		printf("\nIngrese el nombre del archivo: ");
		
		scanf("%s", &NomArchivo);// SE INGRESA EL NOMBRE DEL ARCHIVO

		LecturaEntrada(NomArchivo);
		
		printf("\nDesea probar otro archivo S/N?  ");
		
		scanf(" %c" , &sig);
		
		if(sig=='N'){// NO CONTINUA PRUEBA
			num=0;
		}
		system("cls");
	}
	printf("\n\n");
	return 0;
}

