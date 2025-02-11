import cifrado_cesar

encrypt2 = cifrado_cesar.encription(2)
assert encrypt2("hola") == 'JQNC'

encrypt2, decrypt2 = cifrado_cesar.par_encrypted(2)
assert encrypt2("hola") == 'JQNC'
assert decrypt2('JQNC') == "HOLA"

assert cifrado_cesar.encrypt("hola, mundo",2) == "JQNC, ÑWOFQ"
assert cifrado_cesar.decrypt("JQNC, ÑWOFQ",2) == 'HOLA, MUNDO'