#SUB MENU MENU 01
import libreria
apc=0
max=3

def subopcionA():
    print("su empresa es nacional")
def subopcionB():
    print("la empresa es privada")


def opcionA():
    a=libreria.validar_nombre(input("ingrese el nombre de la empresa:"))
    opc=0
    max=3
    while (opc!=max):
        print("#############################")
        print("#####EMPRESA###########")
        print("1.NACIONAL")
        print("2.PRIVADA")
        print("3.SALIR")
        print("###########")
        opc=libreria.pedir_entero("INGRESE LA OPCION:",1,3)

        if(opc==1):
            subopcionA()
        if(opc==2):
            subopcionB()
        #fin_submenu
    print("el nombre del usuario es:"+str(a))

def opcionB():
    b=libreria.nro_ruc_valido(input("ingrese el numero de ruc:"))
    print("el numero de ruc de la empresa es"+str(b))

while (opc != max):
    #IMPRECION DEL MENU
    print("############################")
    print("#####    INDECOPI###########")
    print("1.EMPRESA")
    print("2.numero de ruc")
    print("3.salir")
    print("#############")

    #ELECCION DE OPCIONES
    opc=libreria.pedir_entero("INGRESE LA OPCION:",1.3)

    #MAPEO DE LAS OPCIONES
    if(opc==1):
        opcionA()
    if(opc==2):
        opcionB()
    #fin_mapeo

#fin_while
print("Fin del menu")
