def validar_entero(n):
    if(isinstance(n,bool)):
        return False
    if (isinstance(n, int)):
        return True
    else:
        return False

def validar_rango(n, ri, rf):
    if ( validar_entero(n) == True):
        if (n >= ri and n <= rf):
            return True
        else:
            return False
    else:
        return False

def pedir_numero(msg, ri, rf):
    n=""
    while( validar_rango(n, ri, rf) == False):
       n=input(msg)
       if ( n.isdigit() == True):
           n = int(n)
    #fin_while
    return n
#fin_pedir_numero

def validar_nombre(nombre):
    if(isinstance(nombre,bool)):
        return False
    if ( isinstance(nombre, str)):
        if (len(nombre) >= 3):
            if(nombre.isdigit()!=True):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
#fin_def

def pedir_nombre(msg):
    nombre=""
    while ( validar_nombre(nombre) == False ):
        nombre=input(msg)
    #fin_while
    return nombre
#fin_pedir_nombre

def validar_dni(nro_dni):
    if(isinstance(nro_dni,str)):
        if(len(nro_dni)==8):
            for item in nro_dni:
                if item.isdigit()==False:
                    return False
            else:
                return True
            #fin_for
        else:
            return False
        #fin_if
    else:
        return False
    #fin_if
#fin_def
def pedir_dni(msg):
    nro_dni=1
    while(validar_dni(nro_dni)==False):
        nro_dni=input(msg)
    #fin_while
    return nro_dni
#fin_def
def validar_estado(estado_civil):
    if(isinstance(estado_civil,str)):
        estado_civil=estado_civil.upper()
        if(estado_civil=="SOLTERO" or estado_civil=="CASADO"):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_estado(msg):
    estado_civil=""
    while(validar_estado(estado_civil)==False):
        estado_civil=input(msg)
    #fin_def
    return estado_civil
#fin_estado


def guardar_datos(nombre_archivo, contenido, modo):
    archivo=open(nombre_archivo, modo)
    archivo.write(contenido)
    archivo.close()

def obtener_datos(nombre_archivo):
    archivo=open(nombre_archivo)
    contenido = archivo.read()
    archivo.close()
    return contenido

def validar_marca(marca):
    if(isinstance(marca,str)):
        marca=marca.upper()
        if(marca=="COCACOLA" or marca=="PEPSI"):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_marca(msg):
    marca=""
    while(validar_marca(marca)==False):
        marca=input(msg)
    #fin_def
    return marca
#fin_estado


def validar_apellidos(apellidos):
    if(isinstance(apellidos,str)):
        #.los apellidos deben ser 2
         apellidos=apellidos.split(" ")
         if(len(apellidos)!=2):
             return False
         #.apellidos deben ser letras
         apellido1=apellidos[0]
         apellido2=apellidos[1]
         if(apellido1.isalpha()==False or apellido2.isalpha()==False):
             return False
         if (len(apellido1)<3 or len(apellido2)<3):
             return False
         #si llego hasta aqui es por que es un apellido valido
         return True
    else:
        return False
#fin_def

def pedir_apellidos(msg):
    apellidos=""
    while(validar_apellidos(apellidos)==False):
        apellidos=input(msg)
    #fin_while
    return apellidos
#fin_def

def validar_telefono(telefono):
    if(isinstance(telefono,int)):
        if(len(str(telefono))==9):
            return True

        else:
            return False
    else:
        return False
#fin_def
def pedir_telefono(msg):
    telefono=15
    while(validar_telefono(telefono)==False):
        telefono=int(input(msg))
    #fin_while
    return telefono
#fin_def

def validar_correo(correo):
      if(isinstance(correo,str)):
          #.ejemplo de como debe ser un correo gmail: "palabra(puede incluir numero)@gmail.com"
          correo=correo.split("@")
          if ( len(correo) !=2):
            return False
          palabra_antes=correo[0]
          palabra_despues=correo[1]
          #.comprobar si la palabra antes del "@" es alfanumerica
          if(palabra_antes.isalnum()==False):
              return False
          #.comparar la palabra despues del "@" con "gmail.com" (la la variable: palabra despues, debe ser estrictamente en minusculas e igual a la cadena comparada; no debe utilizarse conversion a minisculas de cadena)
          if(palabra_despues!="gmail.com"):
              return False

          return True
      else:
          return False
#fin_def
def pedir_correo(msg):
    correo=""
    while(validar_correo(correo)==False):
        correo=input(msg)
    #fin_while
    return correo
#fin_def

def validar_contrasena(contrasena):
    if(isinstance(contrasena,str)):
        #la contraseña para mas seguridad debe ser alfanumerica
        if(contrasena.isalnum()==True):
            if(len(contrasena)>=8):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
#fin_def

def pedir_contrasena(msg):
    contrasena=""
    while(validar_contrasena(contrasena)==False):
        contrasena=input(msg)
    #fin_while
    return contrasena
#fin_def

def validar_numero_positivo(numero):
    if(isinstance(numero,bool)):
        return False
    if(isinstance(numero,int) or isinstance(numero,float)):
        if(int(numero)>=0):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_numero_positivo(msg):
    numero=-5
    while(validar_numero_positivo(numero)==False):
        numero=input(msg)
        if(numero.isdigit()==True):
            numero=float(numero)
    #fin_while
    return numero
#fin_def
