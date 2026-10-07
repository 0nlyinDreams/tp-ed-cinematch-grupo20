class NodoAVL:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class AVL:
    def __init__(self):
        self.raiz = None

    def _altura(self, nodo):
        return 0 if nodo is None else nodo.altura

    def _factor_balance(self, nodo):
        if nodo is None:
            return 0
        return self._altura(nodo.izquierda) - self._altura(nodo.derecha)

    def _actualizar_altura(self, nodo):
        nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))

    def _rotacion_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda
        y.izquierda = z
        z.derecha= T2
        self._actualizar_altura(z)
        self._actualizar_altura(y)
        return y

    def _rotacion_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha
        y.derecha = z
        z.izquierda = T3
        self._actualizar_altura(z)
        self._actualizar_altura(y)
        return y

    def _rotacion_izquierda_derecha(self, nodo):
        nodo.izquierda = self._rotacion_izquierda(nodo.izquierda)
        return self._rotacion_derecha(nodo)

    def _rotacion_derecha_izquierda(self, nodo):
        nodo.derecha = self._rotacion_derecha(nodo.derecha)
        return self._rotacion_izquierda(nodo)

    def insertar(self, dato, clave):
        self.raiz = self._insertar_recursivo(self.raiz, dato, clave)

    def _insertar_recursivo(self, nodo, dato, clave):
        if nodo is None:
            return NodoAVL(dato)
        if clave(dato) < clave(nodo.dato):
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, dato, clave)
        elif clave(dato) > clave(nodo.dato):
            nodo.derecha = self._insertar_recursivo(nodo.derecha, dato, clave)
        else:
            return nodo
        self._actualizar_altura(nodo)
        balance = self._factor_balance(nodo)
        if balance > 1 and clave(dato) < clave(nodo.izquierda.dato):
            return self._rotacion_derecha(nodo)
        if balance < -1 and clave(dato) > clave(nodo.derecha.dato):
            return self._rotacion_izquierda(nodo)
        if balance > 1 and clave(dato) > clave(nodo.izquierda.dato):
            return self._rotacion_izquierda_derecha(nodo)
        if balance < -1 and clave(dato) < clave(nodo.derecha.dato):
            return self._rotacion_derecha_izquierda(nodo)
        
        return nodo

    def buscar(self, clave, valor):
        return self._buscar_recursivo(self.raiz, clave, valor)

    def _buscar_recursivo(self, nodo, clave, valor):
        if nodo is None:
            return None
        variable_nodo = clave(nodo.dato)
        if valor == variable_nodo:
            return nodo.dato
        if valor < variable_nodo:
            return self._buscar_recursivo(nodo.izquierda, clave, valor)
        return self._buscar_recursivo(nodo.derecha, clave, valor)

    def inorden(self):
        resultado = []
        self._inorder_rec(self.raiz, resultado)
        return resultado
    def _inorder_rec(self, nodo, resultado):
        if nodo:
            self._inorder_rec(nodo.izquierda, resultado)
            resultado.append(nodo.dato)
            self._inorder_rec(nodo.derecha, resultado)
    def preorden(self):
        resultado = []
        self._preorder_rec(self.raiz, resultado)
        return resultado
    def _preorder_rec(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.dato)
            self._preorder_rec(nodo.izquierda, resultado)
            self._preorder_rec(nodo.derecha, resultado)
    def postorden(self):
        resultado = []
        self._postorder_rec(self.raiz, resultado)
        return resultado
    def _postorder_rec(self, nodo, resultado):
        if nodo:
            self._postorder_rec(nodo.izquierda, resultado)
            self._postorder_rec(nodo.derecha, resultado)
            resultado.append(nodo.dato)

    def altura(self):
        return self._altura(self.raiz)
    def __len__(self):
        return self._contar(self.raiz)
    def _contar(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar(nodo.izquierda) + self._contar(nodo.derecha)

def comparar_bst_vs_avl(lista_datos, clave):
        import time
        try:
            from arbol_binario import ArbolBST
        except ImportError:
            return {"error": "No se encontro arbol_binario.py"}
        bst = ArbolBST()
        for d in lista_datos:
            bst.insertar(d, clave=clave)
        avl = AVL()
        for d in lista_datos:
            avl.insertar(d, clave=clave)
        valores = clave(lista_datos[0])
        t0 = time.time()
        for _ in range(1000):
            bst.buscar(valores, clave=clave)
        t_bst = (time.time() - t0) * 1000
        t0 = time.time()
        for _ in range(1000):
            avl.buscar(valores, clave=clave)
        t_avl = (time.time() - t0) * 1000
        return {
            "altura_bst": bst.altura(),
            "altura_avl": avl.altura(),
            "tiempo_bst_ms": t_bst,
            "tiempo_avl_ms": t_avl,
            "mejor_balance": avl.altura() < bst.altura()
        }