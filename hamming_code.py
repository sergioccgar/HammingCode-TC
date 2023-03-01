import random
'''
 Módulo encargado de simular ruido a una transmisión de información y detectar errores y corregirlos.
'''

'''
 Función que simula ruido y modifica un bit de una matriz con información.
'''
def noise(matrix):
    i = random.randint(0, len(matrix)-1)
    matrix[i] ^= 1
    return matrix

'''
 Función que devuelve el índice que ha sufrido cambios en una matriz determinada.
'''
# def check(matrix):