#menu4
import libreria

def agregarpotencia():
    fuerza=libreria.pedir_numero_positivo("ingrese fuerza:")
    distancia=libreria.pedir_numero_positivo("ingrese distancia:")
    tiempo=libreria.pedir_numero_positivo("ingrese tiempo:")
    potencia=(fuerza*distancia)/tiempo
    contenido=str(fuerza)+"-"+str(distancia)+"-"+str(tiempo)+"-"+str(potencia)+"\n"
    libreria.guardar_datos("potencia.txt", contenido, "a")
    print("DATOS DEL VOTADOR GUARDADOS")

def leerpotencia():
    # 1. Abrir el archivo potencia.txt y mostrar sus datos
    datos = libreria.obtener_datos_lista("potencia.txt")
    # 2. comprobar si hay datos
    if ( datos != ""):
        for item in datos:
            fuerza,distancia,tiempo,potencia=item.split("-")
            msg="LA FUERZA ES:{} N , LA DISTANCIA: {}m, EL TIEMPO: {}s Y LA POTENCIA CALCULADA ES: {}vatios"
            fuerza=fuerza.replace("\n","")
            distancia=distancia.replace("\n","")
            tiempo=tiempo.replace("\n","")
            potencia=potencia.replace("\n","")
            print(msg.format(fuerza,distancia,tiempo,potencia))
        #fin_for
    else:
        print("Archivo sin datos")
#fin_def

opc=0
max=3
while(opc!=3):
    print("############ MENU #############")
    print("1.AGREGAR DATOS POTENCIA      #")
    print("2.MOSTRAR DATOS POTENCIA      #")
    print("3.SALR                        #")
    print("###############################")
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    if(opc==1):
        agregarpotencia()
    if(opc==2):
        leerpotencia()
    #fin_while
#fin_while
