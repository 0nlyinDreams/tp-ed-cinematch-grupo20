#import json
#from modelos.pelicula import Pelicula

#class Catalogo:
 #   """Lógica de negocio: carga y operaciones sobre el catálogo."""

  #  def __init__(self) -> None:
   #     self._elementos: list[Pelicula] = []

    #def cargar_desde_json(self, ruta: str) -> None:
        # Usamos encoding="utf-8" para procesar bien caracteres especiales
     #   with open(ruta, encoding ="utf-8") as archivo:
      #      datos = json.load(archivo)
       #     for item in datos:
        #        self._elementos.append(
         #           Pelicula(
          #              item["titulo"],
           #             item["director"],
            #            item["actores"],
             #           item["genero"],
              #          item["universo"]
               #     )
                #)
    #def buscar_por_titulo(self, titulo: str) -> Pelicula | None: 
     #   """Búsqueda exacta por título, sin distinguir mayúsculas."""
      #  for pelicula in self._elementos:
       #     if pelicula.titulo.lower() == titulo.lower():
        #        return pelicula
        #return None
    #def listar(self) -> list[Pelicula]:
     #   return list(self._elementos)
    #def filtrar_por_genero(self, genero: str) -> list[Pelicula]:
     #   return[
      #      p for p in self._elementos
       #     if p.genero.lower() == genero.lower()
        #]
    #def filtrar_por_universo(self, universo: str) -> list[Pelicula]:
    #     return[
     #        p for p in self._elementos
      #      if p.universo.lower() == universo.lower()
       #  ]
    #def buscar_por_director(self, director: str) -> list[Pelicula]:
     #   """Devuelve todas las películas de un mismo director."""
      #  return[
       #     p for p in self._elementos
        #    if p.director.lower() == director.lower()
        #]
    #def __len__(self) -> int:
     #   return len(self._elementos)

import json
from modelos.pelicula import Pelicula
from estructura.arbol_binario import ArbolBinarioBusqueda as ArbolBinario
from estructuras.heap import Ranking
class Catalogo:
    """Lógica de negocio: carga y operaciones sobre el catálogo."""

    def __init__(self) -> None:
        self._elementos: list[Pelicula] = []
        self._arbol = ArbolBinario()  # Inicializamos el árbol binario de búsqueda

    def cargar_desde_json(self, ruta: str) -> None:
        # Usamos encoding="utf-8" para procesar bien caracteres especiales
        with open(ruta, encoding ="utf-8") as archivo:
            datos = json.load(archivo)
            for item in datos:
                pelicula = Pelicula(
                    item["titulo"],
                    item["director"],
                    item["actores"],
                    item["genero"],
                    item["universo"],
                    item.get("subcategoria", "general"),
                    rating =item.get("rating", 0.0)
                )
                self._elementos.append(pelicula)
                # Insertamos cada pelicula cargada en el arbol usando el titulo como clave
                self._arbol.insertar(pelicula.titulo, pelicula)

    def buscar_por_titulo(self, titulo: str) -> Pelicula | None:
        """Búsqueda exacta por título usando el Árbol Binario."""
        return self._arbol.buscar(titulo)  # Buscamos en el árbol usando el título en minúscula

    def listar(self) -> list[Pelicula]:
        return list(self._elementos)

    def filtrar_por_genero(self, genero: str) -> list[Pelicula]:
        return [
            p for p in self._elementos
            if p.genero.lower() == genero.lower()
        ]

    def filtrar_por_universo(self, universo: str) -> list[Pelicula]:
        return [
            p for p in self._elementos
            if p.universo.lower() == universo.lower()
        ]   

    def obtener_top_5(self) -> list:
        ranking_heap = Ranking()
        for peli in self.listar():
            ranking_heap.insertar((peli.rating, peli.titulo, peli))
        top_5 = []
        for _ in range(5):
            if ranking_heap.esta_vacio():
                break
            _, _, pelicula = ranking_heap.extraer_maximo()
            top_5.append(pelicula)
        return top_5

   # def buscar_por_director(self, director: str) -> list[Pelicula]:
    #    """Devuelve todas las películas de un mismo director."""
     #   return [
      #      p for p in self._elementos
       #     if p.director.lower() == director.lower()
        #]   

    def filtrar_por_subcategoria(self, subcategoria: str) -> list[Pelicula]:
        #return [
         #   p for p in self._elementos
        #]
        lista_filtrada = []
        for p in self._elementos:
            if p._subcategoria.strip().lower() == subcategoria.strip().lower():
                lista_filtrada.append(p)
        return lista_filtrada
    
    def __len__(self) -> int:
        return len(self._elementos)