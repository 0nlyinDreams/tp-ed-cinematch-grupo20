from servicios.catalogo import Catalogo
from ui.terminal import Terminal

def main() -> None:
    # 1 Creamos la logica del sistema
    catalogo = Catalogo()

     # 2 Cargamos datos de prueba
    catalogo.cargar_desde_json("datos/peliculas.json")
    print(f"Se cargaron {len(catalogo)} películas exitosamente.")

     # 3 Iniciamos la pantalla mostrando el catalago
    terminal = Terminal(catalogo)
    terminal.iniciar()
if __name__ == "__main__":
     main()