with open("Archivo4.txt","r") as readfile:
    lineas = readfile.readline()
    Departamentos = []
    Capitales = []
    for c_linea in readfile:
        renglon=c_linea.split(":")
        Departamentos.append(renglon[0])
        Capitales.append(renglon[1])
print(Departamentos)
print(Capitales)