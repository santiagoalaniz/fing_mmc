# I. Unidad 2 - Sesion 4 -  Ejercicio 4.1

# II. Trabajo individual.

Santiago Alaniz, CI 50826476, santiago.alaniz@fing.edu.uy

# III. Descripcion del Problema

1. Comparar y discutir la dependencia de los criterios de peor caso nC, nN, nH frente a los parámetros ε y δ.

2. Calcular nC, nN, nH para ε = 0.01, δ = [ 0.001, 0.01, 0.05 ]

# IV. Descripcion de la Solucion

## Parte a)

 nC, nN y nH es la notación comúnmente utilizada para referirse al tamaño de muestra necesario para satisfacer cada uno de los tres enfoques que se vieron en la sesion 4:

  - nC: Tamaño de muestra necesario para satisfacer la desigualdad de Chebyshev.
  - nN: Tamaño de muestra necesario para satisfacer el Teorema Central del Límite.
  - nH: Tamaño de muestra necesario para satisfacer el Teorema de Hoeffding.

El criterio de peor caso de Chebyshev (nC) depende de la varianza de la distribucion aleatoria X (δ^2) y de la precision deseada (ε). Esta formula nos da un limite inferior conservador para el tamaño de muestra necesario para la precision deseada. A medida que la precision deseada (ε) se agudiza, el tamaño de muestra necesario (nC) se incrementa.

Por otro lado, un criterio mas optimista es el Teorema Central del Límite (nN).
Se dice que es mas optimista porque nos proporciona una estimacion del tamaño de la muestra sin necesidad de conocer la distribucion de los datos, asume que los datos provienen de una distribucion normal. El tamaño de muestra necesario (nN) depende de la desviacion estandar de la poblacion (δ) y de la precision deseada (ε). A medida que la precision deseada (ε) se agudiza, el tamaño de muestra necesario (nN) se incrementa.

Finalmente, el Teorema de Hoeffding (nH) es un criterio que tambien depende de la precision deseada (ε) y del nivel de confianza (δ). Pero cuenta con la particularidad de que no es necesario conocimeinto previo de la varianza de la distribucion de los datos. La fórmula nos proporciona un enfoque conservador que tiene en cuenta la convergencia de la suma de variables aleatorias independientes y acotadas hacia su media. Quizas su principal desventaja sea el hecho de que no se puede aplicar siempre, dado que depende de suposiciones especificas como:

- Las variables aleatorias son independientes, identicamente distribuidas y acotadas.

Al igual que el criterio de Chebyshev y el TCL, el tamaño de muestra necesario (nH) depende de la precision deseada (ε) y a medida que esta se agudiza, el tamaño de muestra necesario (nH) se incrementa.

## Parte b)

La solución fue programada en **Python 3.11.2**, usando las siguientes librerías:

  - **scipy.stats**: se utilizó para obtener la distribución normal inversa.
  - **math**: se utilizó para obtener el logaritmo natural y la función de redondeo hacia arriba *ciel*.

  *(Atencion: scipy no es una libreria nativa de python, por lo que es necesario instalarla previamente)*

El código proporcionado implementa una serie de funciones para calcular el número mínimo de muestras necesarias para garantizar un nivel de precisión y confianza.

Hay tres funciones definidas:
- **n_of_samples_chebyshev()**
- **n_of_samples_normal()**
- **n_of_samples_hoeffding()**

Cada una de estas funciones toma un nivel de confianza **delta** y una precisión deseada **eps** como argumentos, y devuelve el número mínimo de muestras necesarias para garantizar que la estimación esté dentro de la precisión deseada.

La función **main()** es el punto de entrada del programa y ejecuta un bucle que itera sobre los niveles de confianza en la lista **DELTAS**. Para cada nivel de confianza, la función **main()** llama a cada una de las tres funciones de cálculo de muestras con los valores de **EPS** y **delta** correspondientes. Los resultados de cada cálculo se imprimen en la consola.

# V. Resultados Computacionales

1. MacBook Air, Apple M1, 2020, 8GB RAM, ptython 3.11.2
2. Semilla: NO CORRESPONDE;
3. $(anexo) python3 exercise_4_1.py


| epsilon   | delta        | nC (Chebyshev) | nN (Teo central limite) | nH (Hoeffding) |
|-----------|--------------|-------------|-----------|----------|
| eps=0.01 | delta=0.001 | nC=2500000 | nN=27069 | nH=38005 |
| eps=0.01 | delta=0.01  | nC=250000  | nN=16588 | nH=26492 |
| eps=0.01 | delta=0.05  | nC=50000   | nN=9604  | nH=18445 |


# VI. Anexo

Consultar la carpeta ~/anexo por los logs, capturas, código de la solucion y demás archivos de interés.
