import random
import time
import matplotlib.pyplot as plt
import sys


class BuscadorDeParesOriginal:

    def __init__(self, argv):
        self.argv = argv  # corrección aquí
        self.ejecutar()

    @staticmethod
    def convertir_lista(lista):
        return list(map(int, lista))

    @staticmethod
    def encontrar_pares(arr, suma):
        pares = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] == suma:
                    pares.append((arr[1], arr[j]))
        return pares

    @staticmethod
    def leer_archivo(nombre):
        with open(nombre, 'r') as archivo:
            lineas = list(map(str.strip, archivo.readlines()))
        return lineas

    def ejecutar(self):

        if len(self.argv) == 3:
            lista = self.convertir_lista(self.argv[1].split(','))

            resultado = self.encontrar_pares(lista, int(self.argv[2]))  # corrección aquí
            print(*resultado, sep='\n')
        elif len(self.argv) == 2:
            tex = self.leer_archivo(self.argv[1])
            for i in range(len(tex)):
                lista = self.convertir_lista(tex[i].split()[0].split(','))  # corrección aquí
                resultado = self.encontrar_pares(lista, int(tex[i].split()[1]))  # corrección aquí
                print(*resultado, sep='\n')
        else:
            print("Los datos no son correctos")


class BuscadorDeParesModificado:

    def __init__(self, argv):
        self.argv = argv  # corrección aquí
        self.ejecutar()

    @staticmethod
    def convertir_lista(lista):
        return list(map(int, lista))

    @staticmethod
    def encontrar_pares(arr, suma):
        pares = []
        complementos = {}  # Usaremos un diccionario para almacenar los complementos necesarios.

        for num in arr:
            complemento = suma - num
            if complemento in complementos:
                pares.append((num, complemento))
            complementos[num] = True  # Agregamos el número al diccionario.

        return pares

    @staticmethod
    def leer_archivo(nombre):
        with open(nombre, 'r') as archivo:
            lineas = list(map(str.strip, archivo.readlines()))
        return lineas

    def ejecutar(self):
        if len(self.argv) == 3:
            lista = self.convertir_lista(self.argv[1].split(','))

            resultado = self.encontrar_pares(lista, int(self.argv[2]))  # corrección aquí
            print(*resultado, sep='\n')
        elif len(self.argv) == 2:
            tex = self.leer_archivo(self.argv[1])
            for i in range(len(tex)):
                lista = self.convertir_lista(tex[i].split()[0].split(','))  # corrección aquí
                resultado = self.encontrar_pares(lista, int(tex[i].split()[1]))  # corrección aquí
                print(*resultado, sep='\n')
        else:
            print("Los datos no son correctos")


def medir_tiempo_ejecucion(clase, n):
    lista = [random.randint(1, 1000) for _ in range(n)]
    suma_aleatoria = random.randint(2, 2000)

    inicio = time.time()
    buscador = clase([None, ', '.join(map(str, lista)), str(suma_aleatoria)])
    fin = time.time()

    return fin - inicio


def graficar_tiempos():
    tamaños = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 100]
    tiempos_original = []
    tiempos_modificado = []

    for n in tamaños:
        tiempos_original.append(medir_tiempo_ejecucion(BuscadorDeParesOriginal, n))
        tiempos_modificado.append(medir_tiempo_ejecucion(BuscadorDeParesModificado, n))

    fig, axs = plt.subplots(1, 3, figsize=(15, 5))  # Cambia a una sola fila y tres columnas

    axs[0].plot(tamaños, tiempos_original, '-o', color='blue')
    axs[0].set_title('Versión original (O(n^2))')
    axs[0].set_xlabel('Tamaño de la entrada')
    axs[0].set_ylabel('Tiempo de ejecución (segundos)')
    axs[0].grid(True)

    axs[1].plot(tamaños, tiempos_modificado, '-o', color='green')
    axs[1].set_title('Versión modificada (O(n))')
    axs[1].set_xlabel('Tamaño de la entrada')
    axs[1].set_ylabel('Tiempo de ejecución (segundos)')
    axs[1].grid(True)

    axs[2].plot(tamaños, tiempos_original, '-o', color='blue', label='Original (O(n^2))')
    axs[2].plot(tamaños, tiempos_modificado, '-o', color='green', label='Modificada (O(n))')
    axs[2].set_title('Comparación Directa')
    axs[2].set_xlabel('Tamaño de la entrada')
    axs[2].set_ylabel('Tiempo de ejecución (segundos)')
    axs[2].grid(True)
    axs[2].legend()

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    graficar_tiempos()
