# I. Unidad 2 - Sesión 6 -  Ejercicio 6.2

# II. Trabajo Grupal.
* Santiago Alaniz, CI 50826476, santiago.alaniz@fing.edu.uy
* Bruno De Simone, CI 49145550, bruno.de.simone@fing.edu.uy

# III. Descripción del Problema

Problema: Se desea estimar la integral de la función x1x2^2x3^3x4^4x5^5 sobre el hipercubo Jm de dimensión m = 5.

• Parte a: Revisar los códigos preparados para el ejercicio 6.1, elegir uno de ellos como punto de partida. Sobre esa base, modificarlo para realizar el cálculo por Monte Carlo de la integral planteada en el ejercicio 6.2. Realizar 10^6 replicaciones y estimar el valor de ζ. Calcular analíticamente el valor exacto de la integral.

• Parte b: En base al valor estimado en la parte a, calcular el número de replicaciones necesario para obtener un error menor a 10^-4 (con nivel de confianza 0.95).

• Parte c: Decimos que un intervalo de confianza cubre el valor exacto cuando este último pertenece al intervalo. Realizar L = 500 experimentos con semillas diferentes, cada uno consistente en estimar por Monte Carlo con el número de replicaciones de la parte b el valor de la integral, así como intervalos de confianza de nivel 0.9, 0.95 y 0.99. Para cada nivel de confianza, calcular el nivel de cobertura empírico (en qué porcentaje de los 500 experimentos el intervalo de confianza calculado cubrió el valor exacto). Discutir los resultados, comparando la cobertura empírica con la especificada.

# IV. Descripción de la Solución

## Parte a)
Se tomó la solución en python debido a que ambos miembros tenían experiencia con el lenguaje. Los únicos cambios que se tuvieron que realizar para la adaptacion del codigo fueron:
* En cada iteración generar un vector de 5 dimensiones en vez de 2.
* Cambiar la función que en el 6.1 obtiene la altura del punto por la función de la que se quiere calcular la integral.

```python
def F(x1, x2, x3, x4, x5): return x1 * x2 ** 2 * x3 ** 3 * x4 ** 4 * x5 ** 5

def montecarlo_simulation(n: int):
    # Initialize the variables
    S = 0
    T = 0

    for i in range(n):
        # Random point generator using uniform distribution U(0,1)
        x_j = random_point()
        # Evaluate function value
        F_x_y = F(*x_j)

        T += (1 - (1/i)) * ((F_x_y - (S/(i-1))) ** 2) if i > 1 else 0
        S += F_x_y

    Int_ = (S / n)
    Var_F = T / (n - 1)
    Var_Int_ = Var_F / n
    IC_Normal = (Int_ - i_norm_95 * math.sqrt(Var_Int_),
                 Int_ + i_norm_95 * math.sqrt(Var_Int_))

    return (Int_, Var_Int_, IC_Normal, Var_F)


def random_point():
    return [U_01() for _ in range(5)]
```

Luego para el calculo analitico simplemente se utilizo la biblioteca scipy que ofrece la funcionalidad de calcular integrales, se encadenó el llamado de esa función para integrar en [0,1] en dx_1, dx_2, dx_3, dx_4 y dx_5.
```python
analytic_value = quad(lambda x1:
                      quad(lambda x2:
                           quad(lambda x3:
                                quad(lambda x4:
                                     quad(lambda x5: 
                                        F(x1, x2, x3, x4, x5),
                                     0, 1)[0],
                                0, 1)[0], 
                           0, 1)[0], 
                      0, 1)[0], 
                 0, 1)[0]
```


## Parte b)
Se realizó lo mismo que en el ejercicio 6.1 pero con una cota de error distinta.
```python
def number_of_replications_normal(punctual_variance: float):
    i_norm_delta = i_norm(1 - (DELTA / 2))
    sqr_epsilon = EPSILON ** 2
    return math.ceil((((i_norm_delta ** 2) * punctual_variance) / sqr_epsilon))
```

## Parte c)
Para esta parte se modificó un poco el código de la última parte del 6.1 agregando el cálculo de los intervalos de confianza deseados 90%, 95%, 99% y agregando un loop que ejecute ese código 500 veces.
```python
for i in range(500):
		# different seed per iteration
        reset_seed(i)
        (Int_, Var_Int_, IC_Normal, Var) = montecarlo_simulation(n=nN)
        # 95%
        if IC_Normal[0] <= analytic_value <= IC_Normal[1]:
            cubre_valor_95 += 1
        # 90%
        IC_Normal = (Int_ - i_norm_90 * math.sqrt(Var_Int_),
                     Int_ + i_norm_90 * math.sqrt(Var_Int_))
        if IC_Normal[0] <= analytic_value <= IC_Normal[1]:
            cubre_valor_90 += 1
        # 99%
        IC_Normal = (Int_ - i_norm_99 * math.sqrt(Var_Int_),
                     Int_ + i_norm_99 * math.sqrt(Var_Int_))
        if IC_Normal[0] <= analytic_value <= IC_Normal[1]:
            cubre_valor_99 += 1
```

# V. Resultados Computacionales

1. AMD Ryzen 7 1700x a 3.4 GHz, 16 GB DDR4 3200mhz, python 3.10
2. Semilla Inicial: 50826476;
3. $(anexo) python3 exercise_6_2.py

## Parte a)
Se realizaron las 10^6 repeticiones lo cual generó:
 * <b>Estimacion</b>: 0.0013768445624771088
 * <b>Varianza de la estimación</b>: 9.546173358639415e-11
 * <b>Encontró intervalo de confianza en un 95% con cota de error de 0.0001</b>: (0.0013576948283138312, 0.0013959942966403865)
 * <b>Duración de ejecución</b>: 2.296041s

La solución analítica para la integral de la función es: 0.0013888...

## Parte b)
A partir de la aproximación normal obtuvimos:
* <b>nN (mínimo de replicaciones)</b>: 36672
* delta: 0.05
* epsilon: 0.0001

## Parte c)
Para la las 500 iteraciones se obtuvieron distintos resultados segun el intervalo de confianza deseado, consideramos que tiene sentido ya que a medida que se calcula un intervalo de confianza con mayor porcentaje tienden a cubrir mas veces el valor real.

| 90% | 95% | 99% |
|:--:|:-----:|:-------:|
| 87.4% | 93.6%  | 98.8%   |

# VI. Anexo

Consultar la carpeta ~/anexo por los logs, capturas, código de la solución y demás archivos de interés.
