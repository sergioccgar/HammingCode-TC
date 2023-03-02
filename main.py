import codeumsetzer as c
import dekodierer as d
import hamming_code as hc
import time
import random

print("¡Hola! Te damos la bienvenida a la Práctica 01 de laboratorio de Teoría de Códigos")
mensaje = input("Por favor, ingresa el mensaje que deseas probar: ")
opcion_valida = False
while not opcion_valida:
    try:
        tamanho_matriz = int(input("Por favor, ingresa un entero tal que las matrices que almacenarán"
                                   "el mensaje tengan un tamaño 2^n. "))
        opcion_valida = True
    except ValueError:
        print("Por favor, ingresa un entero.")
cadena_bits = c.bits_string_to_bits_list((c.string_to_binary(mensaje)))
bloques_hamming = c.bits_to_blocks(cadena_bits, tamanho_matriz)

print("El mensaje ha sido codificado en las siguientes matrices: ")
for matriz in bloques_hamming:
    print(matriz)

print("Enviando mensaje...")
for i in range(3):
    time.sleep(1)
    print("...")
print("¡Se ha detectado interferencia!")
for matriz in bloques_hamming:
    hc.noise(matriz)
print("¡Haz recibido el siguiente mensaje!")
print(d.dekodieren(d.get_info(bloques_hamming)))
print("Se encontraron las siguientes matrices: ")
for matriz in bloques_hamming:
    print(matriz)
print("Detectando errores...")
for i in range(3):
    time.sleep(1)
    print("...")
print("Corrigiendo errores...")
for i in range(3):
    time.sleep(1)
    if random.randint(1, 100) == 28:
        print("Pichi se está esforzando para reparar el mensaje...")
    print("...")
print("Se encontraron los siguientes errores: ")

for i in range(len(bloques_hamming)):
    print(f"El bit con ruido en la matriz {i} es {hc.check(bloques_hamming[i])}")

for i in range(len(bloques_hamming)):
    hc.reparador(bloques_hamming[i], hc.check(bloques_hamming[i]))
print("¡Listo! El mensaje corregido es: ")
print(d.dekodieren(d.get_info(bloques_hamming)))

print("Pichi dice '¡Adiós!'")


# my_message = "Hallo Pichi -"
# my_message_in_bits = c.bits_string_to_bits_list((c.string_to_binary(my_message)))
# my_message_in_blocks = c.bits_to_blocks(my_message_in_bits, 5)
# print(my_message_in_blocks)
# print(d.dekodieren(d.get_info(my_message_in_blocks)))
# print(f"El mensaje enviado fue {my_message}")
# print("---")
#
# print("Matrices sin ruido: ")
# for matrix in my_message_in_blocks:
#     print(matrix)
#
# noisy = []
# for matrix in my_message_in_blocks:
#     noisy.append(hc.noise(matrix))
#
# print("Matrices con ruido: ")
# for matrix in my_message_in_blocks:
#     print(matrix)
#
# print(f"El mensaje recibido fue: {d.dekodieren(d.get_info(my_message_in_blocks))}")
#
# for i in range(len(my_message_in_blocks)):
#     print(f"El bit con ruido en la matriz {i} es {hc.check(my_message_in_blocks[i])}")
#
# for i in range(len(my_message_in_blocks)):
#     hc.reparador(my_message_in_blocks[i], hc.check(my_message_in_blocks[i]))
#
# print(f"El mensaje reparado fue: {d.dekodieren(d.get_info(my_message_in_blocks))}")
