#menu 2
import libreria


def agregarDatos():
    marca=libreria.pedir_marca("ingrese marca:")
    contenido=marca+"\n"
    libreria.guardar_datos("preferencias.txt", contenido, "a")
    print("DATOS GUARDADOS")

def leerDaros():
    # 1. Abrir el archivo preferencias.txt y mostrar sus datos
    datos = libreria.obtener_datos_lista("preferencias.txt")
    if(datos!=""):
        for item in datos:
            marca=item
            marca=marca.replace("\n","")
            marca=marca.upper()
            msg="SU GASEOSA PREFERIDA ES: {}"
            print(msg.format(marca))

    else:
        print("ARCHIVO SIN DATOS")
#fin_def

opc=0
max=3
while(opc!=3):
    print("")
    print("############ MENU ELECCIÓN DE MARCA DE GASEOSA PREFERIDA #############")
    print("#  SOLO DOS MARCAS COBOCIDAS: COCACOLA  O PEPSI                      #")
    print("1.AGREGAR DATOS                                                      #")
    print("2.LEER DATOS                                                         #")
    print("3.SALR                                                               #")
    print("######################################################################")
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    if(opc==1):
        agregarDatos()
    if(opc==2):
        leerDaros()
    #fin_while
#fin_while
