from modelos.usuarios import Usuario
from modelos.pelicula import Pelicula
from servicios.catalogo import Catalogo

class Recomendador:
    """Lógica de negocio para sugerir películas a los usuarios."""
    def __init__(self, catalogo: Catalogo) -> None:
        self._catalogo = catalogo

    def recomendador_por_universo(self, universo_favorito: str) -> list[Pelicula]:
        """Devuelve todas las películas que pertenecen a un universo específico"""
        return self._catalogo.filtrar_por_universo(universo_favorito)

class GrafoRecomendador:
    def __init__(self):
        self.lista_adyacencia = {}

    def agregar_nodo(self, pelicula: str) -> None:
        if pelicula not in self.lista_adyacencia:
            self.lista_adyacencia[pelicula] = []

    def agregar_arista(self, peli1: str, peli2: str) -> None:
        if peli1 in self.lista_adyacencia and peli2 in self.lista_adyacencia:
            if peli2 not in self.lista_adyacencia[peli1]:
                self.lista_adyacencia[peli1].append(peli2)
            if peli1 not in self.lista_adyacencia[peli2]:
                self.lista_adyacencia[peli2].append(peli1)

    def construir_grafo(self, lista_peliculas: list) -> None:
        for p in lista_peliculas:
            self.agregar_nodo(p.titulo)
        for i in range(len(lista_peliculas)):
            for j in range(i+1, len(lista_peliculas)):
                p1 = lista_peliculas[i]
                p2 = lista_peliculas[j]
                if p1.universo == p2.universo and p1.universo != "Independiente":
                    self.agregar_arista(p1.titulo, p2.titulo)

    def obtener_similares(self, pelicula: str) -> list:
        return self.lista_adyacencia.get(pelicula, [])

