# I. Unidad 5 - Sesión 15 - Ejemplo de Aplicaciones -  Ejercicio 15.1

# II. Integrantes

* Santiago Alaniz, CI 50826476, santiago.alaniz@fing.edu.uy

# III. Descripción del Problema

Elejir y estudiar uno de los trabajos mencionados en la `Unidad 5`. Realizar un breve resumen del trabajo, explicando:

- Que problema se intenta resolver o estudiar.
- Que metodos se proponen (mencionar las similutudes y diferencias con los metodos vistos a lo largo del curso).
- Conclusiones y resultados del trabajo, potenciales debilidades.

# IV. Analisis del articulo: "From Monte Carlo to Quantum Computation" - Stefan Heinrich

## **Que problema se intenta resolver o estudiar.**

En primera instancia, el autor expone una breve introduccion a este novedoso campo de investigacion.

Para ello, en el articulo se listan resultados teoricos que han sido fundacionales y tambien motivadores para el desarrollo de la computacion cuantica. (Historia de la computacion cuantica, Sistemas de Bits cuanticos, Compuertas Cuanticas, etc.)

Sin embargo, estos avances han "limitado" en cierta medida lo que es el area de estudio en el concepto mas amplio del termino. Ya que pareciera ser que la mayoria de los esfuerzos se centran en estudiar problemas discretos, como puede ser el caso de la factorizacion de numeros enteros.

El porque es mas que evidente, se han demostrado soluciones a problemas discretos que obtienen ordenes de complejidad mas bajos y desconocidos para la computacion clasica. [1](Shor Algorithm)

Por lo tanto, el autor propone una discusion alternativa, en particular, se introducen los avances en integracion matematica utilizando computacion cuantica.

Y lo que es el punto central del articulo, como se desempenan teoricamente estos metodos frente al ya conocido metodo de Monte Carlo para la integracion.

## **Metodos propuestos y su relacion con los vistos en el curso.**

La primera relacion con lo estudiado en el curso resulta ser una de las caracteristicas de la computacion cuantica.

En la genesis de su funcionamiento, la computacion cuantica se basa en la superposicion de estados, lo que permite realizar operaciones en paralelo.

Una de las manifestaciones de este principio es la transformación de Walsh-Hadamard[2], que genera una superposición de todos los posibles estados cuánticos. Cuando se mide, esta superposición genera un número aleatorio verdadero, respaldado por la entropía inherente a la física cuántica.

Esta característica contrasta notablemente con la computación clásica, que depende de algoritmos deterministas para generar números pseudo-aleatorios utilizados en los métodos de Monte Carlo. O, como ya hemos visto en el curso, obtener numeros verdadeamente aleatorios a partir de fenomenos fisicos. [3]

Despues, obviamente teniendo en cuenta que se trata de una lectura altamente tecnica y especilizada. La integracion numerica mediante algoritmos cuanticos, es al menos, en su base, similar a lo visto en el curso. Ya que se trata de una aproximacion a la media de resultados de la funcion a integrar. [4]

Y lo que es mas, el articulo propone un algoritmo cuantico para la integracion numerica [5], con metodologia inspirada en tecnicas utilizas en los metodos Monte Carlo.

A grandes rasgos, Se introduce una variable de control[6], separando la integral de la funcion, con un parametro de interpolacion. El operador de interpolación está diseñado para proporcionar el mejor orden de aproximación a la función que se está integrando.

El valor de la integral de la parte principal se puede calcular exactamente con un costo lineal, mientras que la integral del residuo se aproxima usando una sumatoria, en la cual se puede aplicar la computación cuántica para obtener una mejora en la eficiencia.

Este resultado prueba que la computación cuántica puede ser más eficiente que la computación clásica para la integración numérica.

El resto de los teoremas intentan definir limites inferiores y superiores para la la integracion numerica, a partir de la naturaleza de la funcion a integrar.

## **Conclusiones y resultados del trabajo, potenciales debilidades.**

El artículo presenta teoremas que demuestran la existencia de algoritmos cuánticos eficientes para resolver problemas de suma y de integración. Estos algoritmos pueden ser significativamente más eficientes que los métodos clásicos (tanto determinísticos como aleatorizados).

Ademas, los algoritmos cuánticos presentados superan a los métodos clásicos en términos de eficiencia y precisión. Los resultados sugieren que, en términos de complejidad asintótica, los algoritmos cuánticos pueden ofrecer un speedup significativo sobre los métodos clásicos. [7]

Sin embargo, aunque estos algoritmos cuánticos pueden ser muy eficientes en teoría, la aplicación práctica de la computación cuántica aún está en sus primeras etapas. Se necesita una gran cantidad de recursos físicos y técnicos para implementar estos algoritmos en la práctica, lo que puede limitar su uso.

En particular, En los teoremas, se asume la existencia de ciertas subrutinas cuánticas que pueden no ser factibles o fáciles de implementar en la práctica.

Finalmente, La eficiencia de estos algoritmos cuánticos se pone de manifiesto especialmente para conjuntos de datos grandes. Sin embargo, para conjuntos de datos más pequeños, es posible que los métodos clásicos sean suficientemente eficientes.


# VI. Anexo

Citas:

- [[1] - Algoritmo de Shor](https://es.wikipedia.org/wiki/Algoritmo_de_Shor)
- [[2] - Transformacion de Walsh-Hadamard](https://en.wikipedia.org/wiki/Hadamard_transform#Quantum_computing_applications)
- [[3] - Random.org](https://www.random.org/)
- [[4] - Brassard, Hoyer Mosca and Tapp](https://arxiv.org/abs/quant-ph/0005055)
- [[5] - Novak, Quantum complexity of integration](https://arxiv.org/abs/quant-ph/0008124)
- [6] - FING, Metodos Montecarlo, Unidad 5 Sesion 13,14 Metodos para aumentar la Eficiencia.
- [7] - Tabla de Resultados (anexo/exercise_15_1.pdf)

Paper:
`From Monte Carlo to Quantum Computation - Stefan Heinrich`



`Consultar la carpeta ~/anexo por el articulo original.`
