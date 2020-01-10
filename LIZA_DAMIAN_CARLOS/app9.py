#MENU

import libreria
opc=0  #ocpiones
max=3  #maximo de opciones

def opcionA():
    pre=libreria.precion_hidrostatica(int(input("OPCION 1: CALCULA LA PRECION HIDROSTATICA:Ingrese la gravedad:"))) #validad si el numero es <0
    print("la precion hidrostatica es:",pre)
    print("")

def opcionB():
    pote=libreria.potencia(int(input("OPCION 2: CALCULA LA POTENCIA:Ingrese el tiempo para poder hallar la potencia:"))) #validad si el nro ingresado por teclado es <0
    print("la potencia es:",pote)


while (opc !=max):
    #IMPRECION DE MENU
    print("################  MENU  ###########")
    print("1.CALCULA LA PRECION HIDROSTATICA: ")
    print("2.CALCULA LA POTENCIA:             ")
    print("3.SALIR:                           ")
    print("###################################")

    #ELECCION DE LAS OPCIONES
    opc=libreria.pedir_entero("INGRESE LA OPCION:",1,3)

    #MAPEO DE OPCIONES
    if (opc==1):
        opcionA()
    if (opc==2):
        opcionB()
    #fin_mapeo
#fin_menu
print("fin del programa")
