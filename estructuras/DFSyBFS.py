from collections import deque
class recorridos:
    def __init__(self, grafo):
        self.grafo = grafo 
    def BFS(self, inicio):
        visitados={inicio}
        cola= deque([inicio])
        orden=[]
        while cola:
            u= cola.popleft()
            orden.append(u)
            for v in self.vecinos(u):
                if v not in visitados:
                    visitados.add(v)
                    cola.append(v)
        return orden
    def DFS(self, inicio):
        visitados= set()
        orden=[]
        def visitar(u):
            visitados.add(u)
            orden.append(u)
            for v in self.vecinos(u):
                if v not in visitados:
                    visitar(v)
        visitar(inicio)
        return orden
    def DFS_iterativo(self, inicio):
        visitados= set()
        pila=[inicio]
        orden=[]
        while pila:
            u= pila.pop()
            if u in visitados:
                continue
            visitados.add(u)
            orden.append(u)
            for v in reversed(self.vecinos(u)):
                if v not in visitados:
                    pila.append(v)
        return orden
                
