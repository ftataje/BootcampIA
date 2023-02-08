import sys
import time

def ft_progress(listy2):
    length = len(listy2)  # largo de la lista
    for i in range(length): 
        percent = i / length # porcentaje de la lista (0 to 1)
        progress = int(percent * 100) # progress in percent (0 to 100)
        bar = int(percent * 20) # progress in bar (0 to 20)
        print("\rETA: [{}{}] {}%".format("=" * bar, " " * (20 - bar), progress), end="") 
        #\r para que sobreescriba en la misma linea
        # end="" para evitar el salto de linea al final del loop y se sobreescriba
        yield listy2[i] # yield para mantener el estado de la funcion

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)
