#MENU DE UN RECIEN NACIDO

import libreria
opc=0  #ocpiones
max=3  #maximo de opciones

def opcionA():
    nom2=libreria.validar_nombre(input("OPCION 1: INGRESE SU NOMBRE PARA QUE PUEDA SUFRAGAR:")) #validad si es un nombre True y sino es False
    print("el nombre del cliente es:",nom2)
    print("")

def opcionB():
    a=libreria.pedir_sexo(input("OPCION 2: INGRESE EL SEXO DEL NIÑO:")) #validad si el sexo del niño es HOMBRE o MUJER
    print("el sexo del niño es:",a)


while (opc !=max):
    #IMPRECION DE MENU
    print("########  MENU  #########")
    print("1.NOMBRE:                ")
    print("2.SEXO:                   ")
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
