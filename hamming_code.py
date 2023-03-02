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
def check(matrix):
    one_indices = []
    for i in range(len(matrix)):
        if matrix[i] == 1:
            one_indices.append(format(i, '04b'))
    xor = bin(int(one_indices[0], 2) ^ int(one_indices[1], 2))[2:].zfill(4)
    for i in range(2, len(one_indices)):
        xor = bin(int(xor, 2) ^ int(one_indices[i], 2))[2:].zfill(4)
    xor = int(xor, 2)
    return xor

'''
 Funcion que repara el bit con ruido
'''
def reparador(matrix, index):
    matrix[index] ^= 1


# correct = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1]
# incorrect = noise([1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1])
# correct = [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1]
# incorrect = noise([1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1])
# print(f"Correct one is: {correct}")
# print(f"Incorrect one is: {incorrect}")
# print(f"Check of correct is: {check(correct)}")
# print(f"Check of incorrect is: {check(incorrect)}")
#
# Ejercicios:
# bloque1 = [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0]
# print(check(bloque1))
# bloque2 = [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1]
# print(check(bloque2))
# BOB
# bloques = [[1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0],
#            [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# print(check(bloques[0]))
# print(check(bloques[1]))
# bloques = [[1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0],
#            [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
