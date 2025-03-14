from pilas import PilaDeque

class Navegador:
    def __init__(self):
        self.historial_atras = PilaDeque()
        self.historial_adelante = PilaDeque()
        self.pagina_actual = None

    def visitar(self, pagina):
        if self.pagina_actual is not None:
            self.historial_atras = pagina
            # Limpiar el historial adelante al visitar una nueba pagina
            self.historial_adelante = PilaDeque()

    def atras(self):
        if self.historial_atras.esta_vacia():
            print("No hay pagina para hacia atras.")
            return
        self.historial_adelante.agregar(self.pagina_actual)
        self.pagina_actual = self.historial_atras.eliminar()


