import libreria
assert (libreria.validar_nombre("CARLOS")==True)
assert (libreria.validar_nombre(7885)==False)
assert (libreria.validar_nombre("CARLOS78")==False)
assert (libreria.validar_nombre("frank")==True)
assert (libreria.validar_nombre(48)==False)

assert (libreria.validar_dni("123456789")==False)
assert (libreria.validar_dni("12345678")==True)
assert (libreria.validar_dni("485")==False)
assert (libreria.validar_dni("88")==False)
assert (libreria.validar_dni("75703748")==True)
assert (libreria.validar_dni("123456789")==False)

assert (libreria.nro_ruc_valido("123456789124")==True)
assert (libreria.nro_ruc_valido("1234567891")==False)
assert (libreria.nro_ruc_valido("723456789124")==True)
assert (libreria.nro_ruc_valido("72345")==False)

assert (libreria.nro_celular_valido("123456789")==True)
assert (libreria.nro_celular_valido("1234569")==False)
assert (libreria.nro_celular_valido("918161518")==True)




print("OK")
