from servicios.catalogo import Catalogo
from estructura.arbol_general import ArbolGeneral
from servicios.recomendador import GrafoRecomendador
from estructuras.heap import Ranking

class Terminal: 
    def __init__(self, catalogo: Catalogo) -> None:
        self._catalogo = catalogo
        # Inicializamos el Árbol General para las categorías (Opción 2)
        self._arbol_categorias = ArbolGeneral()
        self._inicializar_arbol_categorias()
        #grafo
        self._recomendador = GrafoRecomendador()
        self._recomendador.construir_grafo(self._catalogo.listar())

    def _inicializar_arbol_categorias(self) -> None:
        raiz = self._arbol_categorias.insertar_raiz("Películas")
        categorias = ["Acción", "Comedia", "Drama", "Aventura", "Ciencia Ficción", "Animación", "Crimen", "Terror", "Fantasia"]
        #accion
        nodo_accion= self._arbol_categorias.agregar_hijo(raiz, "Acción")
        self._arbol_categorias.agregar_hijo(nodo_accion, "Superheroes")
        self._arbol_categorias.agregar_hijo(nodo_accion, "Artes Marciales")
        self._arbol_categorias.agregar_hijo(nodo_accion, "Espionaje y Agentes")
        #ciencia ficcion
        nodo_cf = self._arbol_categorias.agregar_hijo(raiz, "Ciencia Ficción")
        self._arbol_categorias.agregar_hijo(nodo_cf, "Aventura Espacial")
        self._arbol_categorias.agregar_hijo(nodo_cf, "Dinosaurios y Mounstros")
        #terror
        nodo_terror = self._arbol_categorias.agregar_hijo(raiz, "Terror")
        self._arbol_categorias.agregar_hijo(nodo_terror, "Sobrenatural")
        self._arbol_categorias.agregar_hijo(nodo_terror, "Psicologico")
        #fantasia
        nodo_fantasia = self._arbol_categorias.agregar_hijo(raiz, "Fantasia")
        self._arbol_categorias.agregar_hijo(nodo_fantasia, "Mundos Magicos")
        self._arbol_categorias.agregar_hijo(nodo_fantasia, "Magia y Hechiceria")
        self._arbol_categorias.agregar_hijo(nodo_fantasia, "Fantasia Oscura")
        #animacion
        nodo_animacion = self._arbol_categorias.agregar_hijo(raiz, "Animación")
        self._arbol_categorias.agregar_hijo(nodo_animacion, "Anime")
        self._arbol_categorias.agregar_hijo(nodo_animacion, "Princesas")
        self._arbol_categorias.agregar_hijo(nodo_animacion, "Comedia animada")
        self._arbol_categorias.agregar_hijo(raiz, "Comedia")
        self._arbol_categorias.agregar_hijo(raiz, "Drama")
        self._arbol_categorias.agregar_hijo(raiz, "Aventura")
        self._arbol_categorias.agregar_hijo(raiz, "Crimen")
        
        #for cat in categorias:
         #   self._arbol_categorias.agregar_hijo(raiz, cat)

    def iniciar(self) -> None:
        # Un bucle que no muere en la primera opción
        while True:
            self._mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                self._buscar_titulo()
            elif opcion == "2":
                self._explorar_categorias()
            elif opcion == "3":
                self._filtrar_genero()
            elif opcion == "4":
                self._filtrar_universo()
            elif opcion == "5":
                self._ver_top_5()
            elif opcion == "6":
                self._recomendar()
            elif opcion == "7":
                self._ver_mas_tarde()
            elif opcion == "0":
                print("¡Hasta la próxima!")
                break
            else:
                print("Opción inválida.")
            print()

            if opcion != "0":
                print("\n" + "-" * 40)
                print("1. Volver al menu principal.")
                print("2. Salir.")
                siguiente = input("Elije una opcion: ").strip()
                if siguiente == "2":
                    print("¡Hasta la proxima!")
                    break

    def _mostrar_menu(self) -> None:
        print("=" * 40)
        print("        CineMatch (v1)")
        print("=" * 40)
        print("1. Buscar película por título")
        print("2. Explorar categorias")
        print("3. Filtrar por género")
        print("4. Filtrar por universo")
        print("5. Ver TOP 5")
        print("6. Obtener recomendaciones")
        print("7. Mi lista 'Ver más tarde'")
        print("0. Salir")
        print("-" * 40)

    def _buscar_titulo(self) -> None:
        titulo = input("Título a buscar: ").strip()
        result = self._catalogo.buscar_por_titulo(titulo)
        if result:
            print(f"Encontrada: {result}")
        else:
            print(f"No encontramos: '{titulo}'.")

    def _explorar_categorias(self) -> None:
        print("\n--- Categorías ---")
        #categorias = self._arbol_categorias.amplitud()[1:]
        #for categoria in categorias:
        #for c in self._arbol_categorias.amplitud():
         #   print(f" - {categoria}")
        nodo_raiz = self._arbol_categorias.raiz #buscar("Peliculas")

        for genero in nodo_raiz.hijos:
            lista_genero = self._catalogo.filtrar_por_genero(genero.dato)
            cantidad_genero = len(lista_genero)
            print(f"[{genero.dato}] ({cantidad_genero})")
            for sub in genero.hijos:
                lista_sub = self._catalogo.filtrar_por_subcategoria(sub.dato)
                cantidad_sub = len(lista_sub)
                print(f"  └── {sub.dato} ({cantidad_sub})")

        eleccion = input("Ingrese la categoria o subcategoria que quiere ver: ").strip()
        resultados = self._catalogo.filtrar_por_subcategoria(eleccion)

        if not resultados:
            resultados = self._catalogo.filtrar_por_genero(eleccion)

        if resultados:
            print(f"Peliculas de {eleccion}")
            for pelicula in resultados:
                print(f"- {pelicula.titulo} (Dir: {pelicula._director})")
        else:
            print(f"No encontramos peliculas para '{eleccion}'.")

    def _filtrar_genero(self) -> None:
        genero = input("Genero: ").strip()
        result = self._catalogo.filtrar_por_genero(genero)

        if result:
            for pelicula in result:
                print(f"- {pelicula}")
        else:
            print(f"No hay películas del género '{genero}'.")

    def _filtrar_universo(self) -> None:
        universo = input("Universo: ").strip()
        result = self._catalogo.filtrar_por_universo(universo)

        if result:
            for pelicula in result:
                print(f"- {pelicula}")
        else:
            print(f"No hay películas del universo '{universo}'.")
            
    def _ver_top_5(self) -> None:
        print("--- Top 5 Peliculas ---")
        top_5_pelis = self._catalogo.obtener_top_5()
        if not self._ver_top_5:
            print("No hay peliculas disponibles en el catalogo")
            return
        for i, peli in enumerate(top_5_pelis, start=0):
            print(f"{i + 1}. {peli.titulo} - {peli.rating}")
           

    def _recomendar(self) -> None:
        #print("Función de recomendaciones próximamente.")
        print("--- Sistema de Recomendaciones ---")
        titulo_buscado = input("Ingrese una pelicula para obtener recomendaciones: ")
        pelicula_encontrada= self._catalogo.buscar_por_titulo(titulo_buscado)
        if pelicula_encontrada:
            similares = self._recomendador.obtener_similares(pelicula_encontrada.titulo)
            if similares:
                print(f"Porque te gusto '{pelicula_encontrada.titulo}', te recomendamos:")
                for sim in similares:
                    print(f" └─ {sim}")
            else: 
                print(f"Por ahora no tenemos recomendaciones")
        else:
            print("No encontramos esa pelicula en el catalogo")

        
    def _ver_mas_tarde(self) -> None:
        print("Tu lista 'Ver más tarde' está vacía.")
