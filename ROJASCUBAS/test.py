import libreria

assert (libreria.validar_entero("hola")==False)
assert (libreria.validar_entero(10.5)==False)
assert (libreria.validar_entero(True)==False)
assert (libreria.validar_entero(15)==True)

assert (libreria.validar_nombre("an")==False)
assert (libreria.validar_nombre(False)==False)
assert (libreria.validar_nombre("12345")==False)
assert (libreria.validar_nombre("ROSA")==True)

assert (libreria.validar_rango(15,14,13)==False)
assert (libreria.validar_rango("20",15,22)==False)
assert (libreria.validar_rango("hola",15,22)==False)
assert (libreria.validar_rango(False,14,22)==False)
assert (libreria.validar_rango(20,15,22)==True)

assert (libreria.validar_dni("123")==False)
assert (libreria.validar_dni(10.5)==False)
assert (libreria.validar_dni("abcdefghijedfs")==False)
assert (libreria.validar_dni("40124578")==True)
assert (libreria.validar_estado("12345")==False)
assert (libreria.validar_estado("ADRIAN")==False)
assert (libreria.validar_estado(True)==False)
assert (libreria.validar_estado("casado")==True)

assert (libreria.validar_marca("1452")==False)
assert (libreria.validar_marca(10.2)==False)
assert (libreria.validar_marca("")==False)
assert (libreria.validar_marca("COCACOLA")==True)
assert (libreria.validar_apellidos(1245)==False)
assert (libreria.validar_apellidos("da,cruz")==False)
assert (libreria.validar_apellidos("mundo")==False)
assert (libreria.validar_apellidos(True)==False)
assert (libreria.validar_apellidos("perez dias")==True)

assert (libreria.validar_telefono(1245)==False)
assert (libreria.validar_telefono(10.52)==False)
assert (libreria.validar_telefono(False)==False)
assert (libreria.validar_telefono("hola")==False)
assert (libreria.validar_telefono(971586579)==True)

assert (libreria.validar_correo("holabiembeido")==False)
assert (libreria.validar_correo(123456789)==False)
assert (libreria.validar_correo("elcapo12@GMAIL.COM")==False)
assert (libreria.validar_correo("juanperez15@gmail.com")==True)

assert (libreria.validar_contrasena("1")==False)
assert (libreria.validar_contrasena("holabiembenido1245")==True)
assert (libreria.validar_contrasena("15457")==False)



assert (libreria.validar_correo("tvjrkvncbccsx65x")==False)
assert (libreria.validar_correo(10.5)==False)
assert (libreria.validar_correo("rojascujose@GMAIL")==False)
assert (libreria.validar_correo("rojascujose@gmail.com")==True)
assert (libreria.validar_correo("rojascujose@UNPRG.edu.pe")==False)

assert (libreria.validar_numero_positivo("hola")==False)
assert (libreria.validar_numero_positivo(-15)==False)
assert (libreria.validar_numero_positivo(True)==False)
assert (libreria.validar_numero_positivo(10)==True)
assert (libreria.validar_numero_positivo(25.5)==True)
print("VALIDACIONES OK")
