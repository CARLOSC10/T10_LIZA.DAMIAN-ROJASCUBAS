import libreria
#MENU
#datos registrados en una votacion

#fucion
def agregarVotador():
    nombre=libreria.pedir_nombre("ingrese su nombre:")
    nro_dni=libreria.pedir_dni("ingrese numero Dni:")
    estado_civil=libreria.pedir_estado("ingrese su estado civil:")
    contenido=nombre+"-"+str(nro_dni)+"-"+estado_civil+"\n"
    libreria.guardar_datos("urna.txt", contenido, "a")
    print("DATOS DEL VOTADOR GUARDADOS")
def leerVotador():
    # 1. Abrir el archivo urna.txt y mostrar sus datos
    datos = libreria.obtener_datos_lista("urna.txt")

    # 2. COmprobar si hay datos
    if ( datos != ""):
        for item in datos:
            nombre,nro_dni,estado_civil=item.split("-")
            msg="EL NOMBRE DEL VOTADOR ES:{} ,CON NÚMERO DE DNI: {}, Y CON ESTADO CIVIL: {}"
            nombre=nombre.replace("\n","")
            nro_dni=nro_dni.replace("\n","")
            estado_civil=estado_civil.replace("\n","")
            print(msg.format(nombre,nro_dni,estado_civil))
        #fin_for
    else:
        print("Archivo sin datos")
#fin_def

opc=0
max=3
while(opc!=3):
    print("############ MENU #############")
    print("1.AGREGAR VOTADOR             #")
    print("2.LEER VOTADORES              #")
    print("3.SALR                        #")
    print("###############################")
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    if(opc==1):
        agregarVotador()
    if(opc==2):
        leerVotador()
    #fin_while
#fin_while
