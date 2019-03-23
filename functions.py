 # Function that test if their are remaining spaces in the text
def noSpaceRemaining(text):
    return True if text.count(' ') == 0 else False


# Function that remove a space
def removeSpaces(text):
    while not noSpaceRemaining(text):
        text.remove(' ')


# Function that convert accent-letters to non-accent-letters
def removeAccents(text):
    accentsE = ['é', 'ẹ', 'è', 'ẻ', 'ẽ', 'ê', 'ế', 'ệ', 'ề', 'ể', 'ễ', 'ë']
    accentsA = ['á', 'ạ', 'à', 'ả', 'ã', 'ă', 'ắ', 'ặ', 'ằ', 'ẳ', 'ẵ', 'â', 'ấ', 'ậ', 'ầ', 'ẩ', 'ẫ', 'ä']
    accentsU = ['ú', 'ụ', 'ù', 'ủ', 'ũ', 'ư', 'ứ', 'ự', 'ừ', 'ử', 'ữ', 'ü']
    accentsI = ['í', 'ị', 'ì', 'ỉ', 'ĩ', 'ï']
    accentsY = ['ý', 'ỵ', 'ỳ', 'ỷ', 'ỹ', 'ÿ']
    accentsO = ['ó', 'ọ', 'ò', 'ỏ', 'õ', 'ô', 'ố', 'ộ', 'ồ', 'ỗ', 'ơ', 'ớ', 'ợ', 'ờ', 'ở', 'ỡ', 'ö']

    for i in range(len(text)):
        if text[i] == 'ç':
            text[i] = 'C'
        elif text[i] in accentsA:
            text[i] = 'A'
        elif text[i] in accentsE:
            text[i] = 'E'
        elif text[i] in accentsU:
            text[i] = 'U'
        elif text[i] in accentsI:
            text[i] = 'I'
        elif text[i] in accentsO:
            text[i] = 'O'
        elif text[i] in accentsY:
            text[i] = 'Y'


# Function that upper the text
def upper(text):
    for i in range(len(text)):
        text[i] = text[i].upper()


# Function that test if there is still punctuation signs
def noPuncSignRemaining(text):
    punctSigns = [',', '.', '?', '!', "'", '-', '_', ':', ';']
    for letter in text:
        if letter in punctSigns:
            return False
    return True


# Function that remove punctuations signs
def removePunctuationSigns(text):
    punctSigns = [',', '.', '?', '!', "'", '-', '_', ':', ';']
    while not noPuncSignRemaining(text):
        for element in punctSigns:
            if element in text:
                text.remove(element)


# Function that convert the givent text into a
def convertLetters(text):
    removeSpaces(text)
    removeAccents(text)
    removePunctuationSigns(text)
    upper(text)
    return text


# Function that tests if the given key is correct
def keyOK(n,offset):
    maxOffset = 2*n - 3
    return True if n >= 2 and 0<=offset<=maxOffset else False


# Function that computes all coordinates of the letters in the table in the right order
def computeCoordinates(n, l, offset):
    list_result = []
    i = offset
    j = 0
    direction = 1
    while j <= l:
        coord = (i, j)
        list_result.append(coord)
        print(coord)
        i += direction
        j += 1
        if i == n:
            direction = - 1
        elif i == 0:
            direction = 1
    print(list_result)
    return list_result


# Function that enters the coordinates the keys of a dictionary
def init(n, l, coordinates):
    dictionary = {}
    for value in coordinates:
        dictionary[value] = "None"
    return dictionary

# Function that enters in the dictionnary all the letters of the plain text
def fullDictionaryCipher(text,l,coordinates,dictionary):
    for i in range(l):
        dictionary[coordinates[i]] = text[i]


# Function that enters in the dictionnary all the letters of the cipher text
def fullDictionaryDecipher(text,n,l,coordinates,dictionary):
    for i in range(n):
        for coordinate in coordinates:
            if coordinate[0] == i:
                dictionary[coordinates] = text[0]
                del text[0]


# Function that runs either fullDictionaryDecipher or Cipher
def fullDictionary(text,n,l,coordinates,dictionary,cipher):
    fullDictionaryCipher(text, l, coordinates, dictionary) if cipher == True else fullDictionaryDecipher(text,n,l,coordinates,dictionary)


# Function that displays on the CLI the table with the letters
def displayDictionary(n,l,coordinates,dictionary):
    for line in range(n):
        for row in range(l):
            if (line, row) in dictionary:
                print(dictionary[(line, row)], end=" | ")
            else:
                print(' ', end=" | ")
        print('')


# Function that returns the cipher text by reading the dictionary
def first(elem):
    return elem[0]

def dictionaryToStringCipher(n,l,coordinates,dictionary):
    cipher = []
    liste = sorted(dictionary.items(), key=first)
    for element in liste:
        cipher.append(element[1])
    return cipher


# Function that returns the plain text by reading the dictionary
def dictionaryToStringDecipher(l, coordinates, dictionary):
    decipher = []
    for element in coordinates:
        decipher.append(dictionary[element])
    return decipher

# Function that runs either dictionaryToStringCipher or Decipher
def dictionaryToString(n,l,coordinates,dictionary):
    pass


# Main function that calls all the other function
def algorithm2(text,n,offset,cipher,display):

    result = []
    text = convertLetters(text)
    l = len(text)
    coordinates = computeCoordonates(n, l, offset)
    dictionary = init(n, l, coordinates)

    fullDictionary(text, n, l, coordinates, dictionary, cipher)

    dictionaryToString(n,l,coordinates,dictionary)

    # If we want a display
    if display == True:
        displayDictionary(n,l,coordinates,dictionary)

    return result