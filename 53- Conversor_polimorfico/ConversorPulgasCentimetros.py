from Conversor import Conversor

class ConversorPulgadasCentimetros(Conversor):
    __VALOR_PULGADA = 2.54;

    @property
    def valor_pulgadas(self):
        return self.__VALOR_PULGADA
    
    def convert_valor1_a_valor2(self, valor_1: float):
        return valor_1 * self.__VALOR_PULGADA

    def convert_valor2_a_valor1(self, valor_2: float):
        return valor_2 / self.__VALOR_PULGADA

    def get_tipo(self):
        return "Pulgadas a Centimetros"
    
    def show_valor_pulgada(self):
        return self.valor_pulgadas