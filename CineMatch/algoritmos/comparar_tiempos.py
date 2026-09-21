import time
from servicios.catalogo import Catalogo

def busqueda_secuencial(lista, titulo_buscado):
    titulo_buscado = titulo_buscado.strip().lower()
    for peli in lista:
        if peli.titulo.strip().lower() == titulo_buscado:
            return peli
    return None

def busqueda_binaria(lista_ordenada, titulo_buscado):
    titulo_buscado = titulo_buscado.strip().lower()
    inicio = 0
    fin = len(lista_ordenada) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        clave_medio = lista_ordenada[medio].titulo.strip().lower()

        if clave_medio == titulo_buscado:
            return lista_ordenada[medio]
        elif clave_medio < titulo_buscado:
            inicio = medio + 1
        else:
            fin = medio - 1
    return None

def medir_tiempos():
    catalogo = Catalogo()
    catalogo.cargar_desde_json("datos/peliculas.json")
    
    # Lista sin ordenar para secuencial, ordenada para binaria y el BST
    lista_peliculas = catalogo.listar()
    lista_ordenada = sorted(lista_peliculas, key=lambda p: p.titulo.strip().lower())
    
    titulo_a_buscar = "X-Men: First Class"  # Peor caso (está al final)

    # 1. Búsqueda Secuencial
    inicio = time.perf_counter()
    busqueda_secuencial(lista_peliculas, titulo_a_buscar)
    tiempo_secuencial = (time.perf_counter() - inicio) * 1_000_000  # a microsegundos

    # 2. Búsqueda Binaria
    inicio = time.perf_counter()
    busqueda_binaria(lista_ordenada, titulo_a_buscar)
    tiempo_binaria = (time.perf_counter() - inicio) * 1_000_000

    # 3. Búsqueda en Árbol (BST)
    inicio = time.perf_counter()
    catalogo.buscar_por_titulo(titulo_a_buscar)
    tiempo_arbol = (time.perf_counter() - inicio) * 1_000_000

    print("==================================================")
    print("      RESULTADOS DE MEDICIÓN DE TIEMPOS (µs)      ")
    print("==================================================")
    print(f"Búsqueda Secuencial : {tiempo_secuencial:.2f} µs")
    print(f"Búsqueda Binaria    : {tiempo_binaria:.2f} µs")
    print(f"Búsqueda Árbol (BST): {tiempo_arbol:.2f} µs")
    print("==================================================")

if __name__ == "__main__":
    medir_tiempos()