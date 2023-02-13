
import random
import sys

def generator(text, sep=" ", option=None):
    """Option es un parámetro opcional, sep es el separador de palabras por defecto es un espacio en blanco."""
    if isinstance(text, str) == False:
        print("ERROR, text debe ser un string")
        sys.exit()
    if option == "shuffle":
        lista = []
        text = text.split(sep)
        while len(text) > 0:
            word = random.choice(text)
            lista.append(word)
            text.remove(word)
        for word in lista:
            yield word
    elif option == "unique":
        text = text.split(sep)
        for word in set(text):
            yield word
    elif option == "ordered":
        text = text.split(sep)
        text.sort()
        for word in text:
            yield word
    else:
        for word in text.split(sep):
            yield word
            
text = "Le Lorem Ipsum est simplement du faux texte."

for word in generator(text, sep=" "):
    print(word)
'''
for word in generator(text, sep=" ", option="shuffle"):
    print(word)

text = "Lorem Ipsum Lorem Ipsum"
for word in generator(text, sep=" ", option="unique"):
    print(word)

for word in generator(text, sep=" ", option="ordered"):
    print(word)
'''












