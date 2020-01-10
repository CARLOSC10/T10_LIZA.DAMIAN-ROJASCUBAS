#menu5
import libreria

def agregarnotas():
    nota1=libreria.pedir_numero("ingrese nota1:",0,20)
    nota2=libreria.pedir_numero("ingrese nota2:",0,20)
    nota3=libreria.pedir_numero("ingrese nota3:",0,20)
    promedio=(nota1+nota2+nota3)/3
    if(promedio>=10.5):
        msj="APROBADO"
    else:
        msj="DESAPROBADO"
    contenido=str(nota1)+"-"+str(nota2)+"-"+str(nota3)+"-"+str(promedio)+"-"+msj+"\n"
    libreria.guardar_datos("promedio.txt", contenido, "a")
    print("DATOS DEL VOTADOR GUARDADOS")

def leerpromedio():
    # 1. Abrir el archivo promedio.txt y mostrar sus datos
    datos = libreria.obtener_datos_lista("promedio.txt")

    # 2. COmprobar si hay datos
    if ( datos != ""):
        for item in datos:
            nota1,nota2,nota3,promedio,msj=item.split("-")
            msg="SUS NOTAS: {}, {}, {}, SU PROMEDIO: {},Y SU CONDICION {}"
            nota1=nota1.replace("\n","")
            nota2=nota2.replace("\n","")
            nota3=nota3.replace("\n","")
            promedio=promedio.replace("\n","")
            msj=msj.replace("\n","")
            print(msg.format(nota1,nota2,nota3,promedio,msj))
        #fin_for
    else:
        print("Archivo sin datos")
#fin_def
opc=0
max=3
while(opc!=3):
    print("############ MENU #############")
    print("1.AGREGAR NOTAS               #")
    print("2.LEER NOTAS Y PROMEDIO       #")
    print("3.SALR                        #")
    print("###############################")
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    if(opc==1):
        agregarnotas()
    if(opc==2):
        leerpromedio()
    #fin_while
#fin_while
