# I. Unidad 4 - Sesión 11 - Sorteo de Variables con distribucion arbitraria -  Ejercicio 11.1

# II. Trabajo Individual.

* Santiago Alaniz, CI 50826476, santiago.alaniz@fing.edu.uy

# III. Descripción del Problema

Resumir en un texto (de entre media y una carilla) los principales contenidos del paper de P. L'Ecuyer, "Software for uniform random number generation: distinguishing the good and the bad".

# IV. Resumen de la Solución

## Pregunta a) - Cual es el objetivo del trabajo?

El objetivo de este trabajo es presentar distintos mecanismos para validar la calidad de los generadores de numeros aleatorios. Para esto se presentan distintos criterios de calidad, diferentes familias de gneradores, luego, se presentan diversos generadores de programas comerciales / lenguaes de programacion y se los evalua con los criterios presentados.

## Pregunta b) - Que generadores de numeros aleatorios se presentan?

1.**Recurrencia Lineal:** Este es un tipo de generador de números aleatorios que utiliza una ecuación lineal para generar la próxima entrada en una secuencia. La ecuación toma la forma `x_i = (a * x_(i-1) + c) mod m`, donde `a`, `c` y `m` son constantes.

2.**Congruencial Lineal (LCG):** Estos son una clase de generadores de números pseudoaleatorios que operan al generar una secuencia de números a través de la siguiente fórmula recursiva: `X_(n+1) = (a*X_n + c) mod m`. Los LCG son rápidos y requieren muy poca memoria, lo que los hace adecuados para simulaciones donde se requiere una gran cantidad de números aleatorios.

4.**Generador Múltiple de Recurrencia (MRG):** Un tipo de generador de números aleatorios que combina las salidas de múltiples generadores de recurrencia lineal para producir una secuencia de números que tiene un período más largo y una calidad mejorada de aleatoriedad en comparación con los generadores individuales.

5.**Twisted Generalized Feedback:** Estos son una clase de generadores de números aleatorios que utilizan operaciones de bit para generar números. El más famoso de estos es el Mersenne Twister, que tiene un período extremadamente largo y pasa muchas pruebas de aleatoriedad.


### Generadores propuestos en el paper.

| Generador      | Clase del generador |
|----------------|---------------------|
| Java           | Recurrencia Lineal  |
| VB             | Congruencial Lineal (LCG) |
| Excel          | Congruencial Lineal (LCG) |
| LCG16807       | Congruencial Lineal (LCG) |
| MRG32k3a       | Generador Múltiple de Recurrencia (MRG) |
| MT19937        | Twisted Generalized Feedback Shift Register (TGFSR) |


-`Java`: La clase java.util.Random utiliza un generador de recurrencia lineal con longitud de periodo 2^48. Sin embargo, cada valor de salida se construye tomando dos valores sucesivos de la recurrencia lineal de la siguiente manera:

  ```
  xi+1 = (25214903917 * xi + 11) mod 2^48
  ui = (227 * floor(xi/2^22) + floor(xi+1/2^21)) / 2^53
  ```

-`Microsoft Visual Basic`: Es un generador congruencial lineal con longitud de período 2^24, definido por:
  ```
  xi = (1140671485 * xi-1 + 12820163) mod 2^24
  ui = xi / 2^24
  ```

-`Excel`: Es un generador congruencial lineal (LCG), excepto que su recurrencia, se implementa directamente para los ui en aritmética de punto flotante. La longitud de su período en realidad depende de la precisión numérica de los números de punto flotante utilizados para la implementación. Esto no se indica en la documentación y no está claro cuál es. Los autores utilizaron un archivo con numeros aleatorios generados por Excel.
  ```
  ui = (9821.0 * ui-1 + 0.211327) mod 1
  ```

-`LCG16807`: LCG16807 es un generador congruencial lineal (LCG). Tiene una longitud de período de 2^31 - 2 y fue propuesto originalmente por Lewis, Goodman y Miller en 1969. Este LCG ha sido ampliamente utilizado en muchas bibliotecas de software para estadísticas, simulación, optimización, etc., así como en bibliotecas de sistemas operativos.:

  ```
  xi = 16807xi-1 mod (2^31 - 1),
  ui = xi/(2^31 - 1),
  ```

-`MRG32k3a`: Un generador propuesto por el autor, comina dos MRGs de orden 3 y tiene periodo cercano a 2^191.

-`MT19937`: Generador a base de un primo de Mersenne con un periodo enorme de 2^199936 - 1.

# Cuales son los hallazgos mas importantes? Que conclusiones y recomendaciones se presentan?

El autor plantea dos tests para asegurar la calidad de estos generadores.

 - Collision Test: Es una prueba que busca determinar si dos o más números generados aleatoriamente son iguales o "colisionan". El test de colisión es especialmente útil para probar generadores de números pseudoaleatorios, ya que estos generadores utilizan algoritmos deterministas para generar números "aleatorios". Si el algoritmo no es lo suficientemente bueno, puedes terminar con una secuencia de números que parece aleatoria a primera vista

 - Birthday Test: Es una prueba estadistica que se basa en la paradoja del cumpleanos, problema clasico visto en los cursos introductorios de probabilidad y estadistica. En este contexto, se usa para saber si los numeros aleatorios estan demasiado agrupados o no. Porque, al igual que la paradoja de cumpleanos, es comun esperar que los numeros al azar (cumpleanos) se repitan con cierta frecuencia, pero si se repiten demasiado, es probable que no sean tan aleatorios. En el paper se utilizan diferentes variables de este test, como por ejemplo `Birthday Spacings Tests with t = 3, with the First 10 Bits Thrown Away`, esto para detectar patrones sutiles en los numeros generados.

 El hallazgo mas importante es que la mayoria de los generadores mencionados en la seccion anterior no pasan los tests descriptos anteriormente. El factor que suele ser determinante en el fallo del test es el periodo del generador a probar.

 El autor recomienda no utilizar los generadores de software comercial ni las librerias de RNG por defecto de los lenguajes de programacion si se esta buscando una buena calidad de aleatoriedad. En la actualidad, hay mejores herraminetas disponibles.

 En particular, el autor recomienda aplicar `MULTIPLE-STREAM PACKAGES`. Es una herramienta que proporciona múltiples flujos (threads) independientes de números pseudoaleatorios. Cada flujo puede ser utilizado en diferentes partes de una simulación, o en diferentes simulaciones, para asegurar que cada uno tiene su propio conjunto independiente de números aleatorios.

# V. Anexo

Bibliografia:

- [1] P. L'Ecuyer, "Software for uniform random number generation: distinguishing the good and the bad".
