morse = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'Ñ':'--.--', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ' ':'/'}

import sys

lista = []
for i in sys.argv[1:]:
    lista.append(i)
    text = " ".join(lista)
    text = text.upper()
    morse_text = ''
    for letter in text:
        if letter in morse:
            morse_text += morse[letter] + ' '
        else:
            print("ERROR")
            sys.exit()
print(morse_text)

