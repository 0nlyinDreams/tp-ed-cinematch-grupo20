# Análisis Comparativo de Estrategias de Búsqueda (TP3)

## 1. Análisis Teórico de Complejidad

| Estrategia | Complejidad temporal (Peor Caso) | Complejidad espacial | Requiere orden previo |
| :--- | :---: | :---: | :---: |
| **Búsqueda Secuencial** | $O(n)$ | $O(1)$ | No |
| **Búsqueda Binaria** | $O(\log n)$ | $O(1)$ | Sí |
| **Árbol Binario (BST)** | $O(\log n)$ | $O(n)$ | No (ordena al insertar) |

---

## 2. Tabla de Tiempos Reales de Ejecución

| Método | Tiempo Promedio ($\mu s$) |
| :--- | :--- |
| **Búsqueda Secuencial** |  7.10 µs |
| **Búsqueda Binaria** |  8.90 µs |
| **Árbol Binario (BST)** |  5.60 µs |

---

## 3. Conclusión

1. **Eficiencia en búsqueda:** La búsqueda secuencial es de forma lineal $O(n)$, lo que resulta ineficiente a medida que la base de datos de películas crece. Tanto la búsqueda binaria como la búsqueda en árbol (BST) ofrecen complejidad logarítmica $O(\log n)$, reduciendo la cantidad de operaciones.
2. **Ventaja del Árbol:** Si bien la búsqueda binaria es rápida, necesita una lista explícitamente ordenada. El Árbol Binario de Búsqueda (BST) resuelve este problema y busca de sin necesidad de reordenar estructuras despues de cada modificación.