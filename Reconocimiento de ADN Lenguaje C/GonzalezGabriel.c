#include <stdio.h>
#include <stdlib.h>

int MAT_ADF[15][4];
//MATRIZ QUE INICIA LOS NODOS Y SUS RESPECTIVOS CAMINOS
void llena_matriz(){
	MAT_ADF[0][0]=7;
    MAT_ADF[0][1]=0;
    MAT_ADF[0][2]=1;
    MAT_ADF[0][3]=2;
    MAT_ADF[1][0]=7;
    MAT_ADF[1][1]=0;
    MAT_ADF[1][2]=3;
    MAT_ADF[1][3]=2;
    MAT_ADF[2][0]=7;//error
    MAT_ADF[2][1]=0;
    MAT_ADF[2][2]=1;
    MAT_ADF[2][3]=3;
    MAT_ADF[3][0]=4;
    MAT_ADF[3][1]=3;
    MAT_ADF[3][2]=3;
    MAT_ADF[3][3]=3;
    MAT_ADF[4][0]=5;
    MAT_ADF[4][1]=3;
    MAT_ADF[4][2]=3;
    MAT_ADF[4][3]=3;
    MAT_ADF[5][0]=6;
    MAT_ADF[5][1]=3;
    MAT_ADF[5][2]=3;
    MAT_ADF[5][3]=3;
    MAT_ADF[6][0]=6;
    MAT_ADF[6][1]=13;
    MAT_ADF[6][2]=6;
    MAT_ADF[6][3]=6;
    MAT_ADF[7][0]=8;
    MAT_ADF[7][1]=0;
    MAT_ADF[7][2]=1;
    MAT_ADF[7][3]=2;
    MAT_ADF[8][0]=9;
    MAT_ADF[8][1]=0;
    MAT_ADF[8][2]=1;
    MAT_ADF[8][3]=2;
    MAT_ADF[9][0]=9;
    MAT_ADF[9][1]=9;
    MAT_ADF[9][2]=11;
    MAT_ADF[9][3]=10;
    MAT_ADF[10][0]=9;
    MAT_ADF[10][1]=9;
    MAT_ADF[10][2]=11;
    MAT_ADF[10][3]=12;
    MAT_ADF[11][0]=9;
    MAT_ADF[11][1]=9;
    MAT_ADF[11][2]=12;
    MAT_ADF[11][3]=10;
    MAT_ADF[12][0]=12;
    MAT_ADF[12][1]=13;
    MAT_ADF[12][2]=12;
    MAT_ADF[12][3]=12;
    MAT_ADF[13][0]=14;
    MAT_ADF[13][1]=13;
    MAT_ADF[13][2]=14;
    MAT_ADF[13][3]=14;
    MAT_ADF[14][0]=14;
    MAT_ADF[14][1]=13;
    MAT_ADF[14][2]=14;
    MAT_ADF[14][3]=14;
}
//AQUI ES DONDE REALMENTE TRABAJA EL CODIGO
int recorrido_arch(char Nom_arch[20]){

	FILE *arch;
	//variable que contendrá letra por letra la cadena
    char ADN;
    //posicion del automata en la matriz con el cual se determinará si es humano o mutante
	int pos=0;
	//se abre el archivo
    arch = fopen( Nom_arch , "r" );

    if(arch==NULL){
        printf("\n Error al abrir el archivo");
        exit(1);
    }

	while((ADN = fgetc(arch)) != EOF){

		//aqui es donde saltamos de nodo en nodo denro de la matriz
        if(ADN == 'a' ){
            pos = MAT_ADF[pos][0];
        }
        else if(ADN == 'c' ){
            pos = MAT_ADF[pos][1];
        }
        else if(ADN== 't' ){
            pos = MAT_ADF[pos][2];
        }
        else if(ADN == 'g' ){
            pos = MAT_ADF[pos][3];
        }
	}
	//se entrega la posicion final de la cadena
	return pos;
}
int main()
{
    char Nom_arch[20];
    char choise='s';
    int pos;
    llena_matriz();
    //ciclo que repite el automata para revisar mas cadenas de ADN
    while(choise == 's' || choise == 'S')
	{
        printf("\nIngrese el nombre del achivo: ");
        scanf("%s",&Nom_arch);

        pos = recorrido_arch(Nom_arch);
        //aqui es donde definimos la condicion si es que el ADN pertenece a un humano o mutante
        if(pos==13){
            printf("\nEl individuo es: MUTANTE");
        }else{
            printf("\nEl individuo es: HUMANO");
        }

        printf("\nDesea probar otro archivo? S/N : ");
        scanf("%s",&choise);

		system("cls");
	}

    return 0;
}
