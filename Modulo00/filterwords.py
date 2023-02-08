import sys

if len(sys.argv) != 3:
    print("ERROR")
    sys.exit()
elif sys.argv[1].isdigit() == True or sys.argv[2].isdigit() == False:
    print("ERROR2")
    sys.exit()
else:
    #Para no considerar caracteres especiales
    lista = sys.argv[1].split()
    lista2 = []
    for word in lista:
        word2 = []
        for c in word:
            if c.isalpha() == False:
                pass
            else:
                word2.append(c)
        lista2.append("".join(word2))
    #Para no considerar palabras que no sean del tamaño indicado
    for i in lista2:
        if len(i) <= int(sys.argv[2]):
            lista2.remove(i)
    print(lista2)




