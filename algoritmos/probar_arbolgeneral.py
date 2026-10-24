import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from estructura.arbol_general import ArbolGeneral, NodoGeneral

def probar_arbol_general():
    print("--- PRUEBA DEL ÁRBOL GENERAL (Categorías) ---")
    arbol = ArbolGeneral()
    raiz = arbol.insertar_raiz("Películas")
    
    categorias = ["Acción", "Comedia", "Drama", "Aventura", "Ciencia Ficción", "Animación", "Crimen", "Terror"]
    for cat in categorias:
        arbol.agregar_hijo(raiz, cat)
    
    print("\nBFS:")
    print(arbol.amplitud())
    
    print("\nrecorrido preorder:")
    print(arbol.profundidad_preorder())

if __name__ == "__main__":
    probar_arbol_general()