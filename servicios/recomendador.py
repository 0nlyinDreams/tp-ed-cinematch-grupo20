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