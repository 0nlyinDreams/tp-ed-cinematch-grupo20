import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from estructura.avl import AVL, comparar_bst_vs_avl
from estructura.arbol_general import ArbolGeneral

class Elemento:
    def __init__(self, titulo, categoria):
        self.titulo = titulo
        self.categoria = categoria
    def __repr__(self):
        return f"{self.titulo}({self.categoria})"

def probar():
    datos = [
        Elemento("A", 1),
        Elemento("B", 2),
        Elemento("C", 3),
        Elemento("D", 4),
        Elemento("E", 5),
        Elemento("F", 6),
        Elemento("G", 7),
        Elemento("H", 8),
        Elemento("I", 9),
        Elemento("J", 10),
    ]
    avl = AVL()
    for d in datos:
        avl.insertar(d, clave=lambda x: x.titulo.lower())
    print(f"altura del AVL: {avl.altura()}")
    print(f"cantidad de nodos en el AVL: {len(avl)}")
    
    print("buscar 'F':", avl.buscar(valor="f", clave=lambda x: x.titulo.lower()))
    print("buscar 'Z':", avl.buscar(valor="z", clave=lambda x: x.titulo.lower()))

    print("comparacion bst vs avl")
    resultado = comparar_bst_vs_avl(datos, clave=lambda x: x.titulo.lower())
    if "error" in resultado:
        print(" Aviso:", resultado ["error"])
    else:
        print(f" altura bst comun: {resultado['altura_bst']}")
        print(f" altura arbol avl: {resultado['altura_avl']}")
        print(f" ¿el avl tiene mejor balance?: {resultado['mejor_balance']}")

        print("\n" + "="*45 + "\n")

        print("categorias")
        arbol = ArbolGeneral()
        raiz = arbol.insertar_raiz("Peliculas")

        ciencia = arbol.agregar_hijo(raiz, "ciencia Ficción")
        accion = arbol.agregar_hijo(raiz, "Acción")

        arbol.agregar_hijo(ciencia, "Avatar")
        arbol.agregar_hijo(ciencia, "Prometheus")
        arbol.agregar_hijo(accion, "Avengers: Endgame")

        print(f"raiz del arbol: {arbol.raiz.dato}")
        print(f"altura del arbol: {arbol.altura()}")
        print(f"cantidad total de nodos: {arbol.cantidad_nodos()}")

        print("BFS")
        print(arbol.amplitud())

        print("busqueda de categoria 'Avatar'")
        print("resultado:", arbol.buscar("Avatar"))

if __name__ == "__main__":
    probar()