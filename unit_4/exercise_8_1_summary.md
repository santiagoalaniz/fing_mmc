# I. Unidad 3 - Sesion 8 - Problemas de Conteo -  Ejercicio 8.1

# II. Trabajo Grupal.

* Santiago Alaniz, CI 50826476, santiago.alaniz@fing.edu.uy
* Bruno De Simone, CI 49145550, bruno.de.simone@fing.edu.uy

# III. Descripcion del Problema

Parte a) Elegir al menos dos fuentes de números aleatorios disponibles en Internet (sitio web o tabla con valores). Explicar como funcionan, como se accede a los numeros y que caracteristicas tienen.

Parte b) En base a este analisis, elegir una de las fuentes, fundamentar la eleccion, y modificar el ejercicio 3.1 parte a) (sesion 3) para que use la nueva fuente de numeros aleatorios (en lugar de los generados por las bibliotecas). Comparar los resultados obtenidos con los de la parte a) del ejercicio 3.1.

# IV. Descripcion de la Solucion

## Tabla RAND

Coleccion de numeros aleatorios publicada a mediados del siglo XX por RAND Corporation en el libro "A million random digits with 100,000 normal deviates", su proposito era proporcionar una fuente confiable de numeros aleatorios para ser utilizados en pruebas estadisitcas y experimentos cientificos.

La tabla contiene un millon de digitios aleatorios, agrupados en viente mil (20.000) filas con cincuenta (50) digitos cada una. Cada fila esta numerada del 0 al 19.999, y cada columna agrupa 5 digitos, numeradas del 0 al 9.

La tabla fue creada utilizando una ruleta electrica conectada a una computadora, que fue debidamente testeada antes de usarla para generar los numeros. La tabla RAND fue un hito en la distribucion de numeros aleatorios dado que fue la primera vez en la historia que se preparaba una tabla de tal exustivo cuidado y refinamiento.

Pese a tener ya mas de 50 años, sigue siendo util para fines educativos y para validar algoritmos que requieran numeros aleatorios.

Para acceder a la tabla, se debe descargar el archivo de texto que la contiene, parsearla con el lenguaje de programacion de preferencia, y luego utilizarla como fuente de numeros aleatorios. Por ejemplo podria utilizar la configuracion de 20000x50 para generar un arreglo con un millon de numeros aleatorios de 5 digitos cada uno.

```pseudocode
rand_table = import(anexo/RAND_true_random_numbers.txt)
rand_table[0][0] = FIVE_DIGIT_TRUE_RANDOM_NUMBER
```

## random.org

La pagina web random.org (proyecto Random.org) es un servicio brindado por la Universidad de Dublin, Irlanda. Random.org usa como fuente de numeros aleatorios el ruido atmosferico. El ruido atmosferico fenomeno natural causado por varios eventos fisicos por ejemplo las descargas electricas, la radiacion solar, la actividad magnetica, etc. 

El ruido atmosferico es por tanto impredecible y dificil de reproducir, lo que lo hace una fuente de numeros aleatorios confiable.

El proceso de obtencion de estos numeros es el siguiente:

- Una bateria de radiofrecuencias capturan el ruido atmosferico desde varios puntos de la tierra. Estos receptores estan configurados y sintonizadas en freecuencias donde no hay señales generadas por humanos, para asegurarse que el ruido es natural.

- Estos receptores convierten el ruido atmosferico a señales electricas, que llegan con todo tipo de voltajes y luego son digitalizadas.

- Estas señales digitales son preprocesadas para eliminar potenciales errores y sesgos. Este paso puede involucrar el metodo descrito por Von Nuemann para garantizar que los numeros sean realmente aleatorios.

- Finalmente, los numeros son guardos en la base de datos y servidores de random.org, y son distribuidos a los usuarios que los solicitan.

Random.org provee una pagina web con diversas herramientas y servicios que hacen uso de estos numeros aleatorios. En el caso de querer usarlos en un programa de computadora, se puede utilizar la API de random.org, que provee diversos endpoints con parametros para solicitar numeros aleatorios de distintos tipos. Cabe resaltar, que es un servicio gratuito pero tiene una cuota de uso limitado por direccion IP (1 millon de bits por dia).

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

Las bases/resultados teoricos que se utilizaron fueron los siguientes:

- [[Metodos Montecarlo] Wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_method)
- [[RAND table] Wikipedia](https://en.wikipedia.org/wiki/Random_number_table)
- [[Random.org] Wikipedia](https://en.wikipedia.org/wiki/Random.org)
- [Problemas de Conteo] EVA del curso - Unidad 4 - Sesion 8.

# V. Resultados Computacionales

- Windows 11, Ryzen 7 6800h, 16GB RAM DDR5 4800MHz, 1TB SSD.
- Numero de Semilla: 50826476;

# VI. Anexo

Consultar la carpeta ~/anexo por los logs, capturas, código de la solucion y demás archivos de interés.
