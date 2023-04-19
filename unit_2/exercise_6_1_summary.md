# I. Unidad 2 - Sesion 6 -  Ejercicio 6.1

# II. Trabajo Individual.

Santiago Alaniz, CI 50826476, santiago.alaniz@fing.edu.uy

# III. Descripcion del Problema

El problema trata sobre la estimación del volumen de una montaña que tiene forma de cono y está inscrita en una región cuadrada. La base de la montaña es circular y tiene un radio de 0.4 km, mientras que la altura de la montaña es de 8 km.

Para calcular el volumen total de la montaña, se utiliza una función matemática que describe la altura de cada punto en la montaña en términos de su ubicación dentro del círculo.

Se propone el uso del método de Monte Carlo para realizar la estimación del volumen, y se solicita calcular el número necesario de replicaciones para obtener un error absoluto deseado con un nivel de confianza del 95%. Finalmente, se pide estimar el volumen y su intervalo de confianza con el número de replicaciones calculado.

- **Parte a**: Escribir un programa para calcular el volumen por Monte Carlo. Realizar 10^6 replicaciones y estimar el valor de ζ y el error cometido (con nivel de confianza 0.95), utilizando como criterio la aproximación normal.

- **Parte b**: En base al valor estimado en la parte a, calcular el número de replicaciones necesario para obtener un error absoluto menor a 10^-3 (con nivel de confianza 0.95).

- **Parte c**: Realizar esa cantidad de replicaciones y estimar ζ y su intervalo de confianza

# IV. Descripcion de la Solucion

Este código en Python utiliza el método de Monte Carlo para estimar la integral de una función en un dominio específico. El programa calcula la integral de la función en el dominio del cono utilizando el método de Monte Carlo y ajusta el número de réplicas para lograr el error máximo permitido.

La solución fue programada en **Python 3.11.2**, usando las siguientes librerías:
- **random**, para generar números aleatorios.
- **datetime**, para medir el tiempo de ejecución.
- **math**, para operaciones matemáticas como raíz cuadrada.
- **scipy.stats**, para calcular percentiles de la distribución normal.
- **pdb**, un módulo de depuración (no se utiliza en esta solucion final, solo para tareas de debugging).

Al principio del codigo se definen constantes que se extraen de la realidad planteada, como por ejemplo la semilla, la funcion a integrar, el radio de la base del cono, la altura del cono, el error máximo permitido y la confianza dada.

La función principal **main()** realiza una simulación de Monte Carlo preliminar y luego calcula el número de réplicas necesarias (nN) para lograr el error máximo permitido (EPSILON) con confianza (DELTA). Después, se realiza **una segunda simulación** de Monte Carlo con el número de réplicas calculado y se muestran los resultados.

La función **montecarlo_simulation()** lleva a cabo una simulación de Monte Carlo para la estimacion de la integral de la funcion en el dominio del cono.

Las funciones auxiliares como **random_point(), U_01() y point_in_circle()** se utilizan para generar puntos aleatorios dentro del espacio de búsqueda y para verificar si un punto está dentro del cono.

```
# pseudocodigo

1. IMPORTAR bibliotecas

2. DEFINIR constantes y parámetros
   SEED_NUMBER
   CONE
   SAMPLE
   DELTA
   EPSILON

3. DEFINIR función F

4. DEFINIR función main():
   4.1 (Int_, Var_Int_, IC_Normal, Var_F) = montecarlo_simulation(n=SAMPLE)
   4.2 nN = number_of_replications_normal(Var_F)
   4.3 (Int_, Var_Int_, IC_Normal, Var_F) = montecarlo_simulation(n=nN)
   4.4 MOSTRAR resultados

5. DEFINIR función montecarlo_simulation(n):
   5.1 INICIALIZAR variables S y T
   5.2 PARA i en range(n):
         5.2.1 GENERAR punto aleatorio x_j
         5.2.2 CALCULAR F_x_y usando función F y x_j
         5.2.3 SI i > 1:
                  ACTUALIZAR T con T += (1 - (1/i)) * (F_x_y - (S/(i-1)))^2
               FIN SI
         5.2.4 ACTUALIZAR S con S += F_x_y
   5.3 CALCULAR Int_, Var_F, Var_Int_ y IC_Normal
   5.4 DEVOLVER (Int_, Var_Int_, IC_Normal, Var_F)


5. DEFINIR funciones auxiliares:
   5.1 random_point()
   5.2 U_01()
   5.3 point_in_circle(x_j)
   5.4 number_of_replications_normal(punctual_variance)
   5.5 reset_seed(i)


```

Vale la pena resaltar que dada la naturaleza del problema es posible calcular una solucion exacta, sin embargo, el objetivo de este ejercicio es estimar la integral de la funcion en el dominio del cono utilizando el metodo de Monte Carlo. Aunque, el resultado exacto fue util para verificar la solucion.

Las bases/resultados teoricos que se utilizaron fueron los siguientes:

- [Metodos Montecarlo] https://en.wikipedia.org/wiki/Monte_Carlo_integration
- [Estmacion de Integrales con Metodos Monte Carlo] EVA del curso - Unidad 2 - Sesion 6.

# V. Resultados Computacionales

1. MacBook Air, Apple M1, 2020, 8GB RAM, ptython 3.11.2
2. Semilla Inicial: 50826476; Dependiendo del numero de replicas la semilla se actualiza con la siguiente formula: seed = seed + 1
3. $(anexo) python3 exercise_6_1.py

## Corrida preliminar.
| n       | Int_               | Var                   | IC_Normal (inferior) | IC_Normal (superior) | time           |
|---------|--------------------|-----------------------|----------------------|----------------------|----------------|
| 1000000 | 1.3403573708455303 | 3.568695069327664e-06 | 1.3372500794873725   | 1.343464662203688    | 0:00:00.946256 |

## Numero de replicaciones necesarias para alcanzar el error maximo permitido.
| nN | delta | epsilon |
|:--:|:-----:|:-------:|
| 13708996 | 0.05  | 0.001   |

## Corrida con el numero de replicaciones calculado.
|    n    |        Int_        |           Var          | IC_Normal (inferior) | IC_Normal (superior) |      time      |
|:-------:|:------------------:|:----------------------:|:--------------------:|:--------------------:|:--------------:|
| 13708996 | 1.3407907982281904 | 2.60005449916871e-07 | 1.3397913982937237   | 1.341790198162657   | 0:00:13.227137 |


# VI. Anexo

Consultar la carpeta ~/anexo por los logs, capturas, código de la solucion y demás archivos de interés.
