# AnalisisAlgoritmos
Repositorio para Análisis de Algoritmos

Integrantes: 
* Pablo Arturo Rodríguez
  
* Carlos Borja
  
* Angie Tatiana Peña

* Andrés Rueda

* Juan David Aldana

* Santiago Guerrero

Informe de los cambios realizados a la propuesta del reto
El código original contiene un algoritmo que busca pares de elementos en una lista cuya suma sea igual a un valor objetivo (suma). El algoritmo original tiene una complejidad de O(n^2) debido a que utiliza dos bucles anidados para comparar todas las combinaciones posibles de elementos en la lista. 
Para mejorar la complejidad y optimizar el rendimiento del algoritmo, se propuso una versión modificada que tiene una complejidad de O(n). A continuación, se explican la propuesta que realizamos en el grupo: 


•	Utilización de un diccionario para almacenar complementos: En la versión modificada, se utiliza un diccionario para almacenar los complementos necesarios para que la suma de un número con otro sea igual al valor objetivo. Esto permite evitar la necesidad de recorrer toda la lista en busca de un complemento en cada iteración. El acceso a los elementos en un diccionario es de tiempo constante, lo que reduce la complejidad del algoritmo. 


•	Eliminación del bucle interno: En el código original, se utilizaban dos bucles anidados para recorrer todas las combinaciones posibles de elementos en la lista. En la versión modificada, se eliminó el bucle interno y se utilizó el diccionario para verificar la existencia del complemento necesario. Esto reduce la cantidad de iteraciones y mejora el rendimiento del algoritmo.


•	Evaluación del rendimiento: Para evaluar el rendimiento de ambas versiones del algoritmo, se realizó una comparación directa de los tiempos de ejecución utilizando diferentes tamaños de entrada (n) y se graficaron los resultados. 
En general, la versión modificada del algoritmo es más eficiente y escalable en comparación con el código original. La utilización de un diccionario para almacenar los complementos necesarios permite reducir la complejidad del algoritmo de O(n^2) a O(n), lo que resulta en un mejor rendimiento, especialmente para listas de tamaño grande.


Además, la visualización gráfica de los tiempos de ejecución para diferentes tamaños de entrada muestra claramente cómo la versión modificada tiene un comportamiento más lineal, mientras que la versión original muestra un crecimiento más cuadrático, lo que confirma la mejora en la complejidad y rendimiento. 


En resumen, la versión modificada del algoritmo representa una mejora significativa en términos de complejidad y rendimiento, lo que la convierte en una opción más eficiente para buscar pares de elementos con una suma objetivo en una lista.

