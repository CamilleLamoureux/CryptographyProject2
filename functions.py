def keyOK(n,offset):
    maxOffset = 2*n - 3
    return True if n >= 2 and 0<=offset<=maxOffset else False


def computeCoordonates(n,l,offset):
    pass


def init(n,l,coordinates):
    pass


def fullDictionaryCipher(text,l,coordinates,dictionary):
    for i in range(l):
        dictionary[coordinates[i]] = text[i]


def fullDictionaryDecipher(text,n,l,coordinates,dictionary):
    pass


def fullDictionary(text,n,l,coordinates,dictionary,cipher):
    fullDictionaryCipher(text, l, coordinates, dictionary) if cipher == True else fullDictionaryDecipher(text,n,l,coordinates,dictionary)


def displayDictionary(n,l,coordinates,dictionary):
    for line in range(n):
        for row in range(l):
            if (line, row) in dictionary:
                print(dictionary[(line, row)], end=" | ")
            else:
                print(" ", end=" | ")
        print("")


def dictionaryToStringCipher(n,l,coordinates,dictionary):
    pass

def dictionaryToStringDecipher(l,coordinates,dictionary):
    pass


def dictionaryToString(n,l,coordinates,dictionary):
    pass


def algorithm2(text,n,offset,cipher,display):
    result = []
    l = len(text)
    coordinates = computeCoordonates(n, l, offset)
    dictionary = init(n, l, coordinates)

    fullDictionary(text, n, l, coordinates, dictionary, cipher)

    # If we want to cipher
    if cipher == True:
        print("We want to cipher")
    # If we want to decipher
    else:
        print("We want to decipher")

    # If we want a display
    if display == True:
        print("We want a display")
    # If we don't want a display
    else:
        print("We don't want a display")

    return result