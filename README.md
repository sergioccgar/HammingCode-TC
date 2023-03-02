# Práctica 1: Hamming Code
## *Equipo: Avonlea*
### Integrantes: Sergio Medina Guzmán 314332428

## Para ejecutar:
1. Es necesario tener Python3.8 instalado
2. Abre una terminal en donde se encuentre main.py
3. Compila y ejecuta con
```
python main.py
```

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
su valor; calcula el logaritmo base dos del índice actual y le suma 1, esto
nos devuelve qué bit de paridad es con el que trabajará get_indices_to_check();
es decir, si el bit de paridad es el 1, su índice en la matriz es 1, si es el 2
, su índice en la matriz es 2, si es el 3, su índice es el 4, si es el 4, su índice
es el 8, y así sucesivamente. De esta manera, mientras que calculate_parity() recibe
EL ÍNDICE DEL BIT DE PARIDAD, get_indices_to_check() recibe QUÉ NUMERO DE BIT ES, si
el primero, el segundo, el tercero, etc.
La paridad se inicializa como 0 y por cada bit que revisa, se 
ejecuta la operación XOR con el operador ^=, finalmente, revisa el número de
1s en la matriz, si es par, el bit de paridad total será 0. Si es impar,
el bit de paridad total será 1.
Nota, la forma en que se calcula la paridad, en esta implementación, es que el bit de paridad n revisa
los bits cuyo índice en la matriz al representarse en binario, tienen un 1
en la posición n. Esto es, el bit de paridad 1 revisa los bits cuyos índices
tienen un 1 en la posición menos significativa de su representación en binario.
Esto es, revisa los números impares.
Esto es consistente con las columnas/filas que el bit de paridad revisa visto
en las ayudantías. Se generaliza de esta manera para poder tener matrices de
2^n bits con n>4.
El bit de paridad 2, revisa los bits cuyos índices tienen un 1 en la segunda posición
de su representación en binario.
Esto es, revisa los bits cuyos índices en la matriz son de la forma ...xx1x, donde los
puntos y las x's representan bits del índice. Por ejemplo, este bit de paridad 
revisará los bits cuyos índices en binario son 10, 11, 110, 111, 1010, 1011, 1110 y 1111
es decir, revisará los bits cuyo índice en la matriz es 2, 3, 6, 7, 10, 11, 14, 15, etc.

Finalmente (ay), la función get_indices_to_check() recibe una matriz,
el índice del bit de paridad actual y el salto que va a tener en sus
revisiones. ¡CORREGIMOS ESTO!

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

Cabe mencionar que tanto codeumsetzer.py como dekodierer.py funcionan con
matrices con 2^n bits con n > 4. Con... un ligero detalle: dekodierer
parece agregar información que no existía antes en el mensaje original
cuando la matriz es demasiado grande... con n = 7 ocurrió. Igualmente, faltó
agregar el cálculo del bit de paridad total.

¡Ya hay una idea de cómo evitar que se agregue información que no existía antes!
Habrá que destinar una cierta cantidad de bits que permita almacenar la longitud
del mensaje original. De esta manera sabremos en qué momento dejar de recuperar
información de las matrices.

Ahora, con hamming_code.py, agregamos la función noise() que recibe una matriz
e invierte un índice de la misma al azar.

Pasamos a implementar la función check(). Recibimos una matriz. Obtenemos todos
los índices cuyos valores sean un 1, convertimos esos índices a binario y
aplicamos la función XOR a todo. Si hubo ruido, el resultado final no será
conformado únicamente por ceros, sino que será la representación en binario
del índice que tuvo ruido.

Bueno, encontramos problemas con la función check, ya que en matrices aparentemente
correctas indicaba que había un índice con ruido. ¿Qué pasó? Estábamos calculando
mal los bits que cada bit de paridad revisa. Corregimos las funciones:
calculate_parity()
get_indices_to_check()
En codeumsetzer.py

Antes de encontrar y trabajar con estos problemas, implementamos la función reparador()
que recibe una matriz y el índice del bit con ruido para corregirlo.

A lo largo de estas implementaciones, se programó el módulo main. Se escribieron
algunas pruebas para verificar el correcto trabajo de todos los módulos.

Procedemos a comentar dichas pruebas (dejamos las pruebas comentadas en cada módulo
en caso de querer probar y jugar nuevamente con ellas).

Ahora, escribimos el programa en main con el cual interactuará el usuario.
¡Listo! El main y la ejecución del programa son de la siguiente manera:

Recibes un saludo.
Se te solicita ingresar el mensaje que pondrá a prueba el programa.
Se te solicita ingresar un entero n que determinará que cada bloque hamming tendrá
2^n elementos con n >= 4.
Se muestran las matrices en las que el mensaje se codificó.
Clip cinemático para agregar drama
Se recibe el mensaje con errores (o sin errores)
Se muestran las matrices recibidas después del ruido.
Más clip cinemático para acumular tensión.
Se indica qué bits en cada matriz son los bits con ruido.
Se corrigen y se muestra el mensaje original.
Pichi se despide (¿Apoco trabaja aquí?)

### Conclusiones

Estamos cansados. Fue muy divertido y aprendí muchas cosas sobre python. Ya teníamos un poco
de experiencia programando en este lenguaje así que lo que ocupó más tiempo fue consultar
documentación en funciones del mismo o cómo hacer una u otra cosa. Se pueden generar matrices
de tamaño hasta 2^16.

Aunque la práctica no fue difícil per se, sí creo que fue demasiada "talacha". Creo que puedo
mejorar en mi familiarización con el lenguaje para tener aún más herramientas y saber qué
puedo hacer y cómo hacerlo.

# Preguntas.

1. Del bloque 1. Obtenemos los índices de los bits con 1s: 1, 5, 6, 13 y 14. En binario son
0001, 0101, 0110, 1101, 1110. Hacemos XOR con cada índice y obtenemos 0001. El mensaje es incorrecto
y el bit con ruido es el bit con índice 0. Aunque realmente esto no modificará la información
guardada en el bloque, pues se alteró el bit de paridad total.
Se puede comprobar esta respuesta en el código comentado en hamming_code.py, hasta abajo,
en la parte "Ejercicios."
2. Los índices de los bits con 1s son 0, 2, 4, 5, 7, 8, 13, 14, 15. En binario son 
0000, 0010, 0100, 0101, 0111, 1000, 1101, 1110, 1111, al aplicar XOR tenemos que
el bit modificado es el 0. Se puede comprobar en la misma sección en hamming_code.py
3. Bob.
Bob recibió ¹. Tenemos lo siguiente en la consola de python:
```
a = "10111001"
b = "10001000"
a = chr(int(a, 2))
b = chr(int(b, 2))
a
'¹'
b
'\x88'
```
Para recibir "XD" debería cambiar sus bloques por los siguientes:
```
 Bloque A
 0, 1, 0, 0,
 1, 1, 0, 1,
 0, 1, 0, 0,
 0, 0, 1, 0
 Bloque B
 1, 0, 1, 0,
 1, 0, 1, 0,
 0, 0, 0, 0,
 0, 0, 0, 0 
```
4. 00110001110 Escribimos los primeros 11 bits en un bloque escribiendolos
en los bits que NO son destinados a los de paridad e iniciamos los bits de paridad como x.
```
Bloque
xxx0
x011
x000
1110
```
El bit de paridad 1 revisa los bits de la columna 2 y 4. Hay dos unos, por lo que será 0
El bit de paridad 2 revisa los bits de las columnas 3 y 4. Hay tres unos, por lo que será 1
El bit de paridad 3 (el índice 4) revisa los bits de las filas 2 y 4. Hay cinco unos, por lo que será 1
El bit de paridad 4 (el índice 8) revisa los bits de las filas 3 y 4. Hay tres unos, por lo que será 1.
```
Bloque
x010
1011
1000
1110
```
Finalmente, tenemos 8 1s, por lo que el bit de paridad total será 0. Tenemos entonces.
```
Bloque
0010
1011
1000
1110
```
Podemos comprobar la respuesta en el código comentado en la sección de ejercicios en 
codeumsetzer.py
5. 5 medios en los cuales se transfiere la información por bits
- Bluetooth. Cada bit se representa mediante una variación en la frecuencia de la señal de radio que se envía y se recibe entre los dispositivos.
- Tarjetas SD. Cada bit se representa mediante una variación en el voltaje de la señal eléctrica que se transmite a través de los contactos metálicos de la tarjeta.
- Cable de cobre. La información se transmite en forma de señales eléctricas y cada bit se representa mediante una variación en la intensidad o voltaje de la señal.
- Redes como 4G y 5G. Cada bit se representa mediante una variación en la frecuencia de la señal de radio que se envía y se recibe entre el dispositivo móvil y la antena de la red.
- Wi-Fi. Cada bit se representa mediante una variación en la frecuencia de la señal de radio que se envía y se recibe entre el dispositivo y el punto de acceso Wi-Fi.
## Puntos extra
- Crea un envío de mensajes utilizando Sockets en lugar de utilizar una variable, donde tanto servidor
como cliente puedan corregir el mensaje automáticamente.
- Desarrolla el ruido para que aleatoriamente pueda tener 0, 1 o 2 errores (máximo) y que sea capaz de
detectar si no hay error, hay 1 (este sí es obligatorio) o si hay 2 errores (aunque no se sepa cuales bits)
- Modifica el algoritmo para bloques de 256 bits(16 x 16) para que contenga más información por
bloque.

### Puntos extra entregados. 
- Modifica el algoritmo para bloques de 256 bits(16 x 16) para que contenga más información por
bloque.

Nota. Desde el principio se construyó el algoritmo para bloques de hasta 256 bits.
