alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def encrypt(message:str,distance:int):
    origin = 0
    steps = 0
    result = ""
    for letter in message.upper():
        if letter in alphabet:
            origin = alphabet.find(letter)
            steps = (origin + distance) % len(alphabet)
            result += alphabet[steps]
        else:
            result += letter
        
    return result

def encription(dist:int):
    def encrypted(message:str):
        return encrypt(message,dist)
    return encrypted

def par_encrypted(dist:int):
    def encrypted(message:str):
        return encrypt(message,dist)
    def decrypted(message:str):
        return encrypt(message,-dist)
    return encrypted,decrypted

encrypt2 = encription(2)
encrypt2, decrypt2 = par_encrypted(2)
assert encrypt2("hola") == 'JQNC'
assert decrypt2('JQNC') == "HOLA"

