# I. Unidad 2 - Sesion 5 -  Ejercicio 5.1

# II. Trabajo individual.

Santiago Alaniz, CI 50826476, santiago.alaniz@fing.edu.uy

# III. Descripcion del Problema
```
Problema (enunciado en sesión 3, ejercicio 3.1): Se desea estimar el volumen de una región R en [0,1]^6 definida por todos los puntos de la hiperesfera de centro (0.45, 0.5, 0.6, 0.6, 0.5, 0.45) y radio 0.35 que además cumplan las siguientes restricciones: 3x1 + 7x4 ≤ 5; x3 + x4 ≤ 1; x1 - x2 - x5 + x6 ≥ 0.
```
- **Parte a**: Compartir en el grupo los códigos desarrollados para la parte a, validarlos revisando los códigos y verificando si las salidas para tamaños de muestra de 10^6 son consistentes. Indicar si se detectaron errores en los mismos, y en ese caso dar los códigos corregidos. Elegir uno de los códigos para las partes siguientes, explicando los motivos de la selección.

- **Parte b**: Calcular la cantidad de replicaciones necesarias para garantizar un error menor a 1.0 × 10^-4 con una probabilidad del 0.95, utilizando el criterio de peor caso de Hoeffding.

- **Parte c**: Utilizando el código elegido en la parte a y la cantidad de replicaciones definida en el punto anterior, calcular el intervalo de confianza de nivel 0.95 utilizando el criterio de Chebyshev y el criterio de Agresti-Coull. Comparar el ancho de estos intervalos entre sí y con el criterio de error manejado en el punto previo.

# IV. Descripcion de la Solucion

## Parte a)

## Parte b)
En esta sección se utiliza el criterio de Hoeffding para calcular la cantidad de replicaciones necesarias que garantizan un error menor a 1.0 × 10^-4 con una probabilidad del 0.95.

En la sección 4.1 se emplean varios métodos (Chebyshev, Normal, Hoeffding) para calcular el tamaño de muestra necesario para unos valores dados delta y epsilon.

Para calcular el tamaño de muestra necesario en esta parte del obligatorio, se reutiliza el código de la sección 3.1 y se llama a la función n_of_samples_hoeffding con los valores correspondientes de delta y epsilon:

```
  IMPORT n_of_samples_hoeffding from exercise_3_1

  DELTA = 0.05
  EPSILON = 0.0001

  n_of_samples_hoeffding(EPSILON, DELTA)
```

## Parte c)
En esta sección se reutiliza código de partes anteriores, en particular de la **Sección 3.1**, utilizando la función **montecarlo_simulation** con el número de replicaciones calculado en la **parte b)**.

Sin embargo, se ha modificado levemente el código elegido en la **parte a**), ya que la función **montecarlo_simulation** original no devolvía el número de puntos que pertenecen a la región de interés (**S_n**), lo cual es necesario para los cálculos siguientes.

Todo lo descrito hasta ahora forma parte de la etapa de precomputo. Una vez obtenidos los resultados, es decir, el valor de n_H y S_n_H, se procede a calcular los intervalos de confianza.

Esto entra en concordancia con los requisitos a la hora de calcular intervalos de confianza.

```
"En estos casos, en general se plantea el problema inverso: conociendo el tamaño de muestra n previamente establecido, y dado un nivel de confianza deseado, ¿qué precisión podemos asignar al resultado obtenido a partir de los resultados de las replicaciones simuladas?"
```

Los resultados arrojados para los intervalos de confianza pueden ser confusos a primera vista, ya que el intervalo de confianza de Chebyshev puede parecer más estrecho que el de Agresti-Coull.

Sin embargo, en este caso particular, el intervalo de confianza de Agresti-Coull es más amplio que el de Chebyshev (ver V. resultados computacionales), lo que indica que es más conservador.

Es importante destacar que el intervalo de Agresti-Coull puede ser más conservador (es decir, más amplio) que otros intervalos de confianza, especialmente cuando la proporción de éxitos es cercana a 0 o 1, lo cual es el caso en este ejercicio. Por lo tanto, es importante evaluar cuidadosamente las características de la muestra y del objetivo del análisis para seleccionar el método de intervalo de confianza más adecuado.

```python
def chebyshev_interval_of_confidence(z=int, n=int, beta=float):
  a = z + (DELTA / 2)
  b = beta * math.sqrt((DELTA / 4) + (z * (n - z) / n))
  divident = n + DELTA

  ic_lower = (a - b) / divident
  ic_upper = (a + b) / divident

  return (ic_lower, ic_upper)

def agresti_coull_interval_of_confidence(n_s=int, n=int, delta=float):
  z = inversed_norm(1 - (delta / 2))
  sqr_z = z ** 2
  n_ = n + (sqr_z)
  p_ = (1 / n_) * (n_s + (sqr_z / 2))
  ic_constant = (z * math.sqrt((p_ / n_) * (1 - p_)))

  ic_lower = p_ - ic_constant
  ic_upper = p_ + ic_constant

  return (ic_lower, ic_upper)
```

## Bases Teóricas
- Calculo de intervalos de confianza, Unidad 2, Sesión 5.
- Intervalo Agresti-Coull, https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Agresti%E2%80%93Coull_interval
- Interval Estimation fora Binomial Proportion, Lawrence D. Brown, T. Tony Cai and Anirban DasGupta


# V. Resultados Computacionales

1. MacBook Air, Apple M1, 2020, 8GB RAM, ptython 3.11.2
2. Semilla:
  - 50826476 (utilizada en exercise_3_1.py)
3. $(anexo) python3 exercise_5_1.py LINEAR (#para generar los resultados pre-computados, ver anexo)
4. $(anexo) python3 exercise_5_1.py (para generar los intervalos de confianza si decide no reutilizar los resultados pre-computados)

## Parte b)
|  Epsilon  |    Delta    |    n_H (Hoeffding) |
|:---------:|:-----------:|:---------:|
| 0.0001    | 0.05        | 184443973 |


## Parte c)

### Estimacion de Volumen con n=n_H de la Parte b)
|     n     |  S_n  |          Vol_          |           Var          | BOUNDARIES |      time      |
|:---------:|:-----:|:----------------------:|:----------------------:|:----------:|:--------------:|
| 184443973 | 52036 | 0.00028212361268101726 | 1.5291582364545105e-12 | True       | 0:04:04.174310 |

### Intervalos Chebyshev y Agresti-Coull

| Intervalo de Confianza (n, S_n, delta=0.05) |     Límite Inferior    |     Límite Superior    |
|:----------------------:|:----------------------:|:----------------------:|
| Chebyshev              | 0.00029913319438221777 | 0.00030691677531528367 |
| Agresti-Coull          | 0.0002707000568436197  | 0.00033913905930522254 |

# VI. Anexo

Consultar la carpeta ~/anexo por los logs, capturas, código de la solucion y demás archivos de interés.
