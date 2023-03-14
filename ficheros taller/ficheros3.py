with open("Archivo3.txt","r") as readfile:
    lineas = readfile.readline()
    nombre = []
    edad = []
    sexo= []
    fechanac=[]
    estatura=[]
    for c_linea in readfile:
        renglon=c_linea.split(",")
        nombre.append(renglon[0])
        edad.append(renglon[1])
        sexo.append(renglon[2])
        fechanac.append(renglon[3])
        estatura.append(renglon[4])
print(nombre)
print(edad)
print(sexo)
print(fechanac)
print(estatura)