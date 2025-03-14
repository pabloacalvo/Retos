"""
Programa que reciba un string en numeros romanos y devuelva el valor en numeros enteros 
"""

class RomanConverter:
    # Diccionario con los valores en orden descendente
    _roman_dict = {
        "M": 1000, 
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    @classmethod
    def get_numerals(cls):
        # Devuelve una lista de tuplas con el caracter y su valor
        return cls._roman_dict

    @classmethod
    def convert_to_int(cls,roman_value:str):
        result = 0 # Variable para almacenar el resultado
        skip_next = False
        for i,value in enumerate(roman_value): # Recorro la palabra
            # Valida si ya se procesaron dos caracteres para saltar la iteracion.
            if skip_next:
                skip_next = False
                continue
            #print( i,value ,cls._roman_dict[value],str(len(roman_value)-1)) # Obtengo el valor de cada Letra y posicion
            #print(roman_value[i:i+2])
            
            # Valida que sea el ultimo elemento o que su valor + el proximo caracter este en la tabla de datos (Ej: IV, CM)
            if i + 1 == len(roman_value) or roman_value[i:i+2] in cls._roman_dict:
                result += cls._roman_dict[roman_value[i:i+2]] # Sumo el valor del elemento de dos caracteres
                skip_next = True # Flag para saltar el proximo recorrido ya que se procesaron dos caracteres del string
            else:
                result += cls._roman_dict[value] # Se suma el valor de un caracter indivual (Ej: X,V,I, etc)
        
        return result
    
    @classmethod
    def convert_to_roman(cls, int_value:int):
        result = []
        for key, value in cls._roman_dict.items():
            while int_value >= value:
                result.append(key)
                int_value -= value

        return "".join(result)

            


print(RomanConverter.convert_to_int("MCMXCIV"))  # 1994
print(RomanConverter.convert_to_int("MMXXIII"))  # 2023
print(RomanConverter.convert_to_int("XLII"))     # 42
print(RomanConverter.convert_to_int("DCCC"))     # 800
print(RomanConverter.convert_to_int("IX"))       # 9


print(RomanConverter.convert_to_roman(1923))
print(RomanConverter.convert_to_roman(2023))
print(RomanConverter.convert_to_roman(42))        
print(RomanConverter.convert_to_roman(800))
print(RomanConverter.convert_to_roman(9))