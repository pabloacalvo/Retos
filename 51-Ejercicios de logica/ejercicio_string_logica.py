"""
El usuario ingresa una cadena de caracteres(string) donde es seguro que dentro de ella habra un numero en sistema binario, si resulta
ser que el numero es par, entonces el programa debera imprimirlo en sistema decimal, en caso controario se imprimie el string ingresado 
sin el numero binario.
El string que el usuario va ingresar, podra tener letras y cualquier simbolo de puntuacion, pero en cuanto a numero solo tendra los 0
y 1 correspondiente al numero binario
"""

test = "a0d0kld1dkjsds1"


number = "".join(char for char in test if char.isdigit())
characters = "".join(char for char in test if char.isalpha())



"""
Dada una frase de texto, comprobar si es u palindromo o no. 
"""
text = input("Ingresa el texto: ").lower()

word_list = text.split(" ")
invert_word_list = [word[::-1] for word in word_list]


for word in word_list:
    for word2 in invert_word_list:
        if word== word2:
            print(f"Palindromo encontrado \n Normal:{word} Invertida: {word2}")
        
