
class nodoPelicula:
    def __init__(self, pelicula):
        self.pelicula = pelicula
        self.siguiente = None

class listaVerMasTarde:
    def __init__(self):
        self.cabeza = None

    def agregar(self, pelicula):
        nuevo_nodo = nodoPelicula(pelicula)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        print(f"'{pelicula.titulo}' se ha agregado a 'Ver mas tarde.'")

    def mostrar(self):
        if not self.cabeza:
            print("Tu lista 'Ver mas tarde' esta vacia.")
            return
        print("=== Lista 'Ver mas tarde' ===")        
        actual = self.cabeza
        while actual:
            print(f"'{actual.pelicula._titulo}' ({actual.pelicula._genero})")
            actual = actual.siguiente