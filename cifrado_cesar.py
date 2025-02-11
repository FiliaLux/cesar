alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def find(letter: str):
    for index, character in enumerate(alphabet):
        if letter.upper() == character:
            return index

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

def decrypt(message:str,distance:int):
    return encrypt(message,-distance)

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