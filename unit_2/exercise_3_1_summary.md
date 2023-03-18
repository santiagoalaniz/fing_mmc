# I. Unidad 2 - Sesion 3 - Ejercicio 3.1

# II. Trabajo individual.

Santiago Alaniz, CI 50826476, santiago.alaniz@fing.edu.uy

# III. Descripcion del Problema

Se desea estimar el volumen de una región R de [0, 1]^6 definida por todos los puntos de la hiper-esfera:

- Centro: (0.45, 0.5, 0.6, 0.6, 0.5, 0.45)
- Radio 0.35

Y que ademas, cumplen las siguientes restricciones lineales:
- 3x1 + 7x4 ≤ 5
- x3 + x4 ≤ 1
- x1 − x2 − x5 + x6 ≥ 0

# IV. Descripcion de la Solucion

La solución fue programada en **Python 3.11.2**, usando las siguientes librerías:

- datetime: para calcular los tiempos de ejecución.
- random: para generar el conjunto de replicación.
- sys: para obtener parametros de la linea de comandos.
- pdb: para debuggear el código. (no es necesario para la ejecución del programa)

La región a estimar se define como una hiper-esfera de radio 0.35 centrada en (0.45, 0.5, 0.6, 0.6, 0.5, 0.45) y las restricciones lineales, expresadas como una lista de funciones lambda.

El código genera puntos aleatorios en el espacio de seis dimensiones y cuenta cuántos puntos caen dentro de la región de interés. La fracción de puntos dentro de la región se utiliza para estimar el volumen de la región.

La función **montecarlo_simulation()** es el núcleo del algoritmo de Montecarlo. Toma como entrada el número de muestras a generar y devuelve el volumen estimado de la región y la varianza de la estimación.

La función **random_point()** genera un punto aleatorio en el espacio de seis dimensiones **R de [0, 1]^6**, mientras que **U_01()** devuelve un número aleatorio uniforme en el intervalo **[0,1]**.

La función **point_in_region()** verifica si un punto se encuentra dentro de la región de interés, primero evalua las restricciones lineales dadas. Luego, la función **point_in_sphere()** verifica si un punto se encuentra dentro de la hiper-esfera (esto siempre y cuando las restricciones lineales se cumplan, de otra manera el punto es descartado).

La función **main()** controla la ejecución principal del código, llamando a **montecarlo_simulation()** para dos tamaños de muestra diferentes (10,000 y 1,000,000) y mostrando los resultados.

El código también tiene algunas constantes y variables globales, como el número de semilla utilizado para el generador de números aleatorios, el número de muestras a generar, si se incluyen o no las restricciones lineales.

## Parte a)

Sobre la consistencia de los dos valores obtenidos, en la tabla (ver resultados computacionales) se puede apreciar que el valor de la varianza decrece en orden de magnitud a medida que aumenta el tamaño de la muestra. Esto es consistente con lo esperado, ya que el metodo converge a la solucion exacta a medida que aumenta el tamaño de la muestra.

## Parte b)

En esta parte se pide previamente calcular el volumen exacto de una hiperesfera de dimensión 6.

El algoritmo se aproxima al volumen exacto de una n-esfera de seis dimensiones (ver seccion resultados computacionales). Esto nos da una pauta general para algunas observaciones que se pueden hacer sobre el problema general (n-esfera de 6 dimensiones mas restricciones lineales):

- El volumen de la región de interés es menor que el volumen de la hiper-esfera de seis dimensiones.

- Esto se debe a que la región de interés tiene restricciones lineales que la limitan. En particula, podemos pensar cada restriccion lineal como un plano que corta la hiper-esfera, la region de interes es entonces la interseccion de todas las regiones en la hiperesfera.

Las bases/resultados teoricos que se utilizaron fueron los siguientes:

- [Metodos Montecarlo] https://en.wikipedia.org/wiki/Monte_Carlo_integration
- [Volumen de N-esfera] https://en.wikipedia.org/wiki/Volume_of_an_n-ball
- [Estmacion de Volumen con Metodos Monte Carlo] EVA del curso - Unidad 2 - Sesion 3.
- [Interseccion] https://es.wikipedia.org/wiki/Intersecci%C3%B3n_(geometr%C3%ADa)

# V. Resultados Computacionales

1. MacBook Air, Apple M1, 2020, 8GB RAM, ptython 3.11.2
2. Semilla: 50826476;
3. $ python3 exercise_3_1.py LINEAR (con restricciones lineales)
4. $ python3 exercise_3_1.py (sin restricciones lineales)

|    n    |   Vol_   |           Var          | Tiempo de cálculo | BOUNDARIES |
|:-------:|:--------:|:----------------------:|:-----------------:|:----------:|
| 10000   | 0.0004   | 3.998799879987999e-08  | 0:00:00.016453    | True       |
| 1000000 | 0.000303 | 3.0290849390849393e-10 | 0:00:01.287557    | True       |
|         |          |                        |                   |            |

|    n    |   Vol_  |           Var          | Tiempo de cálculo | BOUNDARIES |
|:-------:|:-------:|:----------------------:|:-----------------:|:----------:|
| 10000   | 0.0106  | 1.0488688868886888e-06 | 0:00:00.024314    | False      |
| 1000000 | 0.00952 | 9.42937902937903e-09   | 0:00:01.600797    | False      |

*Volumen 6-esfera, radio = 0.35* : **0.009499628763439**

# VI. Anexo

Consultar la carpeta ~/anexo por los logs, capturas, código de la solucion y demás archivos
de interés.
