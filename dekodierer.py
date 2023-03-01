from codeumsetzer import binary_string_to_list
'''
 Módulo encargado de convertir una lista de números enteros y devolver una cadena.
'''

'''
 Función que recibe una lista de enteros, que son todos 0s y 1s y devuelve una cadena
 que es el mensaje codificado en los bytes que son grupos de 8 enteros de la lista. 
'''
def dekodieren(liste):
    long_string = ""  # Cadena de 0s y 1s
    for bit in liste:
        long_string += str(bit)
    # print(long_string)
    # Usamos la función implementada en codeumsetzer.py para tener una lista de cadenas
    # donde cada cadena tiene 8 caracteres y dichos caracteres representan un byte, que
    # a su vez, representa un símbolo en UTF-8.
    byte_list = binary_string_to_list(long_string)
    # print(byte_list)
    decimal_list = []  # Convertimos las cadenas de bytes a enteros en base 10.
    for byte in byte_list:
        decimal_list.append(int(byte, 2))
    # print(decimal_list)
    nachricht = ""  # Nachricht es mensaje en alemán.
    for decimal in decimal_list:
        nachricht += chr(decimal)
    return nachricht


raw_list = [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1]
print(dekodieren(raw_list))
