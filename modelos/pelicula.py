class Pelicula:
    """Representa un elemento del catálogo."""

    def __init__(self, titulo: str, director: str, actores: list[str], genero: str, universo: str, subcategoria: str = ""):
        self._titulo = titulo
        self._director = director
        self._actores = actores
        self._genero = genero
        self._universo = universo
        self._subcategoria = subcategoria

    @property
    def titulo(self) -> str:
        return self._titulo
    
    @property
    def actores(self) -> list[str]:
        return self._actores

    @property
    def genero(self) -> str:
        return self._genero
    
    @property
    def universo(self) -> str:
        return self._universo

    @property
    def subcategoria(self) -> str:
        return self._subcategoria

    def __repr__(self) -> str:
        return f"{self._titulo} ({self._genero}) ({self._subcategoria}) - Universo: {self._universo} | Director: {self._director}"