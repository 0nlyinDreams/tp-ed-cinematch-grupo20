from servicios.catalogo import Catalogo

def probar_arbol() -> None:
    print("==================================================")
    print("      PRUEBA DE ÁRBOL BINARIO DE BÚSQUEDA (BST)  ")
    print("==================================================")

    # 1. Iniciamos el caralogo y cargamos el archivo de peliculas 
    catalogo = Catalogo()
    catalogo.cargar_desde_json("datos/peliculas.json")
    print(f"Se cargaron {len(catalogo)} películas en el catálogo.")

    # 2. Prueba de busqueda
    print("--- 1. Prueba de busqueda---")

    peli_1 = catalogo.buscar_por_titulo("Spider-Man 2")
    if peli_1:
        print(f"Busqueda exitosa ('Spider-Man 2'): Encontrada ({peli_1.titulo})")
    else:
        print("No se encontro 'Spider-Man 2'")

    peli_2 = catalogo.buscar_por_titulo("shrek")  #Prueba en minúsculas
    if peli_2:
        print(f" Búsqueda exitosa ('shrek'): Encontrada ({peli_2.genero})")
    else:
        print(" No se encontró 'shrek'")

    peli_3 = catalogo.buscar_por_titulo("Batman")  #No está en el catalogo JSON
    if peli_3 is None:
        print(" Búsqueda correcta ('Batman'): Devuelve None porque no existe en el árbol.")

# 3. Recorrido
    print("--- 2. Recorrido del Árbol ---")
    arbol = catalogo._arbol

    print("* Recorrido Inorden (debe mostrar los títulos ordenados alfabéticamente):")
    for clave, pelicula in arbol.inorder():
        print(f"  - {pelicula.titulo}")

    print("* Recorrido Preorden:")
    preorden_titulos = [pelicula.titulo for clave, pelicula in arbol.preorder()]
    print(f"  {preorden_titulos[:5]} ... ({len(preorden_titulos)} elementos en total)")

    print("* Recorrido Postorden:")
    postorden_titulos = [pelicula.titulo for clave, pelicula in arbol.postorder()]
    print(f"  {postorden_titulos[:5]} ... ({len(postorden_titulos)} elementos en total)")

if __name__ == "__main__":
    probar_arbol()