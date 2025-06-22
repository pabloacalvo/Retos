from abc import ABC, abstractmethod


class Conversor(ABC):
   
    @abstractmethod
    def get_tipo(self):
        pass

    @abstractmethod
    def convert_valor1_a_valor2(self, valor_1: float):
        pass
    
    @abstractmethod
    def convert_valor2_a_valor1(self, valor_2: float):
        pass