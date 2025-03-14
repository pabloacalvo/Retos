from collections import deque

class PilaDeque():
    def __init__(self):
        self.items = deque()

    def esta_vacia(self):
        return len(self.items) == 0
    
    def agregar(self,item):
        self.items.append(item)

    def eliminar(self):
        if not self.esta_vacia():
            return self.items.pop()
        
    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        raise IndexError["Pila vacia"]
        
    # Agregar elemento: enqueue
    def encolar(self, item):
        self.items.append(item)

    # Retirar elemento delante de la cola: Dequeue
    def desencolar(self,item):
        self.items.popleft()