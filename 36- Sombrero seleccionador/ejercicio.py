""""
/*
 * EJERCICIO:
 * Cada 1 de septiembre, el Hogwarts Express parte hacia la escuela
 * de programación de Hogwarts para magos y brujas del código.
 * En ella, su famoso sombrero seleccionador ayuda a los programadores
 * a encontrar su camino...
 * Desarrolla un programa que simule el comportamiento del sombrero.
 * Requisitos:
 * 1. El sombrero realizará 10 preguntas para determinar la casa del alumno.
 * 2. Deben existir 4 casas. Por ejemplo: Frontend, Backend, Mobile y Data.
 *    (Puedes elegir las que quieras)
 * Acciones:
 * 1. Crea un programa que solicite el nombre del alumno y realice 10
 *    preguntas, con cuatro posibles respuestas cada una.
 * 2. Cada respuesta asigna puntos a cada una de las casas (a tu elección).
 * 3. Una vez finalizado, el sombrero indica el nombre del alumno
 *    y a qué casa pertenecerá (resuelve el posible empate de manera aleatoria,
 *    pero indicándole al alumno que la decisión ha sido complicada).
 */
"""
import random

houses = dict(
    Lanus = 0,
    Boca = 0,
    River = 0,
    Banfield = 0
)

questions = [
    {'question': '¿Quién tiene más Libertadores?',
     'responses': ['Boca', 'Independiente', 'San Lorenzo', 'Lanus'],
     'true_response': 1
    },
    {'question': '¿En qué año Lanús ganó su primer torneo?',
     'responses': ['2001', '2002', '2007', '1996'],
     'true_response': 1
    },
    {'question': '¿Qué equipo tiene más títulos locales?',
     'responses': ['River', 'Boca', 'Independiente', 'Racing'],
     'true_response': 1
    },
    {'question': '¿Cuál es el apodo del club Banfield?',
     'responses': ['El Taladro', 'El Xeneize', 'Los Millonarios', 'El Granate'],
     'true_response': 1
    },
    {'question': '¿En qué año River descendió a la B?',
     'responses': ['2009', '2010', '2011', '2012'],
     'true_response': 1
    },
    {'question': '¿Qué equipo es conocido como "Los Millonarios"?',
     'responses': ['Boca', 'Independiente', 'River', 'San Lorenzo'],
     'true_response': 1
    },
    {'question': '¿En qué año Boca ganó su primera Copa Libertadores?',
     'responses': ['1977', '1978', '1981', '1962'],
     'true_response': 1
    },
    {'question': '¿Cuál es el estadio de Lanús?',
     'responses': ['La Bombonera', 'El Monumental', 'La Fortaleza', 'Cilindro de Avellaneda'],
     'true_response': 1
    },
    {'question': '¿Qué equipo tiene más campeonatos de Primera División?',
     'responses': ['River', 'Boca', 'Independiente', 'Vélez'],
    'true_response': 1
     },
    {'question': '¿Cuál es el apodo del club Boca Juniors?',
     'responses': ['El Rojo', 'El Taladro', 'El Xeneize', 'El Granate'],
     'true_response': 1
    }
]

def print_questionnaire(candidate):
    print(f"Empezamos {candidate.capitalize()}".center(50, "*"))
    for question in questions:
        print(question['question'])
        cont_respon = 1
        for response in question['responses']:
            print(f"{cont_respon}\t {response}")
            cont_respon += 1
        select = int(input())
        if select == question['true_response']:
            select_house = random.choice(list(houses.keys()))
            houses[select_house] += 1

    max_point = max(houses.values())
    tie_validation = [team for team, points in houses.items() if points == max_point ]
    print(houses)
    if len(tie_validation) != 0:
        select_house = random.choice(tie_validation)
        print(f'{candidate} la decicion fue dificl!! pero fuiste seleccionado al equipo: {select_house}')
    else:
        print(f'{candidate} fuiste seleccionado al equipo: {tie_validation}')



name = input("Bienvenido, ingresa tu nombre: ")
print(f"Un gusto {name} a continuacion te voy hacer 10 preguntas y tenes que seleccionar la repuesta correcta")


print_questionnaire(name)
