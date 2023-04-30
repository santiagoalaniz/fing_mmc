# I. Unidad 4 - Sesión 11 - Sorteo de Variables con distribucion arbitraria -  Ejercicio 11.1

# II. Trabajo Individual.

* Santiago Alaniz, CI 50826476, santiago.alaniz@fing.edu.uy

# III. Descripción del Problema

Para generar un punto aleatorio **(X1, X2)** en un círculo de centro **(0, 0)** y **radio 1**, es posible hacerlo de la siguiente forma:

- Se genera un valor aleatorio r, de distribución **Fr(x) = x^2** para 0 ≤ x ≤ 1, y 0 para cualquier otro x.
- Se generan dos v.a. independientes Z1 y Z2 de distribución normal (0, 1).
- Se calcula X1 = rZ1/p(Z1^2 + Z2^2) y X2 = rZ2/p(Z1^2 + Z2^2).

Utilizar esta propiedad para volver a resolver el Ejercicio 6.1 parte a, pero generando únicamente valores de puntos dentro del círculo de base de la montaña:

**Problema 6.1:** se idealiza una montaña como un cono inscrito en una región cuadrada de lado 1 km. La base de la montaña es circular, con centro en (0.5, 0.5) y radio r = 0.4 km, y la altura es H = 8 km. La altura de cada punto (x, y) de la montaña está dada por la función

- **f(x, y) = H - H/r × p(x - 0.5)^2 + (y - 0.5)^2**

en la zona definida por el círculo, y 0 fuera del círculo. El volumen total de la montaña (en km cúbicos) puede verse como la integral de la función altura en la región.

### Parte a)

Escribir un programa para calcular el volumen por Monte Carlo. Realizar 10^6 replicaciones y estimar el valor de ζ y el error cometido (con nivel de confianza 0.95), utilizando como criterio la aproximación normal. Comparar la precisión obtenida con la alcanzada en el **Ejercicio 6.1**


# IV. Resumen de la Solución

## Fundamento Teórico

Se generaron puntos dentro de la *región de interés* (**CCL(r=0.4, centro=(0.5, 0.5))**) usando el método del problema, pero modificándolo:

1. Para generar un valor **r** aleatorio, se utilizó **Fr^-1(U(0,1))** como distribución equivalente a **Fr(x)**.
2. Se generaron **Z1, Z2 ~ Norm(mu=0, var=1)** y se calcularon las coordenadas aleatorias en un **CCL(radio=1, centro=(0, 0))**:
   - X1 = r Z1 / sqrt(Z1^2 + Z2^2)
   - X2 = r Z2 / sqrt(Z1^2 + Z2^2).
3. Se ajustaron las coordenadas aleatorias a la *región de interés* mediante traslación y escalamiento:
   - X1 = 0.5 + 0.4 * X1
   - X2 = 0.5 + 0.4 * X2

Se aplicó integración por Monte Carlo pmediante el metodo de aproximacion a la integral de Lebesgue-Stieltjes. La función de altura k(x, y) se aproximó usando puntos generados por la distribución F(x,y) = (X1, X2), y se multiplicó por el área del círculo para obtener la densidad de probabilidad dF(x, y). Finalmente se calculo el error para un nivel de confianza del 95% usando la aproximación normal.

Fundamentos Teoricos:
- [Sorteo de Variables con distribucion arbitraria] EVA del Curso - Unidad 4 - Sesión 11
- [Integracion por Monte Carlo] EVA del Curso - Unidad 3 - Sesión 6
- [[Transformaciones Geometricas]](https://es.wikipedia.org/wiki/Transformaci%C3%B3n_geom%C3%A9trica)
- [Monte Carlo: concepts, algorithms and applications] - Fishman 1996.

## Pseudocodigo
```python

Constantes:
  ccl_cone = (r = 0.4, c = (0.5, 0.5))
  cone_height = 8
  n = 1000000
  delta = 0.05

Función Fr():
  return sqrt(uniform_sample)

Función scl_to_ccl_cone(x, y):
  return (x * ccl_cone['r'] + ccl_cone['c'][0], y * ccl_cone['r'] + ccl_cone['c'][1])

Función F():
  r = Fr()
  (Z1, Z2) = (normal_samples.pop(), normal_samples.pop())
  X1 = r * Z1 / sqrt(Z1^2 + Z2^2)
  X2 = r * Z2 / sqrt(Z1^2 + Z2^2)
  return scl_to_ccl_cone(X1, X2)

Función k(x, y):
  return cone_height - (cone_height / ccl_cone['r']) * sqrt((x - ccl_cone['c'][0])^2 + (y - ccl_cone['c'][1])^2)

Función montecarlo_simulation(n):
  Inicializar S = 0, T = 0
  Para i en rango(n):
    (x, y) = F()
    k_x_y = k(x, y)
    Si i > 1:
      T += (1 - (1/i)) * ((k_x_y - (S/(i-1)))^2)
    S += k_x_y

  Int_ = (S / n) * ccl_cone_area
  Var_F = T / (n - 1)
  Var_Int_ = Var_F / n
  ic_delta = norm.ppf(1 - delta/2) * sqrt(Var_Int_)
  IC = (Int_ - ic_delta, Int_ + ic_delta)

  return (Int_, Var_Int_, IC, Var_F)

Función main():
  (Int_, Var_Int_, IC, Var_F) = montecarlo_simulation(n)
  Imprimir resultados
```

# V. Resultados Computacionales

1. MacBook Air, Apple M1, 2020, 8GB RAM, ptython 3.11.2
2. Semilla: 50826476;
3. $(~/utils) python3 exercise_6_1_redo.py
3. $(~/anexo) python3 exercise_11_1.py

Para este laboratorio y posteriores se utilizara la libreria `scipy.stats` en vez de `random`. La justificacion es que es una libreria mas comoda para trabajar y posee mas herramientas. Apelando a la consistencia tecnica, el codigo del ejercicio 6.11 fue re-escrito ultizando esta libreria e incluido en ~anexo/utils/excersice_6_1_redo.py. No hay mucho que comentar sobre la re-escritura de este ejercicio, se trato simplemente de cambiar las dependecias y llamadas a estas.


| Ejecución | Comando                     | n       | Int_         | Var               | IC_Normal (min)  | IC_Normal (max)  | Diff              | Tiempo      |
|-----------|-----------------------------|---------|--------------|-------------------|------------------|------------------|-------------------|-------------|
| 1         | exercise_6_1_redo.py        | 1000000 | 1.3421821369 | 3.5752838518e-06  | 1.3384761545     | 1.3458881193     | 0.0017692714      | 0:00:00.770 |
| 2         | exercise_11_1.py            | 1000000 | 1.3387230133 | 3.5483240768e-06  | 1.3350310300     | 1.3424149967     | 0.0016898522      | 0:00:00.894 |
| 3         | exercise_6_1_redo.py        | 100000  | 1.3404009111 | 3.5853824375e-05  | 1.3286650264     | 1.3521367958     | 1.1954449e-05     | 0:00:00.079 |
| 4         | exercise_11_1.py            | 100000  | 1.3407402621 | 3.5565852740e-05  | 1.3290516026     | 1.3524289215     | 0.0003273965      | 0:00:00.090 |
| 5         | exercise_6_1_redo.py        | 10000   | 1.3481004954 | 0.0003621266      | 1.3108031146     | 1.3853978762     | 0.0076876298      | 0:00:00.008 |
| 6         | exercise_11_1.py            | 10000   | 1.3354770752 | 0.0003548754      | 1.2985550030     | 1.3723991474     | 0.0049357903      | 0:00:00.010 |
| 7         | exercise_6_1_redo.py        | 1000    | 1.4061802260 | 0.0038555227      | 1.2844804655     | 1.5278799866     | 0.0657673605      | 0:00:00.001 |
| 8         | exercise_11_1.py            | 1000    | 1.3974097956 | 0.0036746722      | 1.2785985924     | 1.5162209988     | 0.0569969300      | 0:00:00.001 |

El caso n=100000 fue verdaderamente favorable para el metodo clasico. Dejando de lado esto, los demas se comportaron como se esperaba.

Se puede apreciar que la varianza siempre es menor en el ejercicio 11.1 y por lo tanto el IC tambien. Tambien se puede apreciar que la diferencia entre el estimador y el valor real es menor en el ejercicio 11.1.

# VI. Anexo

Consultar la carpeta ~/anexo por los logs, capturas, código de la solución y demás archivos de interés.
