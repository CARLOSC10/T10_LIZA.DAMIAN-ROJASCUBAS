#MENU

import libreria
opc=0  #ocpiones
max=3  #maximo de opciones

def opcionA():
    area1=libreria.area_trapecio(int(input("OPCION 1: CALCULA EL AREA DEL TRAPECIO:Ingrese la base mayor:"))) #validad si el numero es <0
    print("el area del trapecio es:",area1)
    print("")

def opcionB():
    are=libreria.area_del_triangulo(int(input("OPCION 2: CALCULA EL AREA DEL TRIANGULO:Ingrese el lado del triangulo:"))) #validad si el nro ingresado por teclado es <0
    print("el area del triangulo es:",are)


while (opc !=max):
    #IMPRECION DE MENU
    print("########  MENU  #########")
    print("1.AREA DEL TRAPECIO:     ")
    print("2.AREA DEL TRIANGULO:    ")
    print("3.SALIR:                 ")
    print("#########################")

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
