import os
import pathlib

nombre=input("Ingrese el nombre de un fichero")

if os.path.isfile(nombre)==True:
    os.remove(nombre)
else:
    print("El fichero no existe ")