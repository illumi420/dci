import string

def getMessage():
    stringToEncrypt = input("Please Enter a message to encrypt: ")
    return stringToEncrypt


def getCipherKey():
    shiftAmount = int(input("Please enter a key (whole number from 1-25)"))
    return shiftAmount


def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + cipherKey
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage


def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * cipherKey
    return encryptMessage(message, decryptKey, alphabet)


def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

def CaesarCipherProgram():
    an_alphabet = string.ascii_uppercase
    print(f'Alphabet: {an_alphabet}')
    double_alphabet = getDoubleAlphabet(an_alphabet)
    print(f'Alphabet: {double_alphabet}')
    a_message = getMessage()
    print(a_message)
    a_cipher_key = getCipherKey()
    print(a_cipher_key)
    an_encrypted_msg = encryptMessage(a_message, a_cipher_key, an_alphabet)
    print(f"EncryptedMsg: {an_encrypted_msg}")

CaesarCipherProgram()    

