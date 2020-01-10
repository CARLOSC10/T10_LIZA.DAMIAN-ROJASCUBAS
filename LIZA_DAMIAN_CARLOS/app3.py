#MENU DE UNA BOTICA
import libreria
opc=0  #ocpiones
max=3  #maximo de opciones

def opcionA():
    nom=libreria.validar_nombre(input("OPCION 1: INGRESE NOMBRE:")) #validad si es un nombre True y sino es False
    print("el nombre del cliente es:",nom)
    print("")

def opcionB():
    ed=libreria.pedir_edad(int(input("OPCION 2: INGRESE SU EDAD:"))) #validad la edad de una persona
    print("la edad del clientes es:",ed)
    print("")


while (opc !=max):
    #IMPRECION DE MENU
    print("########  MI FARMA  ########")
    print("1.NOMBRE:                   ")
    print("2.EDAD:                     ")
    print("3.SALIR:                    ")
    print("############################")

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
