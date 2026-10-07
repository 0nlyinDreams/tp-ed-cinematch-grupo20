class NodoGeneral:
    def __init__(self, dato):
        self.dato = dato
        self.hijos = []

    def __repr__(self):
        return f"Nodo({self.dato})"

class ArbolGeneral:
    def __init__(self):
        self.raiz = None

    def insertar_raiz(self, dato):
        self.raiz = NodoGeneral(dato)
        return self.raiz

    def agregar_hijo(self, nodo_padre, dato):
        if nodo_padre is None and self.raiz is None:
            raise ValueError("el arbol no tiene raiz")
        nuevo = NodoGeneral(dato)
        nodo_padre.hijos.append(nuevo)
        return nuevo

    def buscar(self, valor):
        if self.raiz is None:
            return None
        cola = [self.raiz]
        while cola:
            actual = cola.pop(0)
            if actual.dato == valor:
                return actual
            cola.extend(actual.hijos)
        return None

    def amplitud(self):
        if self.raiz is None:
            return[]
        resultado = [self.raiz]
        cola = [self.raiz]
        while cola:
            actual = cola.pop(0)
            resultado.append(actual.dato)
            cola.extend(actual.hijos)
        return resultado

    def profundidad_preorder(self, nodo=None, resultado=None):
        if nodo is None:
            nodo = self.raiz
        if resultado is None:
            resultado = []
        if nodo is None:
            return resultado
        resultado.append(nodo.dato)
        for hijo in nodo.hijos:
            self.profundidad_preorder(hijo, resultado)
        return resultado

    def altura(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return 0
        if not nodo.hijos:
            return 1
        return 1 + max(self.altura(hijo) for hijo in nodo.hijos)

    def cantidad_nodos(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return 0
        return 1 + sum(self.cantidad_nodos(hijo) for hijo in nodo.hijos)
