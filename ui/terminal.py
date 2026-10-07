from servicios.catalogo import Catalogo

class Terminal: 
    """Interfaz de línea de comandos."""
    def __init__(self, catalogo: Catalogo) -> None:
        self._catalogo = catalogo

    def iniciar(self) -> None:
        # Un bucle que no muere en la primera opción
        while True:
            self._mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                self._buscar_titulo()
            elif opcion == "2":
                self._listar_todo()
            elif opcion == "3":
                self._filtrar_genero()
            elif opcion == "4":
                self._filtrar_universo()
            elif opcion == "5":
                self._recomendar
            elif opcion == "6":
                self._ver_mas_tarde
            elif opcion == "0":
                print("¡Hasta la próxima!")
                break
            else:
                print ("Opción inválida.")
            print()

    def _mostrar_menu(self) -> None:
        print("=" * 40) # Linea continua formada por 40 guiones
        print("         CineMatch (v1)")
        print("=" * 40)
        print("1. Buscar película por título")
        print("2. Catálogo")
        print("3. Filtrar por género")
        print("4. Filtrar por universo")
        print("5. Obtener recomendaciones")
        print("6. Mi lista 'Ver más tarde'")
        print("0. Salir")
        print("-" * 40)

    def _buscar_titulo(self) -> None:
        titulo = input("Título a buscar: ").strip()
        result = self._catalogo.buscar_por_titulo(titulo)
        if result:
            print(f"Encontrada: {result}")
        else:
            print(f"No encontramos: '{titulo}'.")

    def _listar_todo(self) -> None:
        peliculas = self._catalogo.listar()
        print(f"--- Mostrando {len(peliculas)} peliculas ---")
        for pelicula in peliculas:
            print(f"- {pelicula}")

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

