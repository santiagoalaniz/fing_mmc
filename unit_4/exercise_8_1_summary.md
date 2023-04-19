# I. Unidad 4 - Sesión 8 - Problemas de Conteo -  Ejercicio 8.1

# II. Trabajo Grupal.

* Santiago Alaniz, CI 50826476, santiago.alaniz@fing.edu.uy
* Bruno De Simone, CI 49145550, bruno.de.simone@fing.edu.uy

# III. Descripción del Problema

Parte a) Elegir al menos dos fuentes de números aleatorios disponibles en Internet (sitio web o tabla con valores). Explicar cómo funcionan, cómo se accede a los números y qué características tienen.

Parte b) En base a este análisis, elegir una de las fuentes, fundamentar la elección, y modificar el ejercicio 3.1 parte a) (sesión 3) para que use la nueva fuente de números aleatorios (en lugar de los generados por las bibliotecas). Comparar los resultados obtenidos con los de la parte a) del ejercicio 3.1.

# IV. Descripción de la Solución

## Parte A

### Tabla RAND

Colección de números aleatorios publicada a mediados del siglo XX por RAND Corporation en el libro "A million random digits with 100,000 normal deviates", su propósito era proporcionar una fuente confiable de números aleatorios para ser utilizados en pruebas estadísticas y experimentos científicos.

La tabla contiene un millón de dígitos aleatorios, agrupados en veinte mil (20.000) filas con cincuenta (50) dígitos cada una. Cada fila está numerada del 0 al 19.999, y cada columna agrupa 5 dígitos, numeradas del 0 al 9.

La tabla fue creada utilizando una ruleta eléctrica conectada a una computadora, que fue debidamente testeada antes de usarla para generar los números. La tabla RAND fue un hito en la distribución de números aleatorios dado que fue la primera vez en la historia que se preparaba una tabla de tal exhaustivo cuidado y refinamiento.

Pese a tener ya más de 50 años, sigue siendo útil para fines educativos y para validar algoritmos que requieran números aleatorios.

Para acceder a la tabla, se debe descargar el archivo de texto que la contiene, parsearla con el lenguaje de programación de preferencia, y luego utilizarla como fuente de números aleatorios. Por ejemplo, podría utilizar la configuración de 20000x50 para generar un arreglo con un millón de números aleatorios de 5 dígitos cada uno.

```pseudocode
rand_table = import(anexo/RAND_true_random_numbers.txt)
rand_table[0][0] = FIVE_DIGIT_TRUE_RANDOM_NUMBER
```

### random.org

La página web random.org (proyecto Random.org) es un servicio brindado por la Universidad de Dublín, Irlanda. Random.org usa como fuente de numeros aleatorios el ruido atmosferico. El ruido atmosférico es un fenómeno natural causado por varios eventos físicos por ejemplo las descargas eléctricas, la radiación solar, la actividad magnética, etc. 

El ruido atmosférico es por tanto impredecible y difícil de reproducir, lo que lo hace una fuente de números aleatorios confiable.

El proceso de obtención de estos números es el siguiente:

- Una batería de radiofrecuencias capturan el ruido atmosférico desde varios puntos de la tierra. Estos receptores están configurados y sintonizadas en frecuencias donde no hay señales generadas por humanos, para asegurarse que el ruido es natural.

- Estos receptores convierten el ruido atmosférico a señales eléctricas, que llegan con todo tipo de voltajes y luego son digitalizadas.

- Estas señales digitales son preprocesadas para eliminar potenciales errores y sesgos. Este paso puede involucrar el método descrito por Von Nuemann para garantizar que los números sean realmente aleatorios.

- Finalmente, los números son guardados en la base de datos y servidores de random.org, y son distribuidos a los usuarios que los solicitan.

Random.org provee una página web con diversas herramientas y servicios que hacen uso de estos números aleatorios. En el caso de querer usarlos en un programa de computadora, se puede utilizar la API de random.org, que provee diversos endpoints con parámetros para solicitar números aleatorios de distintos tipos. Cabe resaltar, que es un servicio gratuito pero tiene una cuota de uso limitado por dirección IP (1 millón de bits por día).

```python
import requests

def get_random_number(min_value, max_value):
    url = "https://www.random.org/integers/"
    params = {
        "num": 1,
        "min": min_value,
        "max": max_value,
        "col": 1,
        "base": 10,
        "format": "plain",
        "rnd": "new"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return int(response.text.strip())

min_value = 0
max_value = 100
random_number = get_random_number(min_value, max_value)
print(f"Random number between {min_value} and {max_value}: {random_number}")
```

Las bases/resultados teóricos que se utilizaron fueron los siguientes:

- [[Metodos Montecarlo] Wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_method)
- [[RAND table] Wikipedia](https://en.wikipedia.org/wiki/Random_number_table)
- [[Random.org] Wikipedia](https://en.wikipedia.org/wiki/Random.org)
- [Problemas de Conteo] EVA del curso - Unidad 4 - Sesión 8.

## Parte B

Para la parte B de la entrega decidimos optar por la tabla de dígitos generados aleatoriamente. Decidimos utilizar esta herramienta debido a que para utilizar Random.org sin limitaciones hay que pagar y que nos nos intrigaba más utilizar la tabla ya generada. 
Prevemos que el uso de la tabla está acompañada de una limitante que hablaremos más adelante.

Para la implementación se tomó el mismo código del Ejercicio 3.1 y se le realizaron pequeñas modificaciones. 
Los cambios importantes son:
* Como se define la semilla, la cual ahora es una coordenada cualquiera de la tabla, está ahora define por cuál sección de la tabla comenzar y a partir de ahí se recorre la tabla de forma ordenada de arriba para abajo y de izquierda a derecha. Esto nos permite realizar experimentos deterministas.
* Como obtengo los números aleatorios, para este ejercicio necesito un vector de 6 dimensiones por lo cual para cada iteración consumo 6 posiciones en la tabla.

De consumir las 6 posiciones de la tabla por iteración es que surge la limitante, en la tabla se tienen 
10 x 20000 = 200000 posiciones únicas, lo que significa que a partir de la iteración 33333 empezaremos a utilizar posiciones ya consumidas anteriormente. Debido a que 6 no es un dividendo de 200000 igualmente no se repetirán vectores. 

Sin embargo, a partir de las 100000 iteraciones empezaremos a generar exactamente los mismos vectores generados previamente. Notamos aquí una clara limitante al uso de las tablas pregeneradas. Para el caso con n=10^6, se generaron 10^6/10 vectores únicos.

```python
def montecarlo_simulation(n: int):
    # Seed number for the random number generator reproducibility
    SEED = (2, 7)
    # Initialize the variables
    S_n = 0
    V_s = 0

	# Read file into pandas dataframe
    df = pd.read_fwf('utils/RAND_true_random_numbers.txt', header=None)
    df = df.drop(columns=[0])

    for i in range(n):
        # generador de la distribución uniforme
        (SEED, x_j) = random_point(df, SEED)

        # Si el punto está en la región, incrementar S_n
        S_n = S_n + 1 if point_in_region(x_j) else S_n

    Vol_ = S_n/n
    V_s = (S_n/n)*(1 - S_n/n)/(n-1)

    return (Vol_, V_s, S_n)


def random_point(df, SEED):
    x_j = []
    for i in range(6):
        (row, col) = SEED
        # Get a random row from the file
        columna = df[col]
        # Get the values of the row
        value = columna[row]****
        # Add the value to x_j
        x_j.append(value/100000)
        # Update the Seed
        if len(df.index) - 1 == row:
            if len(df.columns) == col:
                SEED = (0, 1)
            else:
                SEED = (0, col + 1)
        else:
            SEED = (row+1, col)

    return (SEED, x_j)
```

# V. Resultados Computacionales

- Ubuntu, AMD Ryzen 7 1700x a 3.4 GHz, 16GB RAM DDR4 3200mhz.
- Número de Semilla: (2, 7);
- $ python3 exercise_8_1.py LINEAR

## Parte B

Utilizando Tabla Pregenerada
|    n    |   Vol_   |           Var          | Tiempo de cálculo | BOUNDARIES |
|:-------:|:--------:|:----------------------:|:-----------------:|:----------:|
| 10000   | 0.0001   | 1e-08  |  0:00:00.562749    | True       |
| 1000000 | 0.00025 | 2.4993774993774993e-10| 0:00:38.125452   | True       |
| 100000 | 0.00025 | 2.49939999399994e-09| 0:00:03.922398   | True       |

Utilizando librerias de Python
|    n    |   Vol_   |           Var          | Tiempo de cálculo | BOUNDARIES |
|:-------:|:--------:|:----------------------:|:-----------------:|:----------:|
| 10000   | 0.0004   | 3.998799879987999e-08  | 0:00:00.042454    | True       |
| 1000000 | 0.000303 | 3.0290849390849393e-10 | 0:00:02.906765,    | True       |

Lo primero que notamos es que toma mucho más tiempo utilizar la tabla pregenerada, creemos que esto es debido a que se tiene que trabajar con una matriz enorme en memoria y que acceder a las entradas de la misma para obtener un número aleatorio toma más tiempo que generar uno pseudo-aleatorio con las librerías nativas.

En cuanto a la estimación de volumen consideramos que 10^4 iteraciones son muy pocas, ya que realizando otros experimentos con semillas distintas en librerías de nativas se puede llegar al mismo resultado.

Por otra parte, para 10^6 iteraciones confiamos mucho más en el resultado de la librería ya que como se mencionó previamente sabemos de forma certera que no podemos generar más de 10^5 vectores distintos. Para demostrar esto se realizaron además 10^5 iteraciones y vemos que la estimación es la misma.
# VI. Anexo

Consultar la carpeta ~/anexo por los logs, capturas, código de la solución y demás archivos de interés.



