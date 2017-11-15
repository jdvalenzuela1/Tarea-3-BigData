from lightning import Lightning
import math
from numpy import random

lgn = Lightning(host='http://public.lightning-viz.org')
tarea_3 = open("tarea_3.csv", "r")

for line in  tarea_3:
    values = []
    titulo = ""
    line_splitted = line.split(';')
    n = 1
    for element in line_splitted:
        if n == 1:
            titulo = element
            n = 0
        else:
            print element
            if len(element) > 0:
                values.append(int(element))
    viz = lgn.histogram(values, zoom=False, description=("Categoria: "+ titulo))
    viz.open()
