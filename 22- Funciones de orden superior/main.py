"""
/*
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
 * lista de calificaciones), utiliza funciones de orden superior para
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
 */
"""
from datetime import datetime

students = [
    {'name':'Pablo',
     'surname':'Calvo',
     'birthdate':'31-12-1991',
     'qualifications':[3,5,8]
     },
     {'name':'Jose',
     'surname':'Sepaz',
     'birthdate':'12-03-1994',
     'qualifications':[10,9,8]
      },
     {'name':'Aldo',
     'surname':'Bonzi',
     'birthdate':'15-06-1987',
     'qualifications':[10,9,8]
      }
]

def calculate_average(grades:list):
    return sum(grades)

# Creamos un map con los nombres y el promedio de sus notas
print(list(map(lambda students: {'name':students['name'], 'average': calculate_average(students['qualifications'])},students)))

# Filtrar alumnos que su promedio sea mayor igual a 9
print(list(map(lambda students:
               students['name'],
                filter(lambda students: calculate_average(students['qualifications']) >= 9,students)
               )))

# Obtiene los alumnos ordenados por su fecha de nacimiento
print(sorted(students, key=lambda student: datetime.strptime(student['birthdate'], "%d-%m-%Y"), reverse=True))

# Obtener la nota maxima de nota
print(max(map(lambda students: max(students['qualifications']),students)))