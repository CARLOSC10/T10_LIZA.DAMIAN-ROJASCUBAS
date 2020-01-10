#MENU

import libreria
opc=0  #ocpiones
max=3  #maximo de opciones

def opcionA():
    fre=libreria.frecuencia(int(input("OPCION 1: CALCULA LA FRECUENCIA:Ingrese el tiempo empleado para poder hallar la frecuencia:"))) #validad si el numero es <0
    print("la frecuencia es:",fre)
    print("")

def opcionB():
    den=libreria.densidad(int(input("OPCION 2: CALCULA LA DENSIDAD:Ingrese el volumen para poder hallar la densidad:"))) #validad si el nro ingresado por teclado es <0
    print("el area del triangulo es:",den)


while (opc !=max):
    #IMPRECION DE MENU
    print("########  MENU  #########")
    print("1.CALCULA LA FRECUENCIA: ")
    print("2.CALCULA LA DENSIDAD:    ")
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
