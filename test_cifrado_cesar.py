import cifrado_cesar

def test_cifrado_simple_con_distancia():
    assert cifrado_cesar.encrypt("hola, mundo",2) == "JQNC, ÑWOFQ"
    assert cifrado_cesar.decrypt("JQNC, ÑWOFQ",2) == 'HOLA, MUNDO'

def test_cifrado_establecido_con_distancia_2():
    
    encrypt2 = cifrado_cesar.encription(2)
    assert encrypt2("hola") == 'JQNC'

def test_tupla_cifrado_descifrado_distancia_2():
    
    encrypt2, decrypt2 = cifrado_cesar.par_encrypted(2)
    assert encrypt2("hola") == 'JQNC'
    assert decrypt2('JQNC') == "HOLA"

    