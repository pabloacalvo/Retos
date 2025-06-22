from ConversorDolares import ConversorDolares

if __name__ == "__main__":
    conversor_dolares = ConversorDolares()
    print(conversor_dolares.cotizacion)
    # dolares a pesos
    print(conversor_dolares.convert_valor1_a_valor2(1500))
   