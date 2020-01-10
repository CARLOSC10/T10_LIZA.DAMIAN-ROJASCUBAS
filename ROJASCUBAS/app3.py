#menu3
import libreria

def agregarCuenta():
    nombre=libreria.pedir_nombre("ingrese su nombre:")
    apellidos=libreria.pedir_apellidos("ingrese apellidos:")
    contarsena=libreria.pedir_contrasena("ingrse su contrasena(mayor de 8 a mas acracteres y alfanumerica,para mas seguridad):")

    #formar un correo electronico si el usuario quiere(presione enter) sino presione cualquier letra
    dato_nombre=nombre.split(" ")
    dato_apellidos=apellidos.split(" ")
    correo=dato_apellidos[0]+dato_nombre[0]+"15@gmail.com"
    print("DESEA ESTE CORREO:",correo)
    print("PRESIONE ENTER SI LO QUIERE SINO PRESIONE OTRA TECLA")
    desicion=input("su decision:")
    if(desicion==""):
        correo=correo
    if(desicion!=""):
        print("UN CORREO VALIDO DE LA FORMA QUE EL ANTERIOR")
        correo=libreria.pedir_correo("ingrese su correo:")
    #fin_if

    contenido=nombre+"-"+apellidos+"-"+contarsena+"-"+correo+"\n"
    libreria.guardar_datos("cuenta.txt", contenido, "a")
    print("DATOS DEL VOTADOR GUARDADOS")

def leerCuenta():
    # 1. Abrir el archivo cuenta.txt y mostrar sus datos
    datos= libreria.obtener_datos_lista("cuenta.txt")
    if(datos!=" "):
        for item in datos:
            nombre,apellidos,contrasena,correo=item.split("-")
            nombre=nombre.replace("\n","")
            apellidos=apellidos.replace("\n","")
            contrasena=contrasena.replace("\n","")
            correo=correo.replace("\n","")
            msg="SU NOMBRE: {}, SUS APELLIDOS: {}, SU CONTRASEÑA: {}, Y SU CORREO \'gmail\': {} \n FELICIDADES! YA CUENTAS CON TU CORREO \'gmail\' "
            print(msg.format(nombre,apellidos,contrasena,correo))

    else:
        print("ARCHIVO SIN DATOS")
#fin_def


opc=0
max=5
while(opc!=3):
    print("")
    print("############ MENU #############")
    print("1.AGREGAR CUENTA              #")
    print("2.LEER CUENTA                 #")
    print("3.SALR                        #")
    print("###############################")
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    if(opc==1):
        agregarCuenta()
    if(opc==2):
        leerCuenta()
    #fin_while
#fin_while
