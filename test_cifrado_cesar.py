import cifrado_cesar2

encrypt2 = cifrado_cesar2.encription(2)
assert encrypt2("hola") == 'JQNC'

encrypt2, decrypt2 = cifrado_cesar2.par_encrypted(2)
assert encrypt2("hola") == 'JQNC'
assert decrypt2('JQNC') == "HOLA"

assert cifrado_cesar2.encrypt("hola, mundo",2) == "JQNC, ÑWOFQ"
assert cifrado_cesar2.decrypt("JQNC, ÑWOFQ",2) == 'HOLA, MUNDO'