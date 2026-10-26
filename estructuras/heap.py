class Ranking:
    def __init__(self):
        self._elementos = []

    def esta_vacio(self):
        return len(self._elementos) == 0

    def insertar(self, valor):
        self._elementos.append(valor)
        self._subir(len(self._elementos) - 1)

    def extraer_maximo(self):
        if self.esta_vacio():
            return None
        maximo = self._elementos[0]
        ultimo = self._elementos.pop()
        if not self.esta_vacio():
            self._elementos[0] = ultimo
            self._bajar(0)
        return maximo

    def _subir(self, indice):
        while indice > 0:
            padre = (indice - 1) // 2
            if self._elementos[indice][0] > self._elementos[padre][0]:
                self._intercambiar(padre, indice)
                indice = padre
            else:
                break

    def _bajar(self, indice):
        cantidad = len(self._elementos)
        while True:
            izq = 2 * indice + 1
            der = 2 * indice + 2
            mayor = indice
            if izq < cantidad and self._elementos[izq][0] > self._elementos[mayor][0]:
                mayor = izq
            if der < cantidad and self._elementos[der][0] > self._elementos[mayor][0]:
                mayor = der
            if mayor == indice:
                break
            self._intercambiar(indice, mayor)
            indice = mayor

    def _intercambiar(self, i, j):
        self._elementos[i], self._elementos[j] = self._elementos[j], self._elementos[i]