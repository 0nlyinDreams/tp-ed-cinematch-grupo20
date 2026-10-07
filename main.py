from servicios.catalogo import Catalogo
from ui.terminal import Terminal
from estructura.avl import AVL
from estructura.arbol_general import ArbolGeneral

def main() -> None:
    # 1 Creamos la logica del sistema
    catalogo = Catalogo()

     # 2 Cargamos datos de prueba
    catalogo.cargar_desde_json("datos/peliculas.json")
    print(f"Se cargaron {len(catalogo)} películas exitosamente.")

     # 3 Iniciamos la pantalla mostrando el catalago
    terminal = Terminal(catalogo)
    terminal.iniciar()
if __name__ == "__main__":
     main()


class Pelicula:
    def __init__(self, titulo, categoria):
          self.titulo = titulo
          self.categoria = categoria
    def __repr__(self):
        return f"Pelicula({self.titulo}, {self.categoria})"
def inicializar():
         avl = AVL()
         arbol = ArbolGeneral()

         raiz = arbol.insertar_raiz("Peliculas")
         c1 = arbol.agregar_hijo(raiz, "Ciencia Ficción")
         c2 = arbol.agregar_hijo(raiz, "Acción")

         arbol.agregar_hijo(c1, "Avatar")
         arbol.agregar_hijo(c1, "Prometheus")
         arbol.agregar_hijo(c2, "Avengers: Endgame")

         peliculas = [
              Pelicula("Avatar", "Ciencia Ficción"),
              Pelicula("Prometheus", "Ciencia Ficción"),
              Pelicula("Avengers: Endgame", "Acción"),
         ]
         for p in peliculas:
              avl.insertar(p, lambda x: x.titulo.lower())
         return avl, arbol
def menu():
         avl, arbol = inicializar()
         while True:
            print ("\n1. Buscar pelicula (AVL)")
            print("2. Explorar categorias (Arbol General)")
            print("3. Salir")
            opcion = input("\nOpcion: ").strip()
            if opcion == "1":
                 t = input("titulo a buscar: ").strip().lower()
                 resultado = avl.buscar(t, lambda x: x.titulo.lower())
                 print("resultado:", resultado if resultado else "No encontrado")
            elif opcion == "2":
                 print("\nCategorias:")
                 for c in arbol.amplitud():
                      print(f" - {c}")
            elif opcion == "3":
                 break

if __name__ == "__main__":
    menu()