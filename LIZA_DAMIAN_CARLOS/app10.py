#MENU

import libreria
opc=0  #ocpiones
max=3  #maximo de opciones

def opcionA():
    nom1=libreria.validar_nombre(input("OPCION 1: INGRESE SU NOMBRE PARA QUE PUEDA SUFRAGAR:")) #validad si es un nombre True y sino es False
    print("el nombre del cliente es:",nom1)
    print("")

def opcionB():
    ve=libreria.velocidad_tangencial(int(input("OPCION 2: CALCULA LA VELOCIDAD TANGENCIAL:Ingrese el radio dado:"))) #validad si el nro ingresado por teclado es <0
    print("la velocidad tangencial es:",ve)


while (opc !=max):
    #IMPRECION DE MENU
    print("########  MENU  #########")
    print("1.NOMBRE:                ")
    print("2.VELOCIDAD TANGENCIAL:  ")
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
