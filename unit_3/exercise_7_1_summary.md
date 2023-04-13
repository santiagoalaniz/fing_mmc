# I. Unidad 3 - Sesion 7 - Problemas de Conteo -  Ejercicio 7.1

# II. Trabajo Individual.

Santiago Alaniz, CI 50826476, santiago.alaniz@fing.edu.uy

# III. Descripcion del Problema

Se busca determinar cuántas formas hay de asignar profesores a estudiantes en un programa de posgrado, considerando que deben compartir un idioma en común para comunicarse. Con P profesores, S estudiantes y L lenguajes posibles, se emplea el método Monte Carlo para estimar la cantidad de combinaciones válidas, considerando un número de replicaciones y un nivel de confianza. La salida incluye la estimación del número de combinaciones, la desviación estándar y un intervalo de confianza basado en el criterio de Agresti-Coull.

- Parte a) Escribir un programa para realizar el cálculo previamente descrito. Entregar pseudocódigo y código.

- Parte b) Estudiantes/lenguajes y Profesores/lenguajes dados. Utilizando el programa previamente mencionado y 1000 replicaciones de Monte Carlo, se busca estimar las combinaciones NC de asignación de profesores a estudiantes con un idioma en común y obtener intervalos de confianza de nivel 95%.

- Parte c) Realizar una adptacion del programa anterior para agregar una nueva restriccion sobre el numero minimo y maximo de estudiantes por profesor.

# IV. Descripcion de la Solucion

Este obligatorio fue programado en **Python 3.11**, usando las siguientes librerías:
- **datetime**: para medir el tiempo de ejecución.
- **math**: para operaciones matemáticas mas complejas.
- **pdb**: para depuracion del codigo (no es necesario).
- **random**: para generar números aleatorios.
- **scipy.stats**: para calcular percentiles de la distribución normal.
- **sys**: para obtener argumentos de la linea de comandos.

Este apartado detalla las soluciones para cada una de las partes.

Las bases/resultados teoricos que se utilizaron fueron los siguientes:

- [[Metodos Montecarlo] Wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_method)
- [Problemas de Conteo] EVA del curso - Unidad 3 - Sesion 7.

## Parte a)

Este código implementa un simulador de Monte Carlo para la asignación de profesores y estudiantes basada en los idiomas que hablan. La solucion genera un conjunto aleatorio de profesores, estudiantes y lenguajes, y luego asigna aleatoriamente a los estudiantes a un subconjunto de lenguajes y a los profesores tambien.

Los valores aleatorios son determinados por una semilla, y se utilizaron los siguientes rangos numericos:

- Lenguajes (L): entre 3 y 6
- Profesores (P): entre 2 y 4
- Estudiantes (S): entre 8 y 16
- Cada profesor/alumno comprende entre 1 y L lenguajes

Entiendase por configuracion un vector de largo S, cada coordenada del vector es un profesor seleccionado con la funcion random.randint(0, P-1). Y el indice del vector es el estudiante.

```
a = [profesor_x, profesor_y, profesor_z, ...]

a[i] = profesor asignado al estudiante i
```

La probabilidad de ocurrecia de ese vector es la productoria de la ocurrencia de cada profesor para cada alumno, dado que se trata de eventos independientes.

Cada profesor tiene una probabilidad de 1/P de ser seleccionado. Como se trata de un vector de largo S, la probabilidad de ocurrencia del vector es 1/P^S. Esto concuerda con el paso 2.1 del algoritmo de Monte Carlo presentado en el material de estudio.

- *Sortear un a e X con probabilidad 1/|X|*.

Luego de generar una configuracion aleatoria, se verifica si cumple con las restricciones. Si cumple, se incrementa el contador de ocurrencias. Si no, se descarta la configuracion y se vuelve a generar una nueva.

Recordemos que una configuracion es valida si y solo si todos los estudiantes tienen un profesor asignado que hable el mismo idioma que el estudiante. O lo que es lo mismo:

```
idP(a[i]) interseccion idS[i] != null para todo i, i = 0, 1, 2, ..., S-1
```

Finalmente, se calcula el estimador, su desviacion estandar y el intervalo de confianza de Agresti-Coull.

```
psedocodigo:

IMPORTAR_LIBRERIAS

# [1] Definir constantes y conjuntos
  P, S, L.
  idP[i] = {lenguajes que habla el profesor i}
  idS[j] = {lenguajes que habla el estudiante j}

# [2] Definir parámetros de entrada

  SAMPLES = OBTENER DE LA CONSOLA else 1000
  DELTA = OBTENER DE CONSOLA else 0.05

# [3] Simulacion de Monte Carlo, n = SAMPLES, r = P^S

  S_n = 0

  for i in range(n):
    a = configuracion_aleatoria()
    S_n += 1 if is_valid(a) else 0

  X_ = r * (S_n / n)
  Var_X_ = X_ * (r - X_) / (n - 1)
  IC = Agresti_Coull(X_, Var_X_, DELTA)
  return X_, Var_X_, IC

# [4] Funcion Principal
  initialize()
  r = largo(P) ^ largo(S)

  imprimir montecarlo_simulation(SAMPLES, r)
  imprimir valores_generados(P,S,L,idP,idS) # OPCIONAL

# [5] Funciones Auxiliares
```

## Parte b)
Para este apartado, se puede reutilizar casi por completo el codigo de la *parte a)*, la unica diferencia es que las constantes del problema vienen dadas por la letra del problema.

La funcion **initialize()** se encarga de inicializar las constantes del problema segun como se indica en el enunciado.

```
psedocodigo:

importar parte a)

# [1] redefinir initialize().
# [2] invocar main() de la parte a).

```

## Parte c)

De forma similar a la parte anterior, se puede reutilizar completamente la parte b), simplemente hay que tener en cuenta una restriccion de validez a la configuracion, cada profesor tiene un numero minimo y maximo de estudiantes asignados.

```
psedocodigo:

importar parte b)

# [1] redefinir initialize().
# [2] redefinir is_valid().
# [3] invocar main() de la parte a).

```

# V. Resultados Computacionales

- Windows 11, Ryzen 7 6800h, 16GB RAM DDR5 4800MHz, 1TB SSD.
- Numero de Semilla: 50826476;

## Parte a)

- $(~/anexo) python3 exercise_7_1_a.py arg_1: NRO_SAMPLES arg_2: INTERVALO_DELTA arg_3: MOSTRAT_DATOS_GENERADOS

|n|delta|X_|Var|IC (Agresti-Coull)|time|
|-|-|-|-|-|-|
|1000|0.05|131.072|22.808140083533115|(92.62390241313943, 184.191338567257)|0:00:00.004734|
|10000|0.05|138.0352|7.391840786104413|(124.24730481318983, 153.28994192930946)|0:00:00.043097|
|100000|0.05|130.6624|2.2762374851568734|(126.27359968826146, 135.19850212191554)|0:00:00.427581|
|1000000|0.05|127.238144|0.7106183205588165|(125.85270046752734, 128.63834453093264)|0:00:04.297136|
|10000000|0.05|127.9291392|0.2253068885475855|(127.4882822749276, 128.37147129913467)|0:00:43.301886|

## Parte b)

- $(~/anexo) python3 exercise_7_1_b.py 1000 0.05

|n|delta|X_|Var|IC (Agresti-Coull)|time|
|-|-|-|-|-|-|
|1000|0.05|128974.848|10896.060891109579|(109076.34628120286, 151898.88563653224)|0:00:00.004276|

## Parte c)

- $(~/anexo) python3 exercise_7_1_c.py

|n|delta|X_|Var|IC (Agresti-Coull)|time|
|-|-|-|-|-|-|
|1000|0.05|76546.048|8630.152425891665|(61212.735769646475, 95306.16085866356)|0:00:00.004816|

# VI. Anexo

Consultar la carpeta ~/anexo por los logs, capturas, código de la solucion y demás archivos de interés.
