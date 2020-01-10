
#FUNCION QUE VALIDA SI ES UN NOMBRE DE UNA PERSONA
nombre=""
def validar_nombre(nombre):
    if(isinstance(nombre,str)):
        if(len(nombre)>=3):
            for item in nombre:
                if(item.isalpha()==False and item.isspace()==False):
                    return False
                #fin_if
            return True
            #fin_for
        else:
            return False
        #fin_if
    else:
        return False
    #fin_if
#fin_def


#FUNCION QUE VALIDA LA EDAD DE UNA PERSONA HASTA LOS 100 AÑOS
#DECLARACION DE VARIABLE
edad=0
def pedir_edad(edad):
    edad_invalida=(edad<0 or edad>100)
    while(edad_invalida==True):
        edad=int(input("EDAD INVALIDA:Ingrese la edad correcta:"))
        edad_invalida=(edad<=0 or edad>100)
    #fin_while
    return edad
#fin_def


#FUNCION QUE VALIDA UN NRO DE DNI
#DECLARACION DE VARIABLE
nro_dni=""
def validar_dni(nro_dni):
    if(isinstance(nro_dni,str)):     #comprueba si nro_dni es una cadena
        if(len(nro_dni)==8):         #si la longitud del valor de nro_dni es igual 8 hacer:
            for dni in nro_dni:              #iterar nro_dni
                if dni.isdigit()==False:     #se comprueba si c es un caracter de numero
                    return False
            return True
        else:
            return False
    else:
        return False
#fin_def


#FUNCION QUE VALIDA UN NRO DE TELEFONO DE 9 DIJITOS
#DECLARACION DE VARIABLES
nro_telefono=""
def nro_celular_valido(nro_telefono):
    if(isinstance(nro_telefono,str)):
        if(len(nro_telefono)==9):
            for i in nro_telefono:
                if i.isdigit()==False:
                    return False
            return True
            #fin_for
        else:
            return False
    else:
        return False
#fin_def





#FUNCION QUE VALIDA EL SEXO DE UNA PERSONA
#DECLARACION DE VARIABLES

sexo,sexo_invalido="",False
def pedir_sexo(sexo):
    sexo=sexo.upper()
    sexo_invalido=(sexo!="HOMBRE" and sexo!="MUJER")
    while(sexo_invalido==True):
        print("SEXO INVÁLIDO")
        sexo=input("ingrese sexo:")
        sexo=sexo.upper()
        sexo_invalido=(sexo!="HOMBRE" and sexo!="MUJER")
    #fin_while
    return sexo
#fin_def


#FUNCION PARA HALLAR LA DISTANCIA DE UN CARRO
#DECLARACION DE VARIABLES
velocidad=0
#FUNCION QUE VALIDAD LA VELOCIDAD
def distancia(velocidad):
    velocidad_invalida=(velocidad <=0)
    while(velocidad_invalida == True):
        velocidad=int(input("VELOCIDAD INCORRECTA:ingrese nuevamente la velocidad correcta:"))
        velocidad_invalida=(velocidad <=0)
    #fin_while
    dis=velocidad*2
    return dis
#fin_def


#FUNCION PARA HALLAR LA VELOCIDAD TANGENCIAL
#DECLARACION DE VARIABLES
radio=0.0
#FUNCION QUE VALIDAD EL RADIO
def velocidad_tangencial(radio):
    radio_invalida=(radio<=0)
    while(radio_invalida==True):
        radio=int(input("VALOR DEL RADIO INVALIDAD:ingrese nuevamente el valor del radio correcta:"))
        radio_invalida=(radio<=0)
    #fin_while
    velo_tang=4*radio
    return velo_tang
#fin_def


#FUNCION PARA HALLAR EL AREA DEL TRIANGULO EQUILATERO
#DECLARACION DE VARIABLE
lado=0.0
def area_del_triangulo(lado):
    lado_invalido=(lado<=0)
    while(lado_invalido==True):
        lado=float(input("LADO INCORRECTO:Ingrese el lado correcto del triangulo"))
        lado_invalido=(lado<=0)
    #fin_while
    area=((lado**2)*(3**(1/2)))/4
    return area
#fin_def


#FUNCION PARA HALLAR EL AREA DEL TRAPECIO
#DECLARACION DE VARIABLES
base_mayor=0
base_menor=20
altura=3
#FUNCION QUE VALIDAD LA BASE MAYOR
def area_trapecio(base_mayor):
    base_invalida=(base_mayor<=0)
    while(base_invalida==True):
        base_mayor=int(input("BASE INCORRECTA:ingrese nuevamente la base mayor del trapecio correcta:"))
        base_invalida=(base_mayor<=0)
    #fin_while
    area=((base_mayor+base_menor)/2)*altura
    return area
#fin_def


#FUNCION PARA HALLAR LA RESISTENCIA ELECTRICA
#DECLARACION DE VARIABLES
resistencia_inicial=7
variacion_de_temperatura=0.0
coeficiente_de_temperatura=2
#FUNCION QUE VALIDAD LA VARIACION DE TEMPERATURA
def resistencia_electrica(variacion_de_temperatura):
    variacion_invalida=(variacion_de_temperatura<=0)
    while(variacion_invalida==True):
        variacion_de_temperatura=int(input("VARIACION DE TEMPERATURA INVALIDAD:ingrese nuevamente la variacion de temperatura correcta:"))
        variacion_invalida=(variacion_de_temperatura<=0)
    #fin_while
    res=(resistencia_inicial+resistencia_inicial*coeficiente_de_temperatura*variacion_de_temperatura)
    return res
#fin_def


#FUNCION PARA HALLAR LA FRECUENCIA
#DECLARACION DE VARIABLES
nro_vueltas=50
tiempo_empleado=0.0
#FUNCION QUE VALIDAD EL TIEMPO EMPLEADO
def frecuencia(tiempo_empleado):
    tiempo_invalido=(tiempo_empleado<=0)
    while(tiempo_invalido==True):
        tiempo_empleado=int(input(" VALOR DEL TIEMPO INVALIDAD:ingrese nuevamente el valor del tiempo correcta:"))
        tiempo_invalido=(tiempo_empleado<=0)
    #fin_while
    frecu=nro_vueltas/tiempo_empleado
    return frecu
#fin_def


#FUNCION PARA HALLAR LA DENSIDAD
#DECLARACION DE VARIABLES
masa=3
volumen=0
#FUNCION QUE VALIDAD EL VOLUMEN
def densidad(volumen):
    volumen_invalido=(volumen <=0 or volumen >500)
    while(volumen_invalido == True):
        volumen=int(input("VOLUMEN INCORRECTA:ingrese nuevamente el volumen correcta:"))
        volumen_invalido=(volumen <=0 or volumen >500)
    #fin_while
    den=masa/volumen
    return den
#fin_def

#FUNCION PARA HALLAR LA PRECION HIDROSTATICA
#DECLARACION DE VARIABLES
densidad_del_liquido=52
gravedad=0.0
Altura=20
#FUNCION QUE VALIDAD LA GRAVEDAD
def precion_hidrostatica(gravedad):
    gravedad_invalidad=(gravedad<=0 or gravedad>=10)
    while(gravedad_invalidad==True):
        gravedad=float(input("GRAVEDAD INCORRECTA:Ingrese la gravedad correcta:"))
        gravedad_invalidad=(gravedad<=0 or gravedad>=10)
     #fin_while
    pre_hidros=densidad_del_liquido*gravedad*Altura
    return pre_hidros
#fin_def

#FUNCION QUE VALIDA UN NRO DE RUC
#DECLARACION DE VARIABLES
nro_ruc=""
def nro_ruc_valido(nro_ruc):
    if(isinstance(nro_ruc,str)):
        if(len(nro_ruc)==12):
            for i in nro_ruc:
                if i.isdigit()==False:
                    return False
            return True
            #fin_for
        else:
            return False
    else:
        return False
#fin_def


#FUNCION PARA HALLAR EL POTENCIA
#DECLARACION DE VARIABLES
trabajo=12
tiempo=0.0
#FUNCION QUE VALIDA EL TIEMPO
def potencia(tiempo):
    tiempo_invalido=(tiempo<0)
    while(tiempo_invalido==True):
        tiempo=float(input("TIEMPO CORRECTO:Ingrese el tiempo correcto >0:"))
        tiempo_invalido=(tiempo<0)
    #fin_while
    poten=trabajo/tiempo
    return poten
#fin_def

def pedir_entero(msg,ri,rf):
    n=""
    while(validar_rango(n,ri,rf)==False):
        n=input(msg)
        if (n.isdigit()== True):
            n=int(n)
    #fin_while
    return n
#fin_def

def validar_entero(n):
    if (isinstance(n,int)):
        return True
    else:
        return False
#fin_def

def validar_rango(n,ri,rf):
    if (validar_entero(n)==True):
        if (n>= ri and n<=rf):
            return True
        else:
            return False
    else:
        return False
#fin_def
