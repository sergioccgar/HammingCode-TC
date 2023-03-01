import math
'''
 Módulo encargado de convertir una cadena dada a un arreglo de bits. Después organizará dichos
 bits en bloques de tamaño x dependiendo de los bits por matriz que tendremos. Notemos que los
 bits por matriz que tendremos son potencias de 2.
'''

POWERS = [0] + ([2**i for i in range(16)])

'''
 Función que, dada una cadena, devuelve otra cadena cuyos caracteres son 0s y 1s
 y cada grupo de 8, leyendo de izquierda a derecha, corresponde a cada caracter
 de la cadena.
'''
def string_to_binary(message):
    return ''.join(format(ord(i), '08b') for i in message)

'''
 Función que, dada una cadena de 0s y 1s, devuelve una lista que contiene
 tantos elementos como la longitud de la cadena recibida dividida entre 8.
 Dichos elementos son de tipo string y corresponden a un byte que representa
 un caracter del mensaje recibido en string_to_binary().
'''
def binary_string_to_list(message):
    binary_list = []
    for i in range(int(len(message)/8)):
        binary_list.append(message[i*8:(i*8)+8])
    return binary_list

'''
 Función que dada una cadena con un mensaje codificado en bits (la salida de
 string_to_binary()), devuelve una lista de números, a saber, 0s y 1s.
'''
def bits_string_to_bits_list(bits_string):
    bits_list = []
    for i in range(len(bits_string)):
        bits_list.append(int(bits_string[i]))
    return bits_list

'''
 Función que devuelve una lista de listas que representan matrices de
 2^n bits que contienen los bits de paridad y serán utilizadas en la 
 implementación del algoritmo de Hamming Code. El parámetro flag
 indica la potencia de 2 que representa el tamaño de los bloques/listas, 
 i.e., el número de bits que cada bloque/lista almacenará.
 Sabemos que cada matriz puede almacenar (2^n)-n-1 bits, pues esto
 considera que no podemos utilizar los bits de paridad para almacenar
 información. Para saber cuántas matrices necesitamos en total para
 almacenar m bits, calculamos ceil(m/((2^n)-n-1)); esto ya que al dividir
 el número de bits a almacenar entre el número de bits que una matriz puede
 guardar, nos devuelve el número de matrices necesarias para almacenarlos,
 dado que la división no siempre será entera, tomamos ceiling y los bits
 sobrantes los llenaremos con 0s.
'''
def bits_to_blocks(bits_list, flag):
    block_list = []
    parity_bits_indices = []

    # Obtenemos los índices de los bits de paridad.
    for i in range(flag+1):
        parity_bits_indices.append(POWERS[i])

    # Este ciclo genera una matriz de 2**flag elementos
    for i in range(math.ceil(len(bits_list)/((2**flag)-flag-1))):
        matrix = []
        for j in range(2**flag):   # Este loop inicializa los índices de paridad como 0
            if j in POWERS:
                matrix.append(0)
            else:                  # y agrega los bits de información en el resto.
                if not bits_list:  # si la lista de información se termina, llenamos el resto de la matriz con 0s.
                    matrix.append(0)
                else:
                    matrix.append(bits_list.pop(0))  # se agregan los bits de información a bits no de paridad.

        # Se calcula el valor de los bits de paridad.
        for index in parity_bits_indices:
            matrix[index] = calculate_parity(matrix, index)

        # Se agrega la matriz a la lista final.
        block_list.append(matrix)
    return block_list

'''
 Función que calcula el valor del bit de paridad. Recibe una matriz y el índice del bit
 de paridad actual, calcula los índices de los  bits de la matriz que debe revisar para
 determinar su valor de paridad y finalmente calcula el mismo. Para obtener los índices
 hace uso de la función auxiliar get_indices_to_check(), pasando la matriz actual, el
 índice de paridad y el salto es el log2(current)+1, pues esto nos indica qué número
 de bit de paridad estamos revisando (el primero, el segundo, el tercero, el cuarto;
 que corresponden al índice 1, 2, 4, 8, y así sucesivamente.
'''
def calculate_parity(matrix, current):
    if current == 0:
        return 0
    bit_indices = get_indices_to_check(matrix, current, int(math.log2(current) + 1))
    parity = 0
    for i in bit_indices:
        parity ^= matrix[i]
    return parity

'''
 Función que recibe una matriz, un índice current y un salto step. Devuelve los índices
 de la matriz que el bit de paridad con índice current revisará para obtener su valor
 de paridad. Si es el índice 1, sabemos que revisa uno y se salta uno, si el índice es
 2, revisa dos y se salta dos, si es 4, revisa 3 y se salta tres.
'''
def get_indices_to_check(matrix, current, step):
    indices = []
    i = current

    # Obtenemos los índices a revisar por el bit de paridad.
    while i < len(matrix):
        for j in range(step):
            if i+j >= len(matrix):  # No se agregan bits que no le corresponden revisar al bit de paridad actual.
                break
            indices.append(i+j)  # Agregamos todos los índices de los bits por revisar
        i += 2 * step  # Nos saltamos bits que no revisaremos
    return indices


# my_string = string_to_binary("Hallo Pichi -")
# list_of_bytes = binary_string_to_list(my_string)
# bits_list = bits_string_to_bits_list(my_string)
#
# print(POWERS)
# print(my_string)
# print(list_of_bytes)
# print(bits_list)
# print(len(bits_list))
# print(math.ceil(len(bits_list)/((2**4)-4-1)))
# print('\n'.join([str(x) for x in bits_to_blocks(bits_list, 4)]))
# print(bits_to_blocks(bits_list, 4))
# print(get_indices_to_check([0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1], 1, 1))
