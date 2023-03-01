from codeumsetzer import binary_string_to_list
from codeumsetzer import POWERS
'''
 Módulo encargado de convertir una lista de números enteros y devolver una cadena.
'''
'''
 Función que recibe una lista de matrices y obtiene la información de las mismas.
 Descarta la información no necesaria (los 0s agregados en la última matriz)
'''
def get_info(liste):
    info_bits = []
    for matrix in liste:
        for i in range(len(matrix)):
            if i == 0 or i in POWERS:
                continue
            info_bits.append(matrix[i])
    return info_bits
'''
 Función que recibe una lista de enteros, que son todos 0s y 1s y devuelve una cadena
 que es el mensaje codificado en los bytes que son grupos de 8 enteros de la lista. 
'''
def dekodieren(liste):
    long_string = ""  # Cadena de 0s y 1s
    for bit in liste:
        long_string += str(bit)
    byte_list = binary_string_to_list(long_string)  # Favor de leer documentación de esta función en codeumsetzer.py
    nachricht = ""  # Nachricht es mensaje en alemán.
    for byte in byte_list:
        nachricht += chr(int(byte, 2))
    return nachricht


# raw_list = [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1]
# print(dekodieren(raw_list))
# list_of_matrices = [[0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1], [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1], [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0]]
# info = get_info(list_of_matrices)
# print(info)
# print(f"{dekodieren(info)}{len(dekodieren(info))}")
