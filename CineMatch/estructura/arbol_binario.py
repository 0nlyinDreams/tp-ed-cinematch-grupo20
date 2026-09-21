class Nodo:
    def __init__(self, clave: str, valor=None):
        self.clave = clave.strip().lower()  # Guardamos la clave en minúsculas para comparar fácil
        self.valor = valor                  # Objeto Película
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    # --- INSERCIÓN ---
    def insertar(self, clave: str, valor=None) -> None:
        """Inserta una película en el árbol según su título."""
        if self.raiz is None:
            self.raiz = Nodo(clave, valor)
        else:
            self._insertar_recursivo(self.raiz, clave.strip().lower(), valor)

    def _insertar_recursivo(self, nodo_actual: Nodo, clave: str, valor) -> None:
        if clave < nodo_actual.clave:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(clave, valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, clave, valor)
        elif clave > nodo_actual.clave:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(clave, valor)
            else:
                self._insertar_recursivo(nodo_actual.derecho, clave, valor)
        else:
            nodo_actual.valor = valor

    # --- BÚSQUEDA ---
    def buscar(self, clave: str):
        """Busca una película por título en tiempo O(log n)."""
        return self._buscar_recursivo(self.raiz, clave.strip().lower())

    def _buscar_recursivo(self, nodo_actual: Nodo, clave: str):
        if nodo_actual is None:
            return None
        if clave == nodo_actual.clave:
            return nodo_actual.valor
        elif clave < nodo_actual.clave:
            return self._buscar_recursivo(nodo_actual.izquierdo, clave)
        else:
            return self._buscar_recursivo(nodo_actual.derecho, clave)

    # --- RECORRIDOS ---
    def inorder(self) -> list:
        resultado = []
        self._inorder_recursivo(self.raiz, resultado)
        return resultado

    def _inorder_recursivo(self, nodo_actual: Nodo, resultado: list) -> None:
        if nodo_actual is not None:
            self._inorder_recursivo(nodo_actual.izquierdo, resultado)
            resultado.append((nodo_actual.clave, nodo_actual.valor))
            self._inorder_recursivo(nodo_actual.derecho, resultado)

    def preorder(self) -> list:
        resultado = []
        self._preorder_recursivo(self.raiz, resultado)
        return resultado

    def _preorder_recursivo(self, nodo_actual: Nodo, resultado: list) -> None:
        if nodo_actual is not None:
            resultado.append((nodo_actual.clave, nodo_actual.valor))
            self._preorder_recursivo(nodo_actual.izquierdo, resultado)
            self._preorder_recursivo(nodo_actual.derecho, resultado)

    def postorder(self) -> list:
        resultado = []
        self._postorder_recursivo(self.raiz, resultado)
        return resultado

    def _postorder_recursivo(self, nodo_actual: Nodo, resultado: list) -> None:
        if nodo_actual is not None:
            self._postorder_recursivo(nodo_actual.izquierdo, resultado)
            self._postorder_recursivo(nodo_actual.derecho, resultado)
            resultado.append((nodo_actual.clave, nodo_actual.valor))