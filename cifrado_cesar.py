alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def find(letter: str):
    for index, character in enumerate(alphabet):
        if letter.upper() == character:
            return index

def encrypt(message:str,distance:int):
    
    result = ""
    
    for letter in message.upper():
        if letter in alphabet:
            origin = alphabet.find(letter)
            steps = (origin + distance) % len(alphabet)
            result += alphabet[steps]
        else:
            result += letter
        
    return result

def decrypt(message:str,distance:int):
    return encrypt(message,-distance)

assert encrypt("hola, mundo",2) == "JQNC, ÑWOFQ"
assert decrypt("JQNC, ÑWOFQ",2) == 'HOLA, MUNDO'