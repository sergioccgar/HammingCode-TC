# Práctica 1: Hamming Code
## *Equipo: Avonlea*
### Integrantes: Sergio Medina Guzmán 314332428

## Para ejecutar:
Esto lo llenaré al terminar la práctica.

### Introducción:

Hasta antes de las clases de Teoría de Códigos, había
dado por sentado —la expresión "to take for granted"
en inglés expresa de manera más elocuente que el español—
que enviar y recibir mensajes es tan sencillo como suena.
El nivel de abstracción que como usuario de dispositivos, 
e incluso como programador, he llegado a trabajar no me
daba pie a pensar o imaginar todo lo que hay por detrás
de lo que día a día manejamos: información.
A pesar de que sí llegó a cruzar por mi cabeza alguna
vez el "¿Cómo enviamos información y cómo esta llega intacta?",
no di realmente el paso a activamente saber cómo es que
eso se logra.
Gracias a las clases, he tenido un grato primer acercamiento
a la forma en que esto puede ser posible. En esta práctica
analizamos el algoritmo Hamming Code, que nos otorga una
herramienta increíblemente poderosa: el poder transmitir
y recibir mensajes autorrecuperables.

### Desarrollo:

Bueno, demasiada plática (¿escritura?). ¿Cómo vamos a empezar?
Echándole un ojito al esqueleto y ejemplo de lo que hemos de 
entregar, pienso en comenzar programando dos módulos: uno encargado
de codificar una cadena y devolver su equivalente en bits y otro
encargado de decodificar una secuencia de bits para recuperar
el mensaje codificado en él. Una vez tengamos estos dos módulos
procederemos al algoritmo y a la implementación estrellas de la
práctica: el Hamming Code.

El módulo que codificará las cadenas se llamará codeumsetzer, que 
es alemán para codificador, porque estudio alemán pero Ciencias
no me deja mucho tiempo para practicar así que de algún lado habrá
que sacar la práctica y el vocabulario. Análogamente, el módulo que
decodificará cadenas de unos se llamará dekodierer.

¡Hemos terminado el módulo codeumsetzer.py!
Describiré brevemente la implementación del mismo, pues para mayor
detalle se puede consultar la documentación en el código mismo.

Primero, análogo a la sugerencia del ayudante en el esqueleto, creamos
una constante que es una lista con las potencias de 2, comenzando desde
el 0, pero en esta implementación nos ahorramos el floor de math y
simplemente concatenamos a [0] las potencias.

Después, la función string_to_binary(). Recibe una cadena y concatena
lo siguiente: por cada char i en la cadena obtenida, obtiene ord(i) y
por medio de format(), con el especificador '08b', sabemos de 'b' que
convertirá el valor obtenido por ord(i) en binario, pero como tipo string
y de '08' que la cadena obtenida de esa conversión debe ser de longitud
8, por lo que normaliza las cadenas obtenidas agregando 0's a la parte 
izquierda. Después, devuelve todas estas cadenas concatenadas en una sola
que representa los bits que codifican el mensaje ingresado.

La función binary_string_to_list(), para devolver la lista indicada,
accede a las subcadenas que empiezan en el índice i*8 y paran justo
antes del índice (i*8)+8. Este tipo de corte nos permite obtener los
bytes en cadena que representan cada caracter del mensaje original.

La función bits_string_to_bits_list() (¿el programador no tuvo imaginación
para un nombre más corto?) itera por cada caracter de la cadena obtenida
en string_to_binary(), los convierte a int, ya que todos son 0s y 1s, y
los agrega a la lista bits_list, que al final devuelve.

La función bits_to_blocks() recibe una lista de ints, todos 0s y 1s, que
obtenemos de la función anterior y una bandera, que indica el número de bits
de paridad que tendrán las matrices que generaremos. Para obtener cuántos
bits de la lista que recibe puede almacenar en cada matriz, obtiene el número
de elementos de la misma (2**flag), y le resta el número de bits de paridad
(flag-1). Divide el número de bits totales en la lista recibida entre este número
y obtiene el número de matrices necesarias para almacenar todos los bits.

La función calculate_parity() asigna los valores de los bits de paridad. Si
el bit de paridad es el 0, mantiene su valor de 0. Si es mayor, invoca
a la función auxiliar get_indices_to_check() para saber, dado el índice
del bit de paridad, qué indices de la matriz deberá revisar para obtener
su valor. La paridad se inicializa como 0 y por cada bit que revisa, se 
ejecuta la operación XOR con el operador ^=.

Finalmente (ay), la función get_indices_to_check() recibe una matriz,
el índice del bit de paridad actual y el salto que va a tener en sus
revisiones.

Finalmente, el código inferior fue ayudando a ir probando cada una de las
funciones.


Ahora, procedamos a implementar el módulo dekodierer.py

Este módulo posee únicamente una función: dekodieren().
Es una función muy directa. Primero creamos una cadena vacía, luego,
por cada bit en la lista recibida, lo convertimos a cadena y lo
concatenamos con la cadena vacía. Partimos esta cadena en subcadenas
de longitud 8 con la función importada y cada subcadena forma ahora
parte de una lista que se almacena en byte_list.
Creamos una nueva cadena vacía y por cada cadena que representa un byte
en byte_list, convertimos esta cadena a un entero en base 10 con
int(byte, 2) y luego lo convertimos a char, para concatenarlo finalmente
con la cadena nachricht y luego devolver esta misma cadena.

Dicha cadena es el mensaje descodificado.

¡Yay! Ahora sólo falta el módulo hamming_code.py

(Bueno, antes de continuar, agregamos la función get_info() e dekodieren.py,
para obtener la información de una lista de matrices, descartando bits
de paridad y bits sin información al final del mensaje.)





