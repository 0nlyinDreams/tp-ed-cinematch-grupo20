class usuario: 
    """Representa a un usuario del sistema."""
    def __init__(self, id_usuario: int, nombre: str, genero_favorito: str):
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._genero_favorito = genero_favorito

    @property
    def id_usuario(self) -> int:
        return self._id_usuario

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def genero_favorito(self) -> str:
        return self._genero_favorito

    def __repr__(self) -> str:
        return f"Usuario: {self._nombre} (Prefiere: {self._genero_favorito})"
