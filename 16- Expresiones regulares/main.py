"""
/*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */
"""

"""
/d -> digito numerico
/w -> digito alfanumerico
/s -> espacio en blanco
/D -> no numerico
/W -> no alfanumerico
/S -> no es un espacio en blanco

Cuantificadores

+ -> aparece 1 o mas veces
{n} -> se repite n veces
{n,m} -> se repite entre n m veces
{n,} -> de n veces hacia arriba
* -> cero o mas veces
? -> 1 o cero veces
"""

import re




def find_numbers(text:str)->list:
    patron = r"\d+"
    return re.findall(patron,text)


def email_validate(email:str):
    patron_mail = r"\w+\@\w+\.com"
    n = re.search(patron_mail,email)
    if n is not None:
        print("Correo electronico correcto")
    else:
        print("Correo incorrecto")

def telephone_validate(telephone:str,is_celular=False):
    if not is_celular:
        patron = r"^\d{4,8}+$"
    else:
        patron = r"^15\d{8}$"
    result = re.search(patron,telephone)
    if result is not None:
        print("Telefono valido")
    else:
        print("Telefono invalido")

def url_validate(url:str):
    patron = r"^http[s]?://(wwww.)?"
    result = re.search(patron,url)
    if result is not None:
        print("URL Correcta")
    else:
        print("URL Incorrecta")

frase = "Hoy es Domingo 18 de agosto, es decir 18/08/2024"
print(find_numbers(frase))

mail = "+pablocalvo@live.com"
email_validate(mail)

telefono = "1531813930"
telephone_validate(telefono,True)

url = "http://www.google.com"
url_validate(url)