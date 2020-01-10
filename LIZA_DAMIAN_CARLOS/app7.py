#MENU

import libreria
opc=0  #ocpiones
max=3  #maximo de opciones

def opcionA():
    nom1=libreria.validar_nombre(input("OPCION 1: INGRESE SU NOMBRE:")) #validad si es un nombre True y sino es False
    print("el nombre del cliente es:",nom1)
    print("")

def opcionB():
    cel=libreria.nro_celular_valido(input("OPCION 2: SU NUMERO DE CELULAR ES:")) #validad si es un numero de dni valido de 8 digitos
    print("valida si es un numero de celular de 9 digitos:",cel)


while (opc !=max):
    #IMPRECION DE MENU
    print("########  MENU  #########")
    print("1.NOMBRE:                ")
    print("2.CELULAR:               ")
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

