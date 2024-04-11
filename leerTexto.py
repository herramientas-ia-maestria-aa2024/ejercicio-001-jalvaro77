"""
Leer informacion de un txt e imprimir cada liena

Autor: Juan Yupangui
Fecha: 09/04/2024
"""
# Abrir archivo modo lectura, con utf-8 para caracteres latinos
with open('informacion.txt', 'r', encoding='utf-8') as archivo:
    # leer lineas
    lineas = archivo.readlines()

# imprimir cada linea
for numero_linea, linea in enumerate(lineas, start=1):
    print(f'Línea {numero_linea}: {linea.strip()}')#impreme numero de lineas y texto de la linea.